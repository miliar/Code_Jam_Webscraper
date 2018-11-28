using namespace std;
#include<cstdio>
const int MAX_N = 10007;
int A[MAX_N];

int main()
{
	int N, T;
	long long X, Y, i, rez;
	int j, ok;
	freopen("file.in","r",stdin); freopen("file.out","w",stdout);
	scanf("%d",&T);
	for(int k = 1; k<= T; ++k )
	{
		scanf("%d %lld %lld", &N, &X, &Y);
		for( j = 1; j<=N; ++j)
			scanf("%d", &A[j]);
		for(rez = 0, i = X; i <= Y && !rez; ++i )
		{
			for(ok = 1, j = 1; j <= N; ++j)
			{
				if( i % A[j] == 0 || A[j] % i == 0 ) continue;
				ok = 0;
			}
			if(ok) rez = i;
		}
		if(rez) printf("Case #%d: %lld\n", k, rez);
		else printf("Case #%d: NO\n", k);
	}
	return 0;
}