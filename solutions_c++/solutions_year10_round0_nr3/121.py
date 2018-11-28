#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int R, k, N;

vector< long long > sums;
vector<int> nextpos;

long long go( int st, int steps )
{
	long long res = 0;
	while( steps-- )
	{
		res += sums[st];
		st = nextpos[st];
	}
	return res;
}

int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";

		cin >> R >> k >> N;
		vector<int> v(N);

		long long total = 0;
		for(int i = 0; i < N; i++)
		{
			cin >> v[i];
			total += v[i];
		}

		if( total <= k )
		{
			cout << total * R << endl;
			continue;
		}

		int en = 0;
		long long sum = v[0];
		nextpos.resize(N);
		sums.resize(N);
		for(int i = 0; i < N; i++)
		{
			while( sum <= k )
			{
				en = (en + 1)%N;
				sum += v[en];
			}
			nextpos[i] = en;
			sums[i] = sum - v[en];
			sum -= v[i];
		}

		vector<bool> u(N,0);
		int loopHeadCount = 0;
		long long loopHeadSum = 0;
	
		int cur = 0;
		while( !u[cur] )
		{
			loopHeadCount++;
			loopHeadSum += sums[cur];

			u[cur] = 1;
			cur = nextpos[cur];
		}

		int loopCycleCount = 1;
		long long loopCycleSum = sums[cur];

		int loopStart = cur;
		cur = nextpos[loopStart];
		while( cur != loopStart )
		{
			loopCycleCount++;
			loopCycleSum += sums[cur];

			cur = nextpos[cur];
		}

		loopHeadCount -= loopCycleCount;
		loopHeadSum -= loopCycleSum;

		long long res;
		if( loopHeadCount <= R )
			res = go( 0, R );
		else
		{
			res = loopHeadSum;
			R -= loopHeadCount;
			
			res += (R / loopCycleCount) * loopCycleSum;
			res += go( loopStart, R % loopCycleCount );
		}

		cout << res << endl;
	}
}