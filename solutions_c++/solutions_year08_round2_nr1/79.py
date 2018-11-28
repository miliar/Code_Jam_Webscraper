#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
using namespace std; 

#define DEBUG(x) fout << '>' << #x << ':' << x << endl;
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FOR2(i, a, b) for (int i = (a); i > (b); --i)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }
const int INF = 1 << 29;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
#ifdef WIN32
typedef __int64 ll;
#else
typedef long long ll;
#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////// 

ofstream fout("output.out");
ifstream fin("input.in");

ll nums[3][3];

int main()
{
	int T;
	fin >> T;

	FOR(step, 0, T)
	{
		ll n, A, B, C, D, x0, y0, M;
		fin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		
		vector<pair<ll, ll> > trees;
		ll X = x0, Y = y0;
		trees.push_back(make_pair(X, Y));
		FOR(i, 1, n)
		{
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			trees.push_back(make_pair(X, Y));
		}

		FOR(i, 0, 3) FOR(j, 0, 3) nums[i][j] = 0;
		FOR(i, 0, trees.size())
			++nums[trees[i].first%3][trees[i].second%3];

		ll res = 0;
		FOR(i, 0, trees.size())
			FOR(j, i+1, trees.size())
			{
				--nums[trees[i].first%3][trees[i].second%3];
				--nums[trees[j].first%3][trees[j].second%3];
				
				res += nums[(3-(trees[i].first+trees[j].first)%3)%3][(3-(trees[i].second+trees[j].second)%3)%3];

				++nums[trees[i].first%3][trees[i].second%3];
				++nums[trees[j].first%3][trees[j].second%3];
			}
		fout << "Case #" << step+1 << ": " << res/3 << endl;
	}

	return 0;
}
