#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int T;

struct chicken
{
	int order;
	int began;
	int vel;
	double time;
};

bool swp(chicken a, chicken b)
{
	if (((a.time <= T) && (b.time <= T)) || (a.time == b.time))
	{
		return a.order > b.order;
	}
	return a.time < b.time;
}

int main()
{
	freopen("B.in", "rt", stdin);
	freopen("B.out", "wt", stdout);	
	int C;
	cin >> C;
	for (int i = 0; i < C; ++i)
	{
		int N, K, B;
		cin >> N >> K >> B >> T;
		vector <chicken> chicks(N);
		for (int j = 0; j < N; ++j)
		{
			chicks[j].order = j;
			cin >> chicks[j].began;
		}
		for (int j = 0; j < N; ++j)
		{
			cin >> chicks[j].vel;
			chicks[j].time = ((double) B - chicks[j].began) / ((double) chicks[j].vel);
		}
		sort(chicks.begin(), chicks.end(), swp);
		cout << "Case #" << i + 1 << ": ";
		if (chicks[K - 1].time > T)
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			int peres = 0;
			vector <bool> is(N, false);
			for (int j = 0; j < K; ++j)
			{
				is[chicks[j].order] = true;
			}
			int s = 0;
			for (int j = 0; j < N; ++j)
			{
				if (is[j])
				{
					peres += (N - j - 1) - s;
					++s;
				}
			}
			cout << peres << endl;
		}
	}
	return 0;
}
