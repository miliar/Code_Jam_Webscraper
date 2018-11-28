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

		VI p;

		REP(i,N)
		{
			int d;
			cin>>d;
			p.push_back(d-1);
		}
		
		VI visited(p.size());

		VVI cycles;

		REP(i, p.size())
		{
			int j = i;

			VI cycle;
			while(!visited[j])
			{
				visited[j] = true;
				cycle.push_back(j);
				j = p[j];
			}

			if (cycle.size())
				cycles.push_back(cycle);
				
		}

		int exp=0;

		REP(i, cycles.size())
		{
			if (cycles[i].size() > 1)
			exp += (cycles[i].size());
		}



		cout << "Case #" << (t+1) << ": " << exp << ".000000" << "\n";

	}
}



