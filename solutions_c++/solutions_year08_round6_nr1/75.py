#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <set>

using namespace std;
const long N = 1000005,INF=1<<28;
const double eps = 1e-8,pi=acos(-1);
inline long min(long a,long b){return a<b?a:b;}
inline long max(long a,long b){return a>b?a:b;}
inline void swap(long &a,long &b){a^=b;b^=a;a^=b;}
//struct point{long x,y}p[N];
//inline void swap(point& a,point &b){point tt;tt=a;a=b;b=tt;}
long l[N],r[N],lt;
long h1,h2,w1,w2;
long th1,th2,tw1,tw2;
long n,m;
char s[100];
void Init()
{
    long i,j,k;
  ///  lt=lt2=0;
    scanf("%ld",&n);

    w1=tw1=th1=h1=INF;
    w2=tw2=th2=h2=-1;
    th1=tw1=-1;
    th2=tw2=INF;
    lt = 0;
    for(i=0;i<N;i++)l[i]=r[i]=0;
    bool flag=0;
    for(i=0;i<n;i++)
    {
        scanf("%ld%ld%s",&j,&k,s);
      //  printf("%ld %ld\n",j,k);
        if(s[0]=='B'){flag=1;h1<?=j;h2>?=j;w1<?=k;w2>?=k;}
        else{scanf("%s",s);l[lt]=j;r[lt++]=k;}
    }
    if(flag)
    for(i=0;i<lt;i++)
    {
        if(l[i]<h1&&r[i]>=w1&&r[i]<=w2)th1>?=l[i];
        if(l[i]>h2&&r[i]>=w1&&r[i]<=w2)th2<?=l[i];
        if(l[i]>=h1&&l[i]<=h2&&r[i]<w1)tw1>?=r[i];
        if(l[i]>=h1&&l[i]<=h2&&r[i]>w2)tw2<?=r[i];
    }
    scanf("%ld",&m);
  //  printf("%ld m\n",m);

}
bool isB(long j,long k)
{return j>=h1&&j<=h2&&k>=w1&&k<=w2;}
bool Nt(long j,long k)
{
    return j>=th2||j<=th1||k>=tw2||k<=tw1;
}
bool notB(long j,long k)
{
    long i;
    for(i=0;i<lt;i++)
    {
        if(w1!=INF)
        {
        if((l[i]>h2&&j>=l[i]&&r[i]>w2&&k>=r[i])||
           (l[i]>h2&&j>=l[i]&&r[i]<w1&&k<=r[i])||
           (l[i]<h1&&j<=l[i]&&r[i]>w2&&k>=r[i])||
           (l[i]<h1&&j<=l[i]&&r[i]<w1&&k<=r[i])
           )return 1;
        }
        else if(l[i]==j&&r[i]==k)return 1;
    }
    return 0;
}
bool In(long j,long k)
{
    long i;
    for(i=0;i<lt;i++)if(j==l[i]&&k==r[i])return 1;
    return 0;
}
void Solve()
{
    long i,j,k;
    //printf("%ld %ld , %ld %ld\n",h1,h2,w1,w2);
    //printf("%ld %ld , %ld %ld\n",th1,th2,tw1,tw2);
    for(i=0;i<m;i++)
    {
        scanf("%ld%ld",&j,&k);
      //  printf("%ld %ld\n",j,k);
      //  if(!(isB(j,k)^notB(j,k)))
      //      printf("UNKNOWN\n");

         if(isB(j,k))printf("BIRD\n");
         else if(Nt(j,k)||notB(j,k))
            printf("NOT BIRD\n");
         else printf("UNKNOWN\n");
    }
}

int main()
{
    freopen("i1.txt","r",stdin);
   //

freopen("o1.txt","w",stdout);
    long T,K=1;scanf("%ld",&T);
    while(T--)
    {
        Init();
        printf("Case #%ld:\n",K++);
        Solve();
    }
    return 0;
}
