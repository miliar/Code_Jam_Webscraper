#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

int items[2000];
bool hash[1500000];
int que[2000000];
int dp[2][1500000];

int BF(int n, int tot, int xortot)
{
	int ans = -1;
	int N = (1<<n)-1;
	for(int i=1; i<N; i++)
	{
		int xorsum = 0;
		int sum = 0;
		for(int j=0; j<n; j++) if((1<<j) & i)
		{
			xorsum = xorsum ^ items[j];
			sum += items[j];
		}

		if(xorsum == (xorsum^xortot))
		{
			if(tot - sum > ans)
				ans = tot - sum;
		}
	}

	return ans;
}

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	//freopen("xxx-large.out", "w", stdout);
	int test, cas = 1;
	cin>>test;
	while(test--)
	{
		int N;
		cin>>N;
		int i, j;
		
		memset(hash, 0, sizeof(hash));

		int tot = 0;
		int xorTot = 0;
		for(i=0; i<N; i++)
		{
			scanf("%d", &items[i]);
			tot += items[i];
			xorTot = xorTot ^ items[i];
		}

		int ans = -1;
		ans = BF(N, tot, xorTot);
		//int ct = 0, pct = 0;
		//for(i=0; i<N; i++)
		//{
		//	for(j=0; j<pct; j++) dp[0][que[j]] = dp[1][que[j]];
		//	if(!hash[items[i]])
		//	{
		//		hash[items[i]] = 1;
		//		dp[1][items[i]] = items[i];
		//		que[ct++] = items[i];
		//	}
		//	else if(items[i]<dp[1][items[i]])
		//		dp[1][items[i]] = items[i];

		//	for(j=0; j<pct; j++)
		//	{
		//		int tmp = items[i] ^ que[j];
		//		int totTmp = items[i] + dp[0][que[j]];
		//		if(!hash[tmp])
		//		{
		//			hash[tmp] = 1;
		//			dp[1][tmp] = totTmp;
		//			que[ct++] = tmp;
		//		}
		//		else if(totTmp < dp[1][tmp])
		//			dp[1][tmp] = totTmp;
		//		
		//		if((xorTot^tmp) == tmp)//can be divied into two equal piles
		//		{
		//			if(tot-dp[1][tmp] > ans)
		//				ans = tot - dp[1][tmp];
		//		}
		//	}
		//	pct = ct;
		//}

		cout << "Case #" << cas++ << ": ";
		if(ans!=-1)
			cout << ans << endl;
		else
			cout << "NO\n";
	}
	return 0;
}