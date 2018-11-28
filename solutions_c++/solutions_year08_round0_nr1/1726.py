#include <cstdio>
#include <map>
#include <string>
#include <iostream>
#include <algorithm>

#define f(i, n)				for(int i = 0; i < (n); i ++)

std::map<std::string, int> m;
int a[1050];
int T, t, S, Q;
char s[150];
std::string cur;
int used[1050];

bool one[1050][1050];

int dp[1050], NOT_SET;
int part(int to)
{
	int &ret = dp[to];
	if( ret != NOT_SET )	return ret;
	if(to == 0)	return ret = 0;
	if( one[0][to] == 1 )	return ret = 0;
	int res = INT_MAX;
	f(i, to)
		if( one[i + 1][to] == 1 )
		{
			int d = part(i);
			if( d + 1 < res )	res = d + 1;
		}
//	printf("%d %d\n", to, res);
	return ret = res;
}

int main()
{
	scanf("%d", &T);
	for(t = 0; t < T; t ++)
	{
		memset(dp, -1, sizeof(dp)); NOT_SET = *dp;
		memset(one, 0, sizeof(one));
		m.clear();
		scanf("%d\n", &S);
//		printf("%d\n", S);
		f(i, S)
		{
			gets(s);
			m[s] = i + 1;
//			printf("\n%d %s %d\n", i, s, m[s]);
		}
		scanf("%d\n", &Q);
		f(i, Q)
		{
			gets(s);
			a[i] = m[s];
		}
		a[Q] = -1;
//		Q = std::unique(a, a + Q + 1) - a;
//		Q /= sizeof(a[0]);
//		f(i, Q) printf("%d ", a[i]); printf("\n");
		f(end, Q)
		{
			f(st, end + 1)
			{
				memset(used, 0, sizeof(used));
				for(int i = st; i <= end; i ++)	used[ a[i] ] ++;
//				printf("%d %d\n", st, end);
//				for(int i = 1; i <= S; i ++)	printf("%d ", used[i]);
//				printf("%d\n\n", std::count(used + 1, used + S + 1, 0));
				int cnt = std::count(used + 1, used + S + 1, 0);
				if( cnt != 0 )
					if( (a[end + 1] == -1) || (used[ a[end + 1] ] == 0) || (cnt > 1))
				{
//					printf("%d %d OK\n", st, end);
					one[st][end] = 1;
				}
			}
			one[end][end] = 1;
		}
//		f(i, Q){	f(j, i + 1) printf("%d", one[j][i]); printf("\n"); }
		int res = part(Q - 1);
		printf("Case #%d: %d\n", t + 1, res);
	}
}

