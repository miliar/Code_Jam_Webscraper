#include<cstdio>
using namespace std;

int T,N,S,P;

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int i,t,k,ans;
	scanf("%d",&T);
	for (t=1;t<=T;t++)
	{
		ans = 0;
		scanf("%d%d%d",&N,&S,&P);
		for (i=0;i<N;i++)
		{
			scanf("%d",&k);
			if (k % 3 == 0)
			{
				if (k / 3 >= P)
					ans ++ ;
				else if (S && k/3 +1 >= P && k/3 - 1 >= 0)
				{
					S --;
					ans ++;
				}
			}
			else if (k % 3 == 1)
			{
				if (k / 3 +1 >= P)
					ans++;
			}
			else if (k % 3 == 2)
			{
				if (k / 3 +1 >= P)
					ans ++;
				else if (S && k/3 + 2 >= P)
				{
					S --;
					ans ++;
				}
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
