// Google Code Jam 2011 - Round 2
// by vdave, Hungary, 2011

#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;



/*

class SpeedCompare
{
public:
	bool operator()(const pair<pair<int, int>, int>& first, const pair<pair<int, int>, int>& second)
	{
		return first.second < second.second;
	}
};

pair<pair<int, int>, int> walkWays[2048];
double runTime[2048];
double walkTime[2048];

void solve_A(int argc, char *argv[])
{
	int TC;
	scanf("%d", &TC);

	for (int tc = 1; tc <= TC; ++tc)
	{
		int X, S, R, t, N, N2;
		scanf("%d %d %d %d %d", &X, &S, &R, &t, &N);

		for (int i = 0; i < N; ++i)
		{
			scanf("%d %d %d", &walkWays[i].first.first, &walkWays[i].first.second, &walkWays[i].second);
		}
		sort(walkWays, walkWays + N);

		// Make inter-walkway parts as 0 speed walkway
		N2 = N;
		if (walkWays[0].first.first != 0)
			walkWays[N2++] = make_pair(make_pair(0, walkWays[0].first.first), 0);
		for (int i = 1; i < N; ++i)
		{
			if (walkWays[i].first.first != walkWays[i - 1].first.second)
				walkWays[N2++] = make_pair(make_pair(walkWays[i - 1].first.second, walkWays[i].first.first), 0);
		}
		if (walkWays[N - 1].first.second < X)
		{
			walkWays[N2++] = make_pair(make_pair(walkWays[N - 1].first.second, X), 0);
		}
		sort(walkWays, walkWays + N2, SpeedCompare());

		double runTimeLeft = t;
		double totalTime = 0.0;

		for (int i = 0; i < N2; ++i)
		{
			if (walkWays[i].first.first >= X)
				continue;

			double diff = walkWays[i].first.second - walkWays[i].first.first;
			if (walkWays[i].first.second > X)
			{
				diff = X - walkWays[i].first.first;
			}

			double timeWalk = diff / (double) (S + walkWays[i].second);
			double timeRun = diff / (double) (R + walkWays[i].second);
			if (timeRun > runTimeLeft)
			{
				timeRun = runTimeLeft;
				diff -= timeRun * (R + walkWays[i].second);
				timeWalk = diff / (double) (S + walkWays[i].second);
			}
			else
			{
				timeWalk = 0.0;
			}

			totalTime += timeRun + timeWalk;
			runTimeLeft -= timeRun;
		}

		printf("Case #%d: %.9lf\n", tc, totalTime);
	}

	fflush(stdout);
}

*/



char sDelta[1024];
int deltaMass[512][512];

void solve_B(int argc, char *argv[])
{
	int TC;
	scanf("%d", &TC);

	for (int tc = 1; tc <= TC; ++tc)
	{
		int R, C, D;
		scanf("%d %d %d", &R, &C, &D);
		for (int i = 0; i < R; ++i)
		{
			scanf("%s", sDelta);
			for (int j = 0; j < C; ++j)
			{
				deltaMass[i][j] = sDelta[j] - '0';
			}
		}

		int largestK = std::min(R, C);
		int maxK = -1;
		for (int v = 0; v <= R - 3; ++v)
		{
			for (int u = 0; u <= C - 3; ++u)
			{
				for (int k = 3; k <= std::min(R - v, C - u); ++k)
				{
					int massX = 0, massY = 0;
					for (int i = 0; i < k; ++i)
					{
						for (int j = 0; j < k; ++j)
						{
							if ((i == 0 || i == (k - 1)) && (j == 0 || j == (k-1)))
								continue;

							massY += (2 * i + 1 - k) * deltaMass[v + i][u + j];
							massX += (2 * j + 1 - k) * deltaMass[v + i][u + j];
						}
					}

					if (massX == 0 && massY == 0)
					{
						if (k > maxK)
							maxK = k;
					}
				}
			}
		}

		if (maxK == -1)
		{
			printf("Case #%d: IMPOSSIBLE\n", tc);
		}
		else
		{
			printf("Case #%d: %d\n", tc, maxK);
		}
	}

	fflush(stdout);
}
















int primeCnt;
int primes[1000000];

void solve_C(int argc, char *argv[])
{
	int TC;
	scanf("%d", &TC);

	primeCnt = 1;
	primes[0] = 2;
	for (int p = 3; p < 2000000; p += 2)
	{
		bool isPrime = true;
		for (int i = 0; i < primeCnt; ++i)
		{
			if ((p % primes[i]) == 0)
			{
				isPrime = false;
				break;
			}
			if (primes[i] * primes[i] > p)
				break;
		}

		if (isPrime)
			primes[primeCnt++] = p;
	}

	for (int tc = 1; tc <= TC; ++tc)
	{
		long long N;
		scanf("%lld", &N);

		int totalDiff = 1;
		if (N == 1)
			totalDiff = 0;
		for (int i = 0; i < primeCnt; ++i)
		{
			long long pp = primes[i];
			int maxPow = 0;
			while (pp <= N)
			{
				maxPow++;
				pp *= (long long) primes[i];
			}

			if (maxPow > 0)
			{
				totalDiff += maxPow - 1;
			}
		}

		printf("Case #%d: %d\n", tc, totalDiff);
	}

	fflush(stdout);
}











void solve_D(int argc, char *argv[])
{
	int TC;
	scanf("%d", &TC);

	for (int tc = 1; tc <= TC; ++tc)
	{

	}

	fflush(stdout);
}




int main(int argc, char *argv[])
{
	//solve_A(argc, argv);
	//solve_B(argc, argv);
	solve_C(argc, argv);
	//solve_D(argc, argv);

	return 0;
}