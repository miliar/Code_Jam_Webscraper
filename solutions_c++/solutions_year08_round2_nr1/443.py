#define _CRT_SECURE_NO_DEPRECATE 1
#include <vector>     
#include <map>     
#include <set>     
#include <deque>     
#include <algorithm>     
#include <utility>     
#include <sstream>     
#include <iostream>     
#include <cstdio>     
#include <cmath>     
#include <cstdlib>     

using namespace std; 

#define SZ(a) ((int)(a).size())
#define pii pair<int,int>
#define pll pair<__int64,__int64>
#define mp make_pair
template<class A, class B> A convert(B x) {stringstream s; s << x; A r; s >> r; return r;}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	vector <pll> trees;
	int testCnt = 0;
	cin >> testCnt;
	for (int testNum = 0; testNum < testCnt; ++testNum)
	{
		__int64 n, A, B, C, D, x0, y0, M; 
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		trees.clear();
		trees.push_back(mp(x0, y0));
		__int64 res = 0;

		for (int i = 1; i < n; ++i)
		{
			x0 = (A*x0 + B) % M;
			y0 = (C*y0 + D) % M;
			trees.push_back(mp(x0, y0));
		}

		for (int i = 0; i < SZ(trees); ++i)
			for (int j = i+1; j < SZ(trees); ++j)
				for (int k = j+1; k < SZ(trees); ++k)
				{
					__int64 xc = (double)(trees[i].first + trees[j].first + trees[k].first);
					__int64 yc = (double)(trees[i].second + trees[j].second + trees[k].second);
					res += (xc%3 == 0 && yc%3 == 0);
				}

		cout << "Case #" << testNum+1 << ": " << res << endl;
	}
	return 0;
}