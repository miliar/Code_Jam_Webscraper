#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
using namespace std;

#define FORALL(var,x) for (typeof(x.begin()) var=x.begin(); var!=x.end(); var++)
#define FOR(var,lo,hi) for (int var=(lo); var<(hi); var++)
#define SORT(x) sort(x.begin(), x.end())
#define ALL(x) x.begin(), x.end()
#define UNIQUE(x) x.erase(unique(x.begin(),x.end()),x.end()) 

#define mp make_pair
#define pb push_back

typedef long long ll;
typedef vector<int> vi;

ll N, M, A;

int main(void)	{
	int numTestCases;
	cin >> numTestCases;

	for (int nc = 1; nc <= numTestCases; nc++)	{
		cin >> N >> M >> A;
		cout << "Case #" << nc << ": ";	
		bool found = false;

		for (ll x1 = 0; x1 <= N; x1++)	for (ll y1 = 0; y1 <= M; y1++)
			for (ll x2 = x1; x2 <= N; x2++)	for (ll y2 = 0; y2 <= M; y2++)
				for (ll x3 = x2; x3 <= N; x3++)	{
					//cout << x1 << " " << y1 << endl;
					ll X = x1*y2 - x2*y1 + y1*x3 - y2*x3;
					ll C = x1 - x2;
					ll testy3 = 0;
					//cout << A << " " << X << " " << C << endl;
					if (C == 0)	{
						if (X == A)	found = true;
					}
					else	{
						testy3 = (X - A) / C;
						if ((testy3 * C) == (X - A) && (0 <= testy3 && testy3 <= M))	found = true;
					}
					if (found)	{
						cout << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << testy3 << endl;
						found = true;
						goto foo;
					}
				}
					
		foo:

		if (!found)	cout << "IMPOSSIBLE" << endl;
	}

}
