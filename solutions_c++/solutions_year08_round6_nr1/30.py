#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <sstream>

using namespace std;

#define all(x) (x).begin(),(x).end()

struct notbird_box
{
	int sx, sy, ex, ey;

	notbird_box(int a, int b, int c, int d)
	{
		sx = a, sy = b, ex = c, ey = d;
	}
};

int main()
{
	int T;
	cin >> T;
	int N, M;

	for (int cn = 1; cn <= T; ++cn)
	{
		printf("Case #%d:\n", cn);

		cin >> N;
		vector <int> h(N), w(N);
		vector <string> s(N);
		int sx = -1, sy, ex, ey;
		string tmp;

		for (int i = 0; i < N; ++i)
		{
			cin >> h[i] >> w[i] >> s[i];
			if (s[i] == "NOT") cin >> tmp;

			if (s[i] == "BIRD")
			{
				if (sx == -1)
				{
					sx = h[i], ex = h[i];
					sy = w[i], ey = w[i];
				}
				else
				{
					sx <?= h[i]; ex >?= h[i];
					sy <?= w[i]; ey >?= w[i];
				}
			}
		}

		vector <notbird_box> NB;

		for (int i = 0; i < N; ++i)
		{
			if (s[i] == "BIRD") continue;
			int H = h[i], W = w[i];

			int px = 0, py = 0;
			if (H < sx) px = -1;
			if (H > ex) px = 1;
			if (W < sy) py = -1;
			if (W > ey) py = 1;

			if (px == -1 && py == -1) NB.push_back(notbird_box(0, 0, H, W));
			if (px == -1 && py == 0) NB.push_back(notbird_box(0, 0, H, 1000001));
			if (px == -1 && py == 1) NB.push_back(notbird_box(0, W, H, 1000001));
			if (px == 0 && py == -1) NB.push_back(notbird_box(0, 0, 1000001, W));
			if (px == 0 && py == 1) NB.push_back(notbird_box(0, W, 1000001, 1000001));
			if (px == 1 && py == -1) NB.push_back(notbird_box(H, 0, 1000001, W));
			if (px == 1 && py == 0) NB.push_back(notbird_box(H, 0, 1000001, 1000001));
			if (px == 1 && py == -1) NB.push_back(notbird_box(H, W, 1000001, 1000001));

//			cout << NB[NB.size() - 1].sx << ',' << NB[NB.size() - 1].sy << ',' << NB[NB.size() - 1].ex << ',' << NB[NB.size() - 1].ey << endl;
		}

		cin >> M;


		for (int i = 0; i < M; ++i)
		{
			int H, W;
			cin >> H >> W;
			string ret = "UNKNOWN";
			if (sx <= H && H <= ex && sy <= W && W <= ey) ret = "BIRD";
			for (int j = 0; j < N; ++j)
			{
				if (s[j] == "NOT" && H == h[i] && W == w[i])
					ret = "NOT BIRD";
			}

			if (sx != -1)
			{
				for (int j = 0; j < NB.size(); ++j)
				{
					if (NB[j].sx <= H && H <= NB[j].ex &&
						NB[j].sy <= W && W <= NB[j].ey) ret = "NOT BIRD";
				}
				// check UNKNOWN to NOT BIRD.
			}
			cout << ret << endl;
		}
	}
}

