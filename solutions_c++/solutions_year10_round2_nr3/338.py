
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<queue>
#include<cstdio>

using namespace std;
int m, n;
int a[100];
int main()
{
   int k, t, tests;
   int g;
   scanf("%d", &tests); 
   map<int,int> an;
   for (int g = 0; g < tests; g++) {
      scanf("%d", &n); 
      if( an[n] ) {
      printf("Case #%d: %d\n",g+1,an[n]);
      }
      else {
      int i,j;
      int ans=0;
      for(i = 0; i < (1<<(n-1)); i++) {
	  k = 1;
	  for(j = 2; j <= n; j++) if( i & ( 1<<(j-2))) a[j] = k++;
	  else a[j] = -1;
	  //a[k++] = j;
	  for(j = n; j != 1; j = a[j]) 
	      if( (i&(1<<(j-2)))==0) break;
	  if( j == 1 ) ans ++;
	  if( ans == 100003 ) ans = 0;
      }
      an[n] = ans;
      printf("Case #%d: %d\n",g+1,ans);
      }
      
   }
   
   return 0;
}
