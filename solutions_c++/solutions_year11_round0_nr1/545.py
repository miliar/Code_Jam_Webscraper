#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<list>
#include<cmath>
#include<queue>
#include<stack>
#define FOR(x,y,z) for(int x=y;x<z;x++)
#define FORD(x,y,z) for(int x=y; x>=z;x--)
#define max3(a,b,c) max(a,max(b,c))
#define PB push_back
#define F first
#define K(x) ((x)*(x))
#define mabs(x) max(x,-x)
#define S second
#define MP make_pair
#define inf 2000000000
using namespace std;

int res=0,posb,poso;
list<pair<int,int> > B,O;
int main()
{
   int Z;
   scanf("%d",&Z);
   FOR(z,1,Z+1)
   {
      res=0;
      posb=poso=1;
      int kol=1;
      int a,n;
      char c;
      scanf("%d",&n);
      FOR(i,1,n+1){scanf(" %c %d",&c,&a);if(c=='B')B.push_back(MP(i,a));else O.push_back(MP(i,a));}
      O.push_back(MP(inf,inf));
      B.push_back(MP(inf,inf));
      for(res=0;kol<=n;res++)
      {
         if(posb==B.front().S && kol==B.front().F)
         {
            kol++;
            B.pop_front();
            if(poso<O.front().S && O.front().S!=inf)poso++;
            else if(poso>O.front().S && O.front().S!=inf)poso--;
            continue;
         }
         else if(poso==O.front().S && kol==O.front().F)
         {
            kol++;
            O.pop_front();
            if(posb<B.front().S && B.front().S!=inf)posb++;
            else if(posb>B.front().S && B.front().S!=inf)posb--;
            continue;
         }
         if(B.front().S!=inf)
         {
            if(posb<B.front().S)posb++;
            else if(posb>B.front().S)posb--;
         }
         if(O.front().S!=inf)
         {
            if(poso<O.front().S)poso++;
            else if(poso>O.front().S)poso--;
         }
      }
      O.clear();
      B.clear();
      printf("Case #%d: %d\n",z,res);
   }
 //  system("pause");
   return 0;
}
