#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define FN(a, b, c) for( (a) = (b); (a) < (c); a++)
#define FB(a, b, c) for( (a) = (b); (a) >= (c); a--)
#define REP(i, n) FN(i,0,n)
#define RREP(i, n) FN(i,n,0)
#define RIT(i, n) FN(i, n.begin(), n.end())
#define RRIT(i, n) FN(i, n.rbegin(), n.rend())

using namespace std;

int main()
{
	int T, i, j, k, l, res;
	cin >> T;
	REP(i, T)
	{
		cout << "Case #" << (i+1) << ": " << endl;
		int n;
		cin >> n;
		double team[100][6] = {0.0};
		string schedule[n];
		REP(j, n)
		{
			cin >> schedule[j];
			REP(k, n)
			{
				if(schedule[j][k] == '.') continue;
				team[j][0] += 1;
				if(schedule[j][k] == '1' ) team[j][1] += 1;
				else if(schedule[j][k] == '0' ) team[j][2] += 1;
			}
			team[j][3] = team[j][1] / team[j][0];
		}
		REP(j, n)
		{
			team[j][4] = 0;
			REP(k, n)
			{
				if(k == j || schedule[j][k] == '.') continue;
				double gamewin = team[k][1];
				if(schedule[j][k] == '0' && gamewin > 0) gamewin--;
				team[j][4] += gamewin/(team[k][0]-1);
				//cout << j << " " << k << " " << gamewin/(team[k][0] - 1) << endl;
			}
			team[j][4] /= team[j][0];
		}
		REP(j, n)
		{
			team[j][5] = 0;
			REP(k, n)
			{
				if(k == j || schedule[j][k] == '.') continue;
				team[j][5] += team[k][4];
			}
			team[j][5] /= team[j][0];
			//cout << team[j][4] <<endl;
			cout << (0.25 * team[j][3] + 0.50 * team[j][4] + 0.25 * team[j][5]) << endl;
		}
	}
	return 0;
}