#include <stdio.h>
#include <string.h>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>
#include <stack>
#include <queue>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);

	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);

	int T,n;


	int i, j, t;

	int a[1005], b[1005];
	
	scanf("%d",&T);

	for(t = 1; t <= T; t++)
	{
		scanf("%d",&n);
		for(i = 0; i < n; i++)
			scanf("%d%d",&a[i],&b[i]);
		
		int res = 0;

		for(i = 0; i < n; i++)
		{
			for(j = i+1; j <= n; j++)
			{
				if((a[i] < a[j] && b[i] > b[j]) || (a[i] > a[j] && b[i] < b[j]))
					res++;
			}
		}

		printf("Case #%d: %d\n",t,res);
	}

	return 0;
}