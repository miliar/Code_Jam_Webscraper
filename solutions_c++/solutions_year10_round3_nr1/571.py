#include<stdio.h>
#include<string.h>

int A[1005], B[1005];

bool intersects(int i, int j)
{
	int a = A[i], b = B[i], c = A[j], d = B[j];

	return (a < c) != (b < d);
}

int main()
{
	freopen("ALarge.in","r",stdin);
	freopen("ALarge.out","w",stdout);

	int T; scanf("%d",&T);

	for(int t = 1; t <= T; ++t)
	{
		int N; scanf("%d",&N);

		int i;

		for(i = 0; i < N; ++i)
		{
			scanf("%d%d",A+i,B+i);
		}

		// calc ans
		int ans = 0;

		int j;

		for(i = 0; i < N; ++i)
		{
			for(j = i+1; j < N; ++j)
			{
				if(intersects(i,j))
					++ans;
			}
		}

		printf("Case #%d: %d\n",t,ans);

	}

	return 0;
}
