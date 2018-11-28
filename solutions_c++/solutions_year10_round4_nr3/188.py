#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<utility>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PII;

#define MP make_pair
#define PB push_back
#define REP(i, n) for(int i=0, _n=(n); i<_n; ++i)
#define min(a, b) ((a)<(b)?(a):(b))

bool now;
bool a[2][311][311];
int R, cnt;

bool empty()
{
	for(int i=1; i<=100; ++i)
		for(int j=1; j<=100; ++j)
			if (a[now][i][j]) return false;
	return true;

}

int main()
{
	freopen("c.in", "rt", stdin);
	freopen("c.out", "wt", stdout);
	int T, tt=0;
	scanf("%d", &T);
	for(; tt<T; ) {
		scanf("%d", &R);
		now=0;
		memset(a, 0, sizeof(a));
		while (R--) {
			int x1, x2, y2, y1;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for(int i=y1; i<=y2; ++i)
				for(int j=x1; j<=x2; ++j)
					a[now][i][j]=true;
		}

		cnt=0;
		while (!empty()) {
			++cnt;
			/*
			for(int i=1; i<=6; ++i) {
				for(int j=1; j<=6; ++j)
					if (a[now][i][j]) cout << 1;
					else cout << 0;
				cout << endl;
			}
			*/
			now=!now;
			memset(a[now], 0, sizeof(a[now]));
			for(int i=1; i<=100; ++i)
				for(int j=1; j<=100; ++j) 
					if (!a[!now][i][j]) {
						if (a[!now][i][j-1] && a[!now][i-1][j]) a[now][i][j]=true;
					}
					else if (a[!now][i][j-1] || a[!now][i-1][j]) a[now][i][j]=true;
		}
		printf("Case #%d: %d\n", ++tt, cnt);
	}
	return 0;
}
