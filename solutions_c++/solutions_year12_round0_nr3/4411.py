#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<cmath>
#include<climits>
#include<algorithm>
#include<map>
using namespace std;

int valid[1001][1001];

bool judge(int st, int ed, int base)
{
	int i;
	for (i = 10; i <= base; i *= 10) if (st/i+st%i*(base*10/i) == ed) return 1;
	return 0;
}

void init()
{
	int i, j;
	memset(valid, 0, sizeof(valid));
	for (i = 10; i < 100; ++i) 
		for (j = i+1; j < 100; ++j) if (judge(i, j, 10)) valid[i][j] = 1;
	for (i = 100; i < 1000; ++i) for (j = i+1; j < 1000; ++j) if (judge(i, j, 100)) valid[i][j] = 1;
}

void conduct()
{
	int st, ed, i, j, ans;
	scanf("%d%d", &st, &ed);
	for (ans = 0, i = st; i < ed; ++i) 
		for (j = i+1; j <= ed; ++j) if (valid[i][j]) ans++;
	printf("%d\n", ans);
}

int main()
{
	init();
	int time;
	scanf("%d", &time);
	for (int i = 1; i <= time; ++i) {
		printf("Case #%d: ", i);
		conduct();
	} return 0;
}
