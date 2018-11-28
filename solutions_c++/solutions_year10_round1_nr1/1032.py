#include<stdio.h>

int dir[4][2]={{-1,1},{0,1},{1,1},{1,0}};
int n,K;
int flag[400];
char a[100][100],b[100][100],c[100];

int main()
{
    int i,j,T,x,y,v,num,cc;
    char ch;
    freopen("A-large.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&T);
    for(cc=1;cc<=T;cc++)
    {
        scanf("%d %d",&n,&K);
        for(i=0;i<n;i++)
            scanf("%s",a+i);

        for(j=0;j<n;j++)
        {
            num=0;
            for(i=0;i<n;i++)
            {
                ch=a[n-j-1][i];
                if(ch!='.')
                    c[++num]=ch;
            }
            for(i=n-1;i>=0;i--,num--)
                if(num>0)
                    b[i][j]=c[num];
                else
                    b[i][j]='.';


        }
        flag['R']=flag['B']=0;
        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
                if(b[i][j]!='.'&&flag[b[i][j]]==0)
                {
                    for(v=0;v<4;v++)
                    {
                        num=0;
                        x=i,y=j;
                        while(x>=0&&x<n&&y>=0&&y<n&&b[x][y]==b[i][j]&&num<K)
                        {
                            num++;
                            x=i+num*dir[v][0];
                            y=j+num*dir[v][1];
                           
                        }
                        if(num==K)
                            flag[b[i][j]]=1;
                        if(flag['R']&&flag['B'])
                            break;

                    }

                }
        printf("Case #%d: ",cc); 
        if(flag['R']==0&&flag['B']==0)
            printf("Neither\n");
        else if(flag['R']&&flag['B'])
            printf("Both\n");
        else if(flag['R'])
            printf("Red\n");
        else
            printf("Blue\n");

    }
    return 0;
}
