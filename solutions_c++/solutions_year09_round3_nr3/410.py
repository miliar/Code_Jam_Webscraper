#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <algorithm>
#include <set>
#include <cmath>
using namespace std;


int p[6],n,mx,a[102];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca,i,j,ans,t;
	scanf("%d",&T);
	for (ca = 1 ; ca <= T ; ca++)
	{
		scanf("%d%d",&mx,&n);
		for (i = 0 ; i < n ; i++)
		{
			scanf("%d",&p[i]);
		}
		ans = 1<<30;
		do
		{
			for (i = 1 ; i <= mx ; i++)a[i]=i;
			a[0]=a[mx+1] = t= 0;
			for (i = 0 ; i < n ; i++)
			{
				for (j = p[i]-1 ; a[j] ; j--)t++;
				for (j = p[i]+1 ; a[j] ; j++)t++;
				a[p[i]] = 0;
			}
			if(ans > t) ans = t;
		}while(next_permutation(p,p+n));

		printf("Case #%d: %d\n",ca,ans);
	}

	return 0;
}
