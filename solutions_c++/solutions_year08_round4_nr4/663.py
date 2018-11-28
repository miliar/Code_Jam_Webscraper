#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>
#include <functional>

using namespace std;

int a[20],i,j,k,n,cas,ans,x,p;
char s[1030],t[1030];
int main()
{
	scanf("%d",&n);
	for (cas=1;cas<=n ;cas++ )
	{
		scanf("%d",&k);
		for (i=0;i<k ;i++ ) a[i]=i+1;
		memset(s,0,sizeof(s));
		scanf("%s",s);
		ans = 1000000;
		do
		{
			memset(t,0,sizeof(t));
			for (i=0;s[i] ;i+=k )
				for (j=i;j<i+k ;j++ )
				{
					x = i + a[j-i] - 1;
					t[j] = s[x];
				}
			p = 0;
			for (i=1;t[i] ;i++ )
				if (t[i]!=t[i-1]) p++;
			if (p<ans) ans=p;
		}while (next_permutation(a,a+k));

		printf("Case #%d: %d\n",cas,ans+1);
	}
	return 0;
}
