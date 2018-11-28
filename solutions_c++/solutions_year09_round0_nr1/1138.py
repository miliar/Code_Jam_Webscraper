#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))

using namespace std;

int l, d;
int words[5005][16];
char buf[10000];
int pat[16];

void solvecase() {
	scanf("%s", buf);
	int cur = 0;
	for (int i = 0; i < l; i++)
	{
		pat[i] = 0;
		if (buf[cur] == '(')
		{
			cur++;
			while (buf[cur] != ')')
			{
				pat[i] |= 1 << (buf[cur] - 'a');
				cur++;
			}
			cur++;
		}
		else
		{
			pat[i] = 1 << (buf[cur] - 'a');
			cur++;
		}
	}
	int res = 0;
	for (int i = 0; i < d; i++)
	{
		bool ok = true;
		for (int j = 0; j < l; j++)
		{
			if ((pat[j] & words[i][j]) == 0)
			{
				ok = false;
				break;
			}
		}
		if (ok) res++;
	}
	printf("%d", res);
}

void solve() {
	int n;
	scanf("%d%d%d\n", &l, &d, &n);
	for (int i = 0; i < d; i++)
	{
		scanf("%s", buf);
		for (int j = 0; j < l; j++) words[i][j] = 1 << (buf[j] - 'a');
	}
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	freopen("y", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}