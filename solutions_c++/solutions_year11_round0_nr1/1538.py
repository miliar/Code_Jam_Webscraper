/* by Ashar Fuadi [fushar] */

#include <cstdio>
#include <cstring>

#include <vector>
#include <string>
#include <set>
#include <list>
#include <map>
#include <queue>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0; i < (int)n; i++)
#define FOR(i, a, b) for (int i = (int)a; i <= (int)b; i++)
#define REPE(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)
#define RESET(c,v) memset(c, v, sizeof(c))

#define pb push_back
#define mp make_pair
#define DEBUG 1
#define PRINT(x...) DEBUG && printf(x)

int T;
int N;
int main()
{
	cin >> T;
	REP(tc, T)
	{
		cin >> N;
		
		queue<int> O, B;
		queue<string> robots;
		int pO = 1, pB = 1, res = 0;
		
		REP(i, N)
		{
			string r;
			int p;
			cin >> r >> p;
			robots.push(r);
			if (r == "O")
				O.push(p);
			else
				B.push(p);
		}
		
		while (!robots.empty())
		{
			res++;
			bool popped = false;
			if (!O.empty())
			{
				int o = O.front();
				if (robots.front() == "O" && o == pO)
				{
					robots.pop();
					popped = true;
					O.pop();
				}
				else if (pO < o)
					pO++;
				else if (pO > o)
					pO--;
			}
			
			if (!B.empty())
			{
				int b = B.front();
				if (!popped && robots.front() == "B" && b == pB)
				{
					robots.pop();
					B.pop();
				}
				else if (pB < b)
					pB++;
				else if (pB > b)
					pB--;
			}
		}
		cout << "Case #" << tc+1 << ": " << res << endl;
	}
}
