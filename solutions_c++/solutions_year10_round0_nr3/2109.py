#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

#define runc true

#define MAXN 101

int R, K, N;

int pnum[MAXN];
int dp[MAXN], next[MAXN]; // head == n, dp[n] is the cost, next[n] is next head
int rec[MAXN], top;

void buildDP()
{
	int i=0;
	dp[0] = 0;
	for(; i<N; i++){
		if(dp[0] + pnum[i] <= K)
			dp[0] += pnum[i];
		else
			break;
	}
	next[0] = i%N;

	for(i=1;i<N;i++){
		dp[i] = dp[i-1] - pnum[i-1];

		int j = next[i-1];
		//printf("%d %d\n", j, pnum[j]);
		while(dp[i] + pnum[j] <= K){
			dp[i] += pnum[j];
			j++;
			if(j>=N)
				j %= N;
			if(j==i)
				break;
		}
		next[i] = j;
	}
}
//return i | rec[i] == num, -1 is not found
int isOver(int num)
{
	for(int i=0;i<top;i++){
		if(rec[i] == num)
			return i;
	}
	return -1;
}

#if runc
int main()
#else
int C()
#endif
{
#ifndef ONLINE_JUDGE
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	int cse, cnt;
	scanf("%d\n", &cse);
	for(cnt=1;cnt<=cse;cnt++){
		scanf("%d %d %d", &R, &K, &N);

		for(int i=0;i<N;i++){
			scanf("%d", &pnum[i]);
		}

		buildDP();
/*
		for(int i=0;i<N;i++){
			printf("%d: %d %d\n", i, dp[i], next[i]);
		}
*/

		int ans = 0, now=0, dotimes;
		top = 0;
		int loopsta = -1;

		for(dotimes=1 ;  ; dotimes++){
			ans += dp[now];

			rec[top] = now;
			top++;

			if(dotimes == R)
				break;

			now = next[now];

			loopsta = isOver(now);
			if(loopsta >= 0){
				break;
			}

		}

		if(loopsta >= 0){
			int reccost = 0;
			for(int i = rec[loopsta];; i=next[i]){
				reccost += dp[i];

				if(i == rec[top-1])
					break;
			}

			int rectime = top - loopsta ;
			int remind = (R-dotimes);
			ans += reccost * (remind / rectime);
			remind %= rectime;

			//printf("%d %d %d %d %d\t\t", loopsta, remind, rectime, reccost, ans);
			now = 0;
			for(int i=0;i<loopsta;i++)
				now = next[now];
			for(int i=0; i<remind; i++){
				ans += dp[now];
				now = next[now];
			}
		}

		printf("Case #%d: %d\n", cnt, ans);

	}
	return 0;
}
