#include <iostream>
using namespace std;
int T,Tn,H,W;
int s[102][102];
int vx[102][102],vy[102][102];
bool flag[102][102];
int val[102][102];
const int dx[4]={-1,0,0,1};
const int dy[4]={0,-1,1,0};
int i,j,k,tmp,tmpk;
void work(int x, int y)
{
     if (flag[x][y] && flag[vx[x][y]][vy[x][y]])
     {
         work(vx[x][y],vy[x][y]);
         int tmpx,tmpy;
         tmpx=vx[x][y];
         tmpy=vy[x][y];
         vx[x][y]=vx[tmpx][tmpy];
         vy[x][y]=vy[tmpx][tmpy];
     }
        
}
int main()
{
    freopen("B-large.in.txt","r",stdin);
    freopen("B-large.out.txt","w",stdout);
    scanf("%d",&T);
    for (Tn=1;Tn<=T;Tn++)
    {
        memset(s,-1,sizeof(s));
        scanf("%d%d",&H,&W);
        for (i=1;i<=H;i++)
            for (j=1;j<=W;j++)
                scanf("%d",&s[i][j]);
        memset(flag,false,sizeof(flag));
        for (i=1;i<=H;i++)
            for (j=1;j<=W;j++)
            {
                tmp=s[i][j];
                tmpk=-1;
                for (k=0;k<4;k++)
                    if (s[dx[k]+i][dy[k]+j]!=-1 && s[dx[k]+i][dy[k]+j]<tmp)
                    {
                        tmp=s[dx[k]+i][dy[k]+j];
                        tmpk=k;
                    }
                if (tmpk!=-1)
                {
                    flag[i][j]=true;
                    vx[i][j]=dx[tmpk]+i;
                    vy[i][j]=dy[tmpk]+j;
                }
                else
                {
                    vx[i][j]=i;
                    vy[i][j]=j;
                }
            }
        for (i=1;i<=H;i++)
            for (j=1;j<=W;j++)
                work(i,j);
        memset(val,-1,sizeof(val));
        k=0;
        printf("Case #%d:\n",Tn);
        for (i=1;i<=H;i++)
        {
            for (j=1;j<=W;j++)
            {
                if (val[vx[i][j]][vy[i][j]]==-1)
                {
                    val[vx[i][j]][vy[i][j]]=k;
                    k++;
                }
                printf("%c ",val[vx[i][j]][vy[i][j]]+'a');
            }
            printf("\n");
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
