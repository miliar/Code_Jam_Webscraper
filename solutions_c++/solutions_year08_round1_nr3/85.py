#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;
const long N = 1000,INF=1e16,D=1e11;
const double eps = 1e-10;
inline long max(long a,long b){return a>b?a:b;}
inline long min(long a,long b){return a<b?a:b;}
inline void swap(__int64 &a,__int64 &b){__int64 tt;tt=a,a=b,b=tt;}
long n,m;
long mat[2][2]={0,1,-4,6};
long ans[2][2],tmp[2][2];
void Init()
{
    long n1=6,n2=28;
   // n=20;
    scanf("%ld",&n);
  /*  long n3;
    n-=2;
    while(n--)
    {
        n3=((n2*6-n1*4)%1000+1000)%1000;
        //printf("%ld\n",n3);
        n1=n2;n2=n3;
    }
    printf("%03ld\n",n2%1000-1);*/

}
void mul(long a[2][2],long b[2][2],long c[2][2])
{
    long i,j,k;
    for(i=0;i<2;i++)
        for(j=0;j<2;j++)
        {
            a[i][j]=0;
            for(k=0;k<2;k++)
            {
                a[i][j]+=b[i][k]*c[k][j];
                a[i][j]=(a[i][j]%1000+1000)%1000;
            }
        }
}
void cpy(long a[2][2],long b[2][2])
{
    long i,j,k;
    for(i=0;i<2;i++)
        for(j=0;j<2;j++)a[i][j]=b[i][j];
}
void Solve()
{
    long i,j,k;
    if(n==2){printf("027\n");return;}
    ans[0][0]=ans[1][1]=1;
    ans[0][1]=ans[1][0]=0;
    mat[0][0]=0;
    mat[0][1]=1;
    mat[1][0]=-4;
    mat[1][1]=6;
   // printf("%ld n\n",n);
    n-=2;
    while(n)
    {
        if(n&1)
        {
            mul(tmp,ans,mat);
            cpy(ans,tmp);
        }
        n>>=1;
        mul(tmp,mat,mat);
        cpy(mat,tmp);
    }
    long res=0;
    res=6*ans[1][0]+28*ans[1][1];
    printf("%03ld\n",((res+999)%1000+1000)%1000);
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long T,K=1;scanf("%ld",&T);

    while(T--)
    {
        printf("Case #%ld: ",K++);
        Init();
        Solve();
    }
    //Init();
    return 0;
}
