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

int main()
{
   int Z;
   scanf("%d",&Z);
   for(int z=1;z<=Z;z++)
   {
      int n,a;
      int licznik=0;
      scanf("%d",&n);
      FOR(i,1,n+1){scanf("%d",&a);if(a!=i)licznik++;}
      printf("Case #%d: %lf\n",z,double(licznik));
   }
   return 0;
}
