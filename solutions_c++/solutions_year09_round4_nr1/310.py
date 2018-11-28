// GCJ Round X - Problem A
// -- strapahuulius

// pre-written code follows
// #includes {{{
#include <algorithm>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;
// }}}
// constants, typedefs, macros {{{
typedef long long LL;
typedef unsigned long long ULL;
const int oo = 1000000000;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<string> VS;
typedef queue<int> QI;
typedef queue<PII> QPII;
typedef complex<double> tComp;
const double PI = 2.0 * acos(0.0);
const double EPS = 1e-9;
#define FORIT(i,c) for (typeof((c).end()) i=(c).begin(); i!=(c).end(); ++i)
#define CERR(x) cerr << (#x) << " = " << (x) << endl
#define COUT(x) cout << (#x) << " = " << (x) << endl
// }}}


typedef long long LL;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;
void add(int x, int prevx, VI &S, VI &prev, VLL &labelx, VLL &labely, VVLL &weight, VLL &slack, VI &slackx)
{
	S[x] = 1;
	prev[x] = prevx;
	for (int y=0; y<(int)weight.size(); y++)
		if (labelx[x] + labely[y] - weight[x][y] < slack[y])
		{
			slack[y] = labelx[x] + labely[y] - weight[x][y];
			slackx[y] = x;
		}
}
const long long OO = 1000000000000000LL;
LL mw_perfect_matching(VVLL weight, VI &matching) // assert weight[i][j] >= 0
{
	int n = weight.size();
	int match_cnt = 0;
	VLL labelx(n), labely(n);
	matching.assign(n, -1);
	VI matched(n, -1);
	for (int x=0; x<n; x++)
		labelx[x] = *max_element(weight[x].begin(), weight[x].end());
	LL ret = 0;
	while (match_cnt < n)
	{
		queue<int> q;
		VI S(n), T(n), prev(n, -1);
		int xx = find(matching.begin(), matching.end(), -1) - matching.begin();
		int root = xx;
		prev[xx] = -2;
		S[xx] = 1;
		q.push(xx);
		VI slackx(n, root);
		VLL slack(n);
		for (int y=0; y<n; y++)
			slack[y] = labelx[root] + labely[y] - weight[root][y];
		int yy = -1;
		while (1)
		{
			while (!q.empty() && yy == -1)
			{
				xx = q.front();
				q.pop();
				for (int y=0; y<n; y++)
					if (!T[y] && weight[xx][y] == labelx[xx] + labely[y])
					{
						if (matched[y] == -1)
						{
							yy = y;
							break;
						}
						T[y] = 1;
						q.push(matched[y]);
						add(matched[y], xx, S, prev, labelx, labely, weight, slack, slackx);
					}
			}
			if (yy != -1)
				break;
			while (!q.empty())
				q.pop();
			LL min_slack = OO;
			for (int y=0; y<n; y++)
				if (!T[y] && slack[y] < min_slack)
					min_slack = slack[y];
			for (int x=0; x<n; x++)
				if (S[x])
					labelx[x] -= min_slack;
			for (int y=0; y<n; y++)
				if (T[y])
					labely[y] += min_slack;
				else
					slack[y] -= min_slack;
			for (int y=0; y<n; y++)
				if (!T[y] && slack[y] == 0)
					if (matched[y] == -1)
					{
						xx = slackx[y];
						yy = y;
						break;
					}
					else
					{
						T[y] = 1;
						if (!S[matched[y]])
						{
							q.push(matched[y]);
							add(matched[y], slackx[y], S, prev, labelx, labely, weight, slack, slackx);
						}
					}
			if (yy != -1)
				break;
			yy = -1;
		}
		if (yy != -1)
		{
			match_cnt++;
			for (int nx=xx, ny=yy, tmp; nx != -2; nx = prev[nx], ny = tmp)
			{
				tmp = matching[nx];
				matched[ny] = nx;
				matching[nx] = ny;
			}
		}
	}
	for (int x=0; x<n; x++)
		ret += weight[x][matching[x]];
	return ret;
}

// code written during the competition follows
int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		printf("Case #%d: ", tkase+1);
		int n;
		cin >> n;
		string tmp;
		getline(cin, tmp);
		VVLL graph(n, VLL(n, 0));
		for (int i=0; i<n; i++)
		{
			getline(cin, tmp);
			int k = 0;
			for (int j=n-1; j>=0; j--)
				if (tmp[j] == '1')
				{
					k = j;
					break;
				}
			for (int j=k; j<n; j++)
				graph[i][j] = 1000 - abs(i-j);
		}
		VI matching;
		LL ret = mw_perfect_matching(graph, matching) - n * 1000;
		// LOL
		int best = oo;
		sort(matching.begin(), matching.end());
		do
		{

			int sol = 0;
			VI old = matching;
			for (int i=0; i<n; i++)
			{
				int k = n;
				for (int j=i; j<n; j++)
					if (matching[j] == i)
					{
						k = j;
					}
				assert(k != n);
				sol += abs(i-k);
				for (int j=k; j>i; j--)
					matching[j] = matching[j-1];
				matching[i] = i;
			}
			matching = old;
			bool good = true;
			for (int i=0; i<n; i++)
				if (graph[i][matching[i]] <= 0)
				{
					good = false;
					break;
				}
			if (good)
			{
				best = min(best, sol);
			}
		} while (next_permutation(matching.begin(), matching.end()));
		cout << best << endl;

	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
