#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <ctime>
using namespace std;

#define for_each(it, v) for (typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)

const int MAX_N = 100;
const int MAX_M = 100;

int t, n, m;
pair<int, int> eventA[MAX_N + MAX_M];
pair<int, int> eventB[MAX_N + MAX_M];

int scanTime()
{
	int hour, minute;
	char buffer[1024];
	scanf("%s", buffer);
	sscanf(buffer, "%d:%d", &hour, &minute);
	return hour * 60 + minute;
}
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testInd = 0; testInd < testNum; testInd++)
	{
		scanf("%d%d%d", &t, &n, &m);
		for (int i = 0; i < n; i++)
		{
			eventA[i] = make_pair(scanTime(), -(-1));
			eventB[i] = make_pair(scanTime() + t, -(+1));
		}
		for (int i = 0; i < m; i++)
		{
			eventB[i + n] = make_pair(scanTime(), -(-1));
			eventA[i + n] = make_pair(scanTime() + t, -(+1));
		}
		sort(eventA, eventA + n + m);
		sort(eventB, eventB + n + m);
		int cntA = 0, cntB = 0;
		int curA = 0, curB = 0;
		for (int i = 0; i < n + m; i++)
		{
			if (eventA[i].second == -(+1))
				curA++;
			else if (curA > 0)
				curA--;
			else
				cntA++;
			if (eventB[i].second == -(+1))
				curB++;
			else if (curB > 0)
				curB--;
			else
				cntB++;
		}
		printf("Case #%d: %d %d\n", testInd + 1, cntA, cntB);
	}
	return 0;
}
