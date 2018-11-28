#include <iostream>
#include <string.h>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <ctime>
#include <queue>
#include <map>
#define pb push_back
#define MAXN 1
#define MAXM 1
#define INF (1<<30)
#define PI 3.1415926535898
#define esp 10e-6
const int dx[4]={1,0,-1,0};
const int dy[4]={0,-1,0,1};
using namespace std;

class Point
{
      public:
             int x;
             int y;
};

int wei(int k)
{
    int t=0;
    while (k)
          {
          t++;
          k/=10;
          }
    return t;
}

int list[10]={1,10,100,1000,10000};
int check(int x,int y)
{
    if (wei(x)!=wei(y)) return 0;
    int l=wei(x);
    //int p=y;
    for (int i=1;i<l;++i)
        {
        y=(y/10)+(y%10*list[l-1]);
        //cout<<x<<" "<<y<<endl;
        if (x==y) return 1;
        }
    return 0;        
}

int work()
{
    int ans=0;
    int a,b;
    scanf("%d%d",&a,&b);
    if (a>b)
       swap(a,b);
    for (int i=a;i<=b;++i)
        for (int j=i+1;j<=b;++j)
               if (check(i,j))
                  {
                  //printf("%d %d\n",i,j);
                  ans++;
                  }
    //printf("%d",check(12,21));
    printf("%d\n",ans);
    return 0;
}

int main()
{
    freopen("C-small-attempt11.in","r",stdin);freopen("output.txt","w",stdout);
    int T=0;
    //printf("****%d****\n",check(505,550));
    scanf("%d",&T);
     for (int i=1;i<=T;++i)
        {
        printf("Case #%d: ",i);
        work();
        }
    return 0;
}
