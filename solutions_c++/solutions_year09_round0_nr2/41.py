#define INPUT "D:\\code\\gcj09\\B-large.in"
#define OUTPUT INPUT ".out.txt"

#include <vector>
#include <cassert>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <iostream>
#include <cstdio>

using namespace std;
int GI() { int t; scanf("%d", &t); return t; }

int		A[101][101];
char	ch[101][101];
int H, W;

int main()
{
	assert (freopen(INPUT, "r", stdin));
	assert (freopen(OUTPUT, "w", stdout));
	for (int T = GI(), k = 1; k  <= T; ++ k)
	{
		cout << "Case #" << k << ": " << endl;
		H = GI(); W = GI();
		vector < pair < int, pair <int,int > > > vp;
		for (int h = 0; h < H; ++ h)
			for (int w = 0; w < W; ++ w)
			{
				A[h][w] = GI();
				vp.push_back( make_pair(A[h][w], make_pair(h, w)));
			}
		sort (vp.begin(), vp.end());
		memset(ch, '0', sizeof(ch));
		char chVal = 'a' - 1;
		for (int i = 0; i < vp.size(); ++ i)
		{
			int h = vp[i].second.first, w = vp[i].second.second;
			int Dirs[4][2] = { {-1, 0}, {0,-1}, {0,+1}, {+1,0} };
			int best = A[h][w];
			char bestC;
			for (int d = 0; d < 4; ++ d)
			{
				int nh = h + Dirs[d][0], nw = w + Dirs[d][1];
				if (nh >= 0 && nw >= 0 && nh < H && nw < W && best > A[nh][nw]) best = A[nh][nw], bestC = ch[nh][nw];
			}
			if (best == A[h][w])
			{
				ch[h][w] = ++ chVal;
			}
			else
			{
				ch[h][w] = bestC;
			}
		}

		map < char, char > trans;
		char avail = 'a';
		for (int h = 0; h < H; ++ h)
		{
			char *prev = "";
			for (int w = 0; w < W; ++ w)
			{
				char c = ch[h][w];
				if (trans.count(c)) c = trans[c];
				else c = trans[c] = avail ++;
				cout << prev << c;
				prev = " ";
			}
			cout << endl;
		}
	}
	return 0;
}