#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <list>
#include <string>

using namespace std;

#define nul(a) memset(a,0,sizeof(a))
#define sqr(a) ((a)*(a))
#define eps 1e-10
#define inf 1000000000

int main()
{
#ifndef ONLINE_JUDGE
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
#endif
   int i,n,k,t,s;
   scanf("%d",&t);
   for (i=0;i<t;i++){
	   scanf("%d%d",&n,&k);
	   s = 1<<n;
	   if (i > 0) 
		 printf("\nCase #%d: ",i+1);
	   else
		 printf("Case #%d: ",i+1);		 		 
	   if (k%s==s-1)
		 printf("%s ","ON");
	   else
		 printf("%s ","OFF");
   }
 
   return 0;
}