/*
TASK: code jam b water
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>
#define INF 2000000000

int map[110][110];
int index[110][110];
int head[20000];
int alph[20000];

int findhead(int x)
{
    if(x!=head[x])
        head[x]=findhead(head[x]);
    return head[x];
}

inline void uset(int a, int b)
{
//    printf("union %d %d\n", a,b);
    int ha=findhead(a), hb=findhead(b);    
    head[hb]=ha; return;
}

int main()
{
    int t,cc,h,w,i,j,mm;
    char top;
    
    scanf("%d", &t);
    
    w=0;
    
    for(i=0;i<110;i++)
        for(j=0;j<110;j++)
            index[i][j]=w++;
    
    for(cc=0;cc<t;cc++)
    {
        for(i=0;i<110;i++)
            for(j=0;j<110;j++)
                map[i][j]=INF;
        for(i=0;i<20000;i++)
        {
            head[i]=i;
            alph[i]=0;
        }
    
        scanf("%d%d", &h,&w);
        
        for(i=1;i<=h;i++)
            for(j=1;j<=w;j++)
                scanf("%d", &map[i][j]);
        
        for(i=1;i<=h;i++)
            for(j=1;j<=w;j++)
            {
                mm = INF;
                if(mm>map[i-1][j])
                    mm=map[i-1][j];
                if(mm>map[i+1][j])
                    mm=map[i+1][j];
                if(mm>map[i][j-1])
                    mm=map[i][j-1];
                if(mm>map[i][j+1])
                    mm=map[i][j+1];
                
                if(mm>=map[i][j])
                    continue; //sink
                
                if(mm==map[i-1][j])
                    uset(index[i][j],index[i-1][j]);
                else if(mm==map[i][j-1])
                    uset(index[i][j],index[i][j-1]);
                else if(mm==map[i][j+1])
                    uset(index[i][j],index[i][j+1]);
                else if(mm==map[i+1][j])
                    uset(index[i][j],index[i+1][j]);
            }
        
        top='a';
        
        printf("Case #%d:\n", cc+1);
        
        for(i=1;i<=h;i++)
        {
            for(j=1;j<=w;j++)
            {
                if(alph[findhead(index[i][j])]==0)
                    alph[findhead(index[i][j])]=top++;
                printf("%c ", alph[findhead(index[i][j])] );
            }
            printf("\n");
        }
    }
    
    return 0;
}
