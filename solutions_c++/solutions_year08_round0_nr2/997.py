#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;

struct SSche
{
	int a, b;
	bool operator<(SSche &sb)
	{
		if (a != sb.a)
			return a < sb.a;
		else
			return b < sb.b;
	}

}sche[2][105];
int nsche[2];

struct STrain
{
	int time;
	bool operator<(STrain &sb)
	{
		return time > sb.time;
	}
}train[2][105];
int ntrain[2];


int trainuse[2];
int inter;

int converttime(char *str)
{
	int h, m;

	sscanf(str, "%d:%d", &h, &m);
	return h*60+m;
}

void subsolve(int now, int inow)
{
	if (ntrain[now] > 0 && train[now][0].time <= sche[now][inow].a) {
		pop_heap(train[now], train[now]+ntrain[now]);
		ntrain[now] --;
	}
	else {
		trainuse[now] ++;
	}

	train[1-now][ntrain[1-now]].time = sche[now][inow].b + inter;
	ntrain[1-now] ++;
	push_heap(train[1-now], train[1-now]+ntrain[1-now]);
}

void solve()
{
	int i0, i1;

	sort(sche[0], sche[0] + nsche[0]);
	sort(sche[1], sche[1] + nsche[1]);

	ntrain[0] = ntrain[1] = 0;
	trainuse[0] = trainuse[1] = 0;

	i0 = 0;
	i1 = 0;

	while (i0 < nsche[0] || i1 < nsche[1]) {
		if ((i0 < nsche[0] && i1 < nsche[1] && sche[0][i0].a <= sche[1][i1].a)
			|| (i1 >= nsche[1])) {
			subsolve(0, i0);
			i0 ++;
		}
		else {
			subsolve(1, i1);
			i1 ++;
		}
	}
}

int main()
{
	int i, j;
	int t, nowt;
	char str[200];

	freopen("B-large.in.txt", "r", stdin);
	freopen("B-large.out.txt", "w", stdout);

	scanf("%d", &t);
	nowt = 0;
	while (t--) {
		nowt ++;
		scanf("%d", &inter);
		scanf("%d%d", &nsche[0], &nsche[1]);
		for (i = 0; i < 2; i ++) {
			for (j = 0; j < nsche[i]; j ++) {
				scanf("%s", str);
				sche[i][j].a = converttime(str);
				scanf("%s", str);
				sche[i][j].b = converttime(str);
			}
		}

		solve();

		printf("Case #%d: %d %d\n", nowt, trainuse[0], trainuse[1]);
	}

	return 0;
}
