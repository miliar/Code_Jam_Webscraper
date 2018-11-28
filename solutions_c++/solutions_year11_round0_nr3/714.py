#include <functional>
#include <algorithm>
#include <iostream>
#include <iterator>
#include <cstdlib>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <bitset>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <map>
#include <set>

using namespace std;

typedef istringstream ISS;
typedef ostringstream OSS;
#define VT vector
typedef VT<int> VI;
typedef VT<vector<int>> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
typedef VT<VD> VVD;
typedef pair<int,int> PII;

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define FOR(i,a,b) for(int i=(int)a;i<=(int)b;++i)
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define MP make_pair





int main()
{

#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

#endif

	int T;
	cin >> T;

	REP(t, T)
	{
		int N;
		cin >> N;

		VI candies;
		REP(i,N)
		{
			int c;
			cin >> c;
			candies.push_back(c);
		}

		int x=0,s=0;
		REP(i, candies.size())
		{
			x = x ^ candies[i];
			s = s + candies[i];
		}

		if (x == 0)
		{
			cout << "Case #" << (t+1) << ": " << (s-*min_element(ALL(candies))) << "\n";
		}
		else
		{
			cout << "Case #" << (t+1) << ": " << "NO" << "\n";
		}

	}
}



