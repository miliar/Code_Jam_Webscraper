#include <cstdio>

#define FOR(I, N) for(int I = 0, end_ = (N); I < end_; ++I)
int ri() { int r; scanf("%d", &r); return r; }

int main()
{
	FOR(i, ri())
	{
		int N = ri(), S = ri(), p = ri(), answer = 0;

		FOR(j, N)
		{
			int s = ri();
			if (p == 0)
				++answer;
			else if (p == 1 && s > 0)
				++answer;
			else if (p > 1 && (s > (3*p - 3) || (s > (3*p - 5) && S-- > 0)))
				++answer;
		}

		printf("Case #%d: %d\n", i + 1, answer);
	}
}