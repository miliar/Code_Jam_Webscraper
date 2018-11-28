#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <set>
#include <map>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;

typedef vector<int>		VI;
typedef vector<VI>		VVI;
typedef vector<string>	VS;
typedef pair<int,int>	PII;
typedef vector<PII>		VPII;

VVI adj;
int dist[64][64];

int track(int pos, const VI &threat)
{
	int res = 0;
	if (pos == 0)
	{
		for (int i = 0; i < threat.size(); i++)
			if (threat[i])
				res++;
		return res;
	}
	for (int i = 0; i < adj[pos].size(); i++)
		if (dist[pos][0] == dist[adj[pos][i]][0] + 1)
		{
			const int npos = adj[pos][i];
			VI nthreat = threat;
			nthreat[npos] = 1;
			for (int j = 0; j < adj[npos].size(); j++)
				nthreat[adj[npos][j]] = 1;
			res = max(res, track(npos, nthreat));
		}
	return res;
}

int main()
{
	int kases;
	cin >> kases;
	for (int kase = 1; kase <= kases; kase++)
	{
		int P, W;
		cin >> P >> W;
		adj.assign(P, VI());
		for (int i = 0; i < P; i++)
			for (int j = 0; j < P; j++)
				if (i == j)
					dist[i][j] = 0;
				else
					dist[i][j] = 1000;
		for (int i = 0; i < W; i++)
		{
			int x, y;
			char dummy;
			cin >> x >> dummy >> y;
			adj[x].push_back(y);
			adj[y].push_back(x);
			dist[x][y] = dist[y][x] = 1;
		}

		for (int k = 0; k < P; k++)
			for (int i = 0; i < P; i++)
				for (int j = 0; j < P; j++)
					dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);

		VI threat(P, 0);
		int best = track(1, threat);
		cout << "Case #" << kase << ": " << (dist[0][1] - 1) << " " << (best - dist[0][1]) << endl;
	}
	return 0;
}
