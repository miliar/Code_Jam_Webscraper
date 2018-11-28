#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <climits>
#include <cstdio>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int solve(vector< pair<int, int> > a)
{
	int pos[2] = {1, 1}, slack[2] = {0, 0}, totTime = 0;

	for (int i=0; i<a.size(); i++)
	{
		int r = a[i].first;
		int timeTaken = abs(a[i].second - pos[r]) + 1;

		timeTaken = max(1, timeTaken - slack[r]);
	
		totTime += timeTaken;
		slack[!r] += timeTaken;
		slack[r] = 0;
		pos[r] = a[i].second;
	}

	return totTime;
}

int main()
{
	freopen("data.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T; cin >> T;
	
	for (int x=1; x<=T; x++)
	{
		cout << "Case #" << x << ": "; 

		int n; cin >> n;

		vector< pair<int, int> > ins;

		for (int i=0; i<n; i++)
		{
			string str; int tval; cin >> str >> tval;
			ins.push_back( make_pair( (str=="O" ? 0 : 1), tval) );
		}

		cout << solve(ins) << endl;
	}
}