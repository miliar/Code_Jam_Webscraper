#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
using namespace std;

typedef pair<char,int> OP;
const int N = 100 + 10;
OP op[N];
int t[N];

int getTime(int idx)
{
	char robot = op[idx].first;
	int pos = op[idx].second;

	int p = idx-1;
	while (p >= 1 && op[p].first != robot)
		p--;
	int lastpos = op[p].second;
	int lastt = t[p];

	int tt = max(abs(pos - lastpos) + lastt, t[idx-1]) + 1;
	return tt;
}

void work(int testcase)
{
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
		cin >> op[i].first >> op[i].second;
	op[0].second = 1;
	memset(t, 0, sizeof(t));
	for (int i = 1; i <= n; i++)
	{
		t[i] = getTime(i);
	}
	cout << "Case #" << testcase << ": " << t[n] << endl;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int testcase = 1; testcase <= T; testcase++)
		work(testcase);
}
