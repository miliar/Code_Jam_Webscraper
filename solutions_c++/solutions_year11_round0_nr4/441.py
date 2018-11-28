#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <memory.h>

using namespace std;
#define MAXN 1100
int N;
int n[MAXN];
bool c[MAXN];

int main()
{
	int cases;
	int casenum = 1;
	freopen("test", "r", stdin);
	freopen("output", "w", stdout);
	scanf("%d", &cases);
	while(cases--)
	{
		scanf("%d", &N);
		for(int i = 1;i <= N; i++){
			scanf("%d", &n[i]);
		}

		double needswap = 0;

		memset(c, false, sizeof(c));
		for(int i = 1;i <= N; i++){
			if(n[i] == i)continue;	// correct
			if(c[i])continue;		// traversed before

			c[i] = true;			//position i is checked
			int s = n[i];			//start
			int now = n[i];			//current value in position i
			int count = 0;
			while(true){
				count++;
				c[now] = true;
				now = n[now];
				if(now == s)break;
			}
			needswap += count;
		}
		printf("Case #%d: %.6lf\n", casenum++, needswap);
	}
	return 0;
}

