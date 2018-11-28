#include <stdio.h>

#define MAX 52

char board[MAX][MAX];
char temp[MAX];

int T,N,K;
int redFind,blueFind;
struct
{
    int row,col;
}vector[4]={{0,1},{1,0},{1,1},{1,-1}};

void find(int row,int col,int type)
{
    int t;
    char color=board[row][col];
    if(color=='.') return;
    else if(color=='R'&&redFind) return;
    else if(color=='B'&&blueFind) return;

    for(t=0;t<K-1;t++)
    {
        row+=vector[type].row;
        col+=vector[type].col;
        if(color!=board[row][col])
            break;
    }
    if(t==K-1)
    {
        if(color=='R') redFind=1;
        else if(color='B') blueFind=1;
    }
}


void G()
{
    int i,j,m,p,q;
    char t;
    for(i=0;i<N;i++)
    {
        m=0;
        for(j=0;j<N;j++)
        {
            if(board[j][i]!='.')
            {
                temp[m]=board[j][i];
                m++;
                board[j][i]='.';
            }
        }
        q=0;
        for(p=N-m;p<N;p++)
        {
            board[p][i]=temp[q];
            q++;
        }
    }
}


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int i,j,k,t;

    scanf("%d",&T);
    for(i=0;i<T;i++)
    {
        scanf("%d%d",&N,&K);
        getchar();
        for(j=0;j<N;j++)
        {
            t=N-j-1;
            for(k=0;k<N;k++)
            {
                scanf("%c",&board[k][t]);
            }
            getchar();
        }

        G();

        printf("Case #%d: ",i+1);

        redFind=0;
        blueFind=0;
        t=N-K;
        for(j=0;j<N;j++)
            for(k=0;k<=t;k++)
                find(j,k,0);
        for(j=0;j<=t;j++)
            for(k=0;k<N;k++)
                find(j,k,1);
        for(j=0;j<=t;j++)
            for(k=0;k<=t;k++)
                find(j,k,2);
        for(j=0;j<=t;j++)
            for(k=K-1;k<N;k++)
                find(j,k,3);
                
        
        if(redFind&&blueFind)
            printf("Both\n");
        else if(redFind)
            printf("Red\n");
        else if(blueFind)
            printf("Blue\n");
        else 
            printf("Neither\n");

        
    }
}
