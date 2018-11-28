#include <cstdio>
#include <vector>

using namespace std;

int abs(int x) { return (x<0)? -x : x; }
int gcd(int a, int b)
{
	return b ? gcd(b, a%b) : a;
}

int main()
{
	int C;
	scanf("%d", &C);

	for (int tp = 1; tp <= C; ++tp)
	{
		int N;
		scanf("%d", &N);
		vector <int> V(N);
		for (int i = 0; i < N; ++i)
		{
			scanf("%d", &V[i]);
		}

		int T = abs(V[1] - V[0]);

		for (int i = 0; i < N; ++i)
		{
			for (int j = i+1; j < N; ++j)
			{
				T = gcd(T, abs(V[i]-V[j]));
			}
		}

		printf("Case #%d: %d\n", tp, (T-(V[0]%T))%T);
	}

	return 0;
}
