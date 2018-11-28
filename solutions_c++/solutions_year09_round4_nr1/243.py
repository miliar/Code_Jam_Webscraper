#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <algorithm>
using namespace std;

char s[60];
int n,a[60];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca,i,j,k,ans;
	scanf("%d",&T);
	for (ca = 1 ; ca <= T ; ca++)
	{
		ans=0;
		scanf("%d",&n);
		memset(a,0,sizeof a);
		for (i = 0 ; i < n ; i++)
		{
			scanf("%s",s);
			for (j = 0 ; s[j] ; j++)if(s[j]=='1')a[i]=j;
		}
		for (i = 0 ; i < n ; i++)
		{
			if(a[i]<=i)continue;
			for (j = i+1 ; j < n ; j++)
			{
				if(a[j]<=i)break;
			}
			for (k = j ; k > i ; k--)swap(a[k],a[k-1]);
			ans+=j-i;
		}
		printf("Case #%d: %d\n",ca,ans);
	}

	return 0;
}
