#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <ctime>
using namespace std;

int n;

struct play
{
	int costTime, pDie, index;
	bool operator <(play u)const
	{
		int a = costTime * u.pDie;
		int b = u.costTime * pDie;
		if(a != b)
			return a < b;
		return index < u.index;
	}
}P[1001];

void solve()
{
	cin >> n;
	for(int i = 1; i <= n; i++)
		cin >> P[i].costTime;
	for(int i = 1; i <= n; i++)
		cin >> P[i].pDie;
	for(int i = 1; i <= n; i++)
		P[i].index = i;
	

	sort(P + 1, P + 1 + n);
	for(int i = 1; i <= n; i++)
		cout << P[i].index-1 << (i == n ? "\n" : " ");
}

int MAIN()
{
	int testCase;
	cin >> testCase;
	for(int caseID = 1; caseID <= testCase; caseID ++)
	{
		cout << "Case #" << caseID << ": ";
		solve();
	}
	return 0;
}

int main()
{
	ios :: sync_with_stdio(false);
	cout << fixed << setprecision(16);
	int RUN_RESULT = MAIN();
	return RUN_RESULT;
}
