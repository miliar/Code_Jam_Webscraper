#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
const int MAX = 305;

struct INFO
{
	int st, end;
	int p;
}train[MAX], temp;
bool cmp(const INFO &A, const INFO &B)
{
	if (A.st == B.st)
		return A.end < B.end;
	return A.st < B.st;
}
int t, cnta, cntb, cnt;
priority_queue<int, vector<int>, greater<int> > Q[2];
int ans[2];

void solve()
{
	while (!Q[0].empty()) Q[0].pop();
	while (!Q[1].empty()) Q[1].pop();

	int i, nowp, nextp, ontop;
	for (i = 0; i < cnt; ++ i)
	{
		nowp = train[i].p;
		nextp = 1 - nowp;
		if (Q[nextp].empty() || (ontop = Q[nextp].top()) > train[i].st)
		{
			ans[nowp] ++;
			Q[nowp].push(train[i].end + t);
		}
		else
		{
			Q[nextp].pop();
			Q[nowp].push(train[i].end + t);
		}
	}
}

int main (void)
{
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	int N, Case = 1;
	scanf("%d", &N);
	while (N --)
	{
		scanf("%d", &t);
		scanf("%d %d", &cnta, &cntb);
		int i, ta, tb;
		for (i = 0; i < cnta; ++ i)
		{
			scanf("%d:%d", &ta, &tb);
			train[i].st = ta*60+tb;
			scanf("%d:%d", &ta, &tb);
			train[i].end = ta*60+tb;
			train[i].p = 0;
		}
		for (i = cnta; i < cnta+cntb; ++ i)
		{
			scanf("%d:%d", &ta, &tb);
			train[i].st = ta*60+tb;
			scanf("%d:%d", &ta, &tb);
			train[i].end = ta*60+tb;
			train[i].p = 1;
		}
		cnt = cnta+cntb;
		sort(train, train+cnt, cmp);

		ans[0] = ans[1] = 0;
		solve();
		printf("Case #%d: %d %d\n", Case++, ans[0], ans[1]);
	}
	return 0;
}