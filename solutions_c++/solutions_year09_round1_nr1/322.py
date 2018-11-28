
#include<iostream>
#include<sstream>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<queue>
#include<cstdio>

#define F(i,n) for( int i = 0; i < (int)n;i++)
#define FE(i,v) for( typeof((v).begin()) i = (v).begin(); i!= (v).end();i++)
#define ms(a,k) memset(a,k,sizeof(a))
using namespace std;

int m, n, deci, x, b, nb;
char  dp[100000000][10];
int f()
{
//   printf("f(%d)\n",deci);
   if(deci == 1) return 1;
   char  &ret = dp[deci][b];
   if(ret >= 0 ) return ret;
   ret = 0;
   int sum = 0, d;
   while(deci>0)
   {
      d = deci%b;
      sum = sum  + d*d;
      deci /= b;      
   }
   /*
   deci = 0;
   while(sum>0)
   {
      d = sum %10;
      deci = deci*10 + d;
      sum /= 10;
   }
   */
   deci = sum;

   return ret = f();

}
int main()
{
   ms(dp,-1);
   int k, t, tests;
   scanf("%d\n",&tests);
   F(itest,tests)
   {
      string s;
      getline(cin,s);
      stringstream sin(s);
      vector<int> v;
      typeof(v.begin()) it ;

      while(sin>>k) v.push_back(k);
      int sum ,d , x;
      for( t = 2; t < 100000000 ; t++)
      {
	 deci = t;
	    for( it = (v).begin(); it!= (v).end();it++)
	    {
	       b = *it;
	       deci = t;
//	       printf("Checking %d %d\n",deci,b);
	       if(f() != 1) break; 
	    }
	 if( it == v.end())
	    break;
      }
      printf("Case #%d: %d\n",1+itest,t);

   }
   return 0;
}
