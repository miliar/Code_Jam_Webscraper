#include<cstdio>

using namespace std;

long long mas[10000];

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	long long T;
	scanf("%lld", &T);
	long long i, j, k, l;
	for(i = 0; i<T; i++)
	{
		long long N, H, L;
		scanf("%lld%lld%lld", &N, &L, &H);
		for(k = 0; k<N; k++)
		{
			scanf("%lld", &mas[k]);
		}
		long long res = 0;
		printf("Case #%d: ", i+1);
		for(l = L; l<=H; l++)
		{
			for(k = 0; k<N; k++)
			{
				if(l%mas[k] != 0 && mas[k]%l != 0)
					break;
			}
			if(k == N)
			{
				res = l;
				break;
			}
		}
		if(res == 0)
			printf("NO\n");
		else
			printf("%lld\n", res);
	}
	return 0;
}
