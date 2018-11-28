// Google Code Jam 2011 - Round 2
// by vdave, Hungary, 2011

#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;



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

















void solve_B(int argc, char *argv[])
{
	int TC;
	scanf("%d", &TC);

	for (int tc = 1; tc <= TC; ++tc)
	{

	}

	fflush(stdout);
}
void solve_C(int argc, char *argv[])
{
	int TC;
	scanf("%d", &TC);

	for (int tc = 1; tc <= TC; ++tc)
	{

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
	solve_A(argc, argv);
	//solve_B(argc, argv);
	//solve_C(argc, argv);
	//solve_D(argc, argv);

	return 0;
}