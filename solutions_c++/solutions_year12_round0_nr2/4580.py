
/* -------- Author: Harshit Agrawal --------- */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string.h>
#include <limits.h>

using namespace std;

#define MAXN 100
#define x first
#define y second

typedef pair<int,int> ii;
typedef long long int ll;
int myGCD( int a, int b)
{
   if(b==0) return a;
   else 
      return myGCD(b,a%b);
}

int myPOW(int a, int b)
{
   int val;
   if( b==0 ) return 1;
   if( b==1 ) return a;
   val = myPOW(a,b/2);
   val = val*val;
   return (b%2)?val*a:val;
}

int main() {
   int T;
   scanf("%d",&T);
   int i,j,k,l, n, sur, p;
   int ans=0;
   i=1;
   while(i<=T)
   {
      vector<int> gog;
      ans=0;
      scanf("%d",&n);
      scanf("%d",&sur);
      scanf("%d",&p);
      for(j=0;j<n;j++)
      {
	 scanf("%d",&k);
	 gog.push_back(k);
      }
      sort(gog.begin(), gog.end());
      for(j=n-1;j>=0;j--)
      {
	 if( gog[j]%3 == 0 )
	 {
	    if( gog[j]/3 >= p ) ans++;
	    else if( gog[j]/3 > 0 && gog[j]/3+1>=p && sur >0 ) { ans ++; sur--; }
	 }
	 else if( gog[j]%3 == 1 )
	 {
	    if( gog[j]/3 >= p || gog[j]/3+1>=p ) ans++;
	 }
	 else
	 {
	    if( gog[j]/3 >= p || gog[j]/3+1 >= p ) ans++;
	    else if( gog[j]/3+2 >= p && sur > 0 ) { ans++; sur--;}
	 }
      }
      printf("Case #%d: %d\n",i,ans);
      i++;
   }

   return 0;
}

