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

	REP(cs, T)
	{
		int N;
		cin >> N;

		VI button;
		VI robots;
		REP(i, N)
		{
			char r;
			cin >> r;
			robots.push_back(r == 'O');
			int b;
			cin>>b;
			button.push_back(b);
		}

		int o=1,b=1;
		int t = 0;
		REP(i, robots.size())
		{
			int& curr_robot = robots[i] ? o : b;
			int& other_robot = robots[i] ? b : o;

			bool color = robots[i];
			int next_button = -1;
			for(int j=i+1;j<robots.size();++j)
			{
				if (next_button==-1 && robots[j] == !color)
				{
					next_button = button[j];
					break;
				}
			}

			while(curr_robot != button[i])
			{
				if (button[i] > curr_robot)
					curr_robot++;
				else if (button[i] < curr_robot)
					curr_robot--;

				if (next_button != -1)
				{
					if (next_button > other_robot)
						other_robot++;
					else if (next_button < other_robot)
						other_robot--;
				}

				t++;
			}

			//				
			if (next_button != -1)
			{
				if (next_button > other_robot)
					other_robot++;
				else if (next_button < other_robot)
					other_robot--;
			}

			t++;


		}


		cout << "Case #" << (cs+1) << ": " << t << "\n";
	}
}



