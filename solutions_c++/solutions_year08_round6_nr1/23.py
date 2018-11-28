#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstdio>

#define INF 1000000000

using namespace std;

typedef pair<int, int> D;

D w[1000], h[1000];

bool is_in(int min_w, int max_w, int min_h, int max_h, int w, int h)
{
	return min_w <= w && w <= max_w && min_h <= h && max_h >= h;
}

int main()
{
	int N;
	cin >> N;
	for(int t = 1; t <= N; ++t)
	{
		int n, min_w = INF, max_w = 0, min_h = INF, max_h = 0;
		cin >> n;
		for(int i = 0; i < n; ++i)
		{
			string type;
			cin >> h[i].first >> w[i].first >> type;
			h[i].second = w[i].second = 0;
			if(type == "BIRD") h[i].second = w[i].second = 1;
			else cin >> type;
		}
		for(int i = 0; i < n; ++i) if(h[i].second)
		{
			min_w = min(min_w, w[i].first);
			max_w = max(max_w, w[i].first);
			min_h = min(min_h, h[i].first);
			max_h = max(max_h, h[i].first);
		}
		int m;
		cin >> m;
		printf("Case #%d:\n", t);
		for(int i = 0; i < m; ++i)
		{
			int ih, iw;
			cin >> ih >> iw;
			if(min_w <= iw && iw <= max_w && min_h <= ih && ih <= max_h) printf("BIRD\n");
			else
			{
				bool unknown = true;
				int r_min_w = min(iw, min_w), r_max_w = max(iw, max_w), r_min_h = min(ih, min_h), r_max_h = max(ih, max_h);
				//cout << r_min_w << " " << r_max_w << " " << r_min_h << " " << r_max_h << endl;
				for(int j = 0; j < n && unknown; ++j) if(h[j].second == 0)
				{
					unknown = !is_in(r_min_w, r_max_w, r_min_h, r_max_h, w[j].first, h[j].first);
					//cout << unknown << endl;
				}
				if(unknown) printf("UNKNOWN\n");
				else printf("NOT BIRD\n");
			}
		}
	}
	return 0;
}
