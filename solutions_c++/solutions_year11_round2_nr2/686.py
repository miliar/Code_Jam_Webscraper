#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<list>
#include<cmath>
#include<queue>
#include<set>
#include<stack>
#define FOR(x,y,z) for(int x=y;x<z;x++)
#define FORD(x,y,z) for(int x=y; x>=z;x--)
#define max3(a,b,c) max(a,max(b,c))
#define PB push_back
#define F first
#define ALL(x) x.begin(),x.end()
#define K(x) ((x)*(x))
#define mabs(x) max(x,-x)
#define S second
#define MP make_pair
#define e 0.00000000001
#define inf 2000000000
using namespace std;
int c,d;
vector<pair<int,int> > P;

bool check(double t)
{
 //  printf("\nCHECK: %lf\n",t);
   double last=P[0].F-t;
   FOR(i,0,P.size())
   {
 //     printf("%lf\n",last);
      int k=P[i].S;
      last=max(P[i].F-t,last);
      FOR(j,0,k)last+=d;//printf("{%d %lf}",k,last);}
      if(last>P[i].F+t+d)return false;
   }
   return true;
}

int main()
{
   int Z;
   scanf("%d",&Z);
   for(int z=1;z<=Z;z++)
   {
      int a,b;
      scanf("%d %d",&c,&d);
      FOR(i,0,c){scanf("%d %d",&a,&b);P.PB(MP(a,b));}
      sort(ALL(P));
      double p=0,q=10000000000000.0;
      while(q-p>0.0000001)
      {
         double s=(p+q)/2;
         if(check(s))q=s;
         else p=s;
      }
      printf("Case #%d: %lf\n",z,(p+q)/2);
      P.clear();
   }
 //  system("pause");
   return 0;
}
