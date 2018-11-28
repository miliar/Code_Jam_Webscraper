//最大完备子图算法
#include<stdio.h>

const int maxe=1024;
const int maxn=81;
const int R=10;
char g[maxn][maxn];
bool e[maxe][maxe];
int ans[maxn][maxe];
int row,col,len;

int getbit(int x)
{
    int sum=0;
    while(x>0) sum+=x%2,x/=2;
    return sum;
}

bool canseat(int x,char g[])
{
    int i;
    int f[maxn];
    for(i=0;i<col;i++) f[i]=x%2,x/=2;
    for(i=1;i<col;i++) if(f[i]==1 && f[i-1]==1) return false;
    for(i=0;i<col;i++) if(f[i]==1 && g[i]=='x') return false;
    return true;
}

bool canreach(int x,int y)
{
    int i,f1[maxn],f2[maxn];
    for(i=0;i<col;i++) f1[i]=x%2,x/=2;
    for(i=0;i<col;i++) f2[i]=y%2,y/=2;
    for(i=0;i<col;i++) if(f2[i]){
        if(i-1>=0 && f1[i-1]==1) return false;
        if(i+1<col && f1[i+1]==1) return false;
    }
    return true;
}

int solve()
{
    int i,j,k;
    for(i=0;i<row;i++){
        for(j=0;j<len;j++){
            if(!canseat(j,g[i])) ans[i][j]=0;
            else{
                if(i==0) ans[i][j]=getbit(j);
                else{
                    ans[i][j]=0;
                    for(k=0;k<len;k++){
                        if(e[k][j] && ans[i][j]<ans[i-1][k]){
                            ans[i][j]=ans[i-1][k];
                        }
                    }
                    ans[i][j]+=getbit(j);
                }
            }
            //printf("%d\n",ans[i][j]);
        }
    }
    j=0;
    for(i=0;i<len;i++) if(j<ans[row-1][i]) j=ans[row-1][i];
    return j;
}

void input()
{
    int i,j;
    scanf("%d%d",&row,&col);
    for(i=0;i<row;i++) scanf("%s",&g[i]);
    len=(1<<col);
    for(i=0;i<len;i++){
        for(j=0;j<len;j++){
            e[i][j]=canreach(i,j);
        }
    }
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int i,T;
    scanf("%d",&T);
    for(i=1;i<=T;i++){
        input();
        printf("Case #%d: %d\n",i,solve());
    }
    //while(1);
    return 0;
}
