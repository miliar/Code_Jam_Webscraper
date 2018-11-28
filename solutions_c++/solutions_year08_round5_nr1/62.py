#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
using namespace std;

inline long min(long a,long b){return a<b?a:b;}
inline long max(long a,long b){return a>b?a:b;}
inline long swap(long &a,long &b){long tt;tt=a,a=b,b=tt;}

const long N = 2000000,INF = 1<<28;
const double eps = 1e-8,pi=acos(-1);
long n,m;
char s[1005][1005];
long f[3005][3005];
long c[1005];
void Init()
{
    long i,j,k;
    scanf("%ld",&n);
    for(i=0;i<n;i++)
    {
        scanf("%s %ld",s[i],c+i);
    }
}
long nx,ny,dir;
long dx[]={-1,0,1,0};
long dy[]={0,1,0,-1};
bool In(long x,long y)
{
    long i;
    long tmp=0;
    for(i=y+1;i<1000;i++)if(f[x][i])tmp++;
    return (tmp%2);
}
bool ab(long x,long y)
{
    long i,ff;
    ff=0;
    for(i=y+1;i<1000;i++)if(f[x][i]){ff=1;break;}
    if(!ff)return 0;
    ff=0;
    for(i=y-1;i>0;i--)if(f[x][i]){ff=1;break;}
    if(!ff)return 0;
    return 1;
}
bool cd(long x,long y)
{
    long i,ff;
    ff=0;
    for(i=x+1;i<1000;i++)if(f[i][y]){ff=1;break;}
    if(!ff)return 0;
    ff=0;
    for(i=x-1;i>0;i--)if(f[i][y]){ff=1;break;}
    if(!ff)return 0;
    return 1;
}
void Solve()
{
    long i,j,k;
    long tx,ty;
    memset(f,0,sizeof(f));
    long mnx,mny,mxx,mxy;
    mnx=mny=500;
    mxx=mxy=500;
    nx=500,ny=500,dir=0;
    for(i=0;i<n;i++)
    {
        for(j=0;j<c[i];j++)
        {
            for(k=0;s[i][k];k++)
            {
                tx=nx,ty=ny;
                if(s[i][k]=='F')
                {
                    nx+=dx[dir]*2,ny+=dy[dir]*2;
                    mnx<?=nx;mny<?=ny;
                    mxx>?=nx;mxy>?=ny;
                    f[(tx+nx)/2][(ty+ny)/2]=1;
                }
                else if(s[i][k]=='R'){dir++;dir%=4;}
                else {dir--;dir=(dir+4)%4;}
            }
        }
    }
    long ans=0;
    for(i=mnx-1;i<mxx+1;i+=2)
        for(j=mny-1;j<mxy+1;j+=2)
        {
            //printf("%ld %ld\n",i,j);
            if(!In(i,j)&&(ab(i,j)||cd(i,j)))ans++;
        }
    printf("%ld\n",ans);

}
int main()
{
    long T,K=1;
    freopen("i100.txt","r",stdin);
    freopen("o100.txt","w",stdout);
    scanf("%ld",&T);
    while(T--)
    {
        printf("Case #%ld: ",K++);
        Init();
        Solve();
    }
    return 0;
}
