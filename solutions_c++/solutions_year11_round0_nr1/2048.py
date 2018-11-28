#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <list>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>

#include "windows.h"
using namespace std; 
char s[1000];int a[1000];int next[1000];
int dp[1000];
int main()   
{   
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,n,i,j;
	scanf("%d",&t);
	for(int test=1;test<=t;test++){
	    scanf("%d",&n);
		int lo=0,lb=0;
		a[0]=1;dp[0]=0;
		for(i=1;i<=n;i++){
		    scanf(" %c%d",&s[i],&a[i]);
			//printf("%c %d\n",s[i],a[i]);
			if(s[i]=='O'){
			    next[i]=lo;
				lo=i;
			}
			else if(s[i]=='B'){
			    next[i]=lb;
				lb=i;
			}
		}
		for(i=1;i<=n;i++){
			    dp[i]=max(abs(a[i]-a[next[i]])+1+dp[next[i]],dp[i-1]+1);
				//printf("%d %d %d %d\n",i,dp[i],abs(a[i]-a[next[i]])+1+dp[next[i]],dp[i-1]+1);
				//printf("%d %d %d %d\n",a[i],next[i],dp[next[i]],dp[i-1]+1);
		}
		printf("Case #%d: %d\n",test,dp[n]);

	}
	
}   
