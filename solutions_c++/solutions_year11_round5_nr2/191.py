#include <assert.h> 
#include <ctype.h> 
#include <float.h> 
#include <math.h> 
#include <stdio.h> 
#include <string> 
#include <stdlib.h> 
#include <time.h> 
#include <algorithm> 
#include <numeric> 
#include <functional> 
#include <utility> 
#include <vector> 
#include <list> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <sstream> 
#include <iostream> 
#include <memory.h>

using namespace std; 

#define rep(i,n) for(int i=0;i<(n);++i)
#define clr(a,b) memset(a,b,sizeof(a)); 
#define all(c) (c).begin(), (c).end() 
#define inf 1000000000 

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;

int dp[1001];

vector<int> card;
vector<int> vis;

int ans = 0;

void brute(int pos, int last, int lenCur, int lenSmall)
{
	if (pos == card.size())
	{
		bool f = false;

		if (lenCur)
			lenSmall = min(lenSmall, lenCur);

		for (int i = 0; i < card.size(); i++)
		{
			if (!vis[i])
			{
				f = true;
				vis[i]= 1;
				brute(i + 1, card[i], 1, lenSmall);
				vis[i]= 0;
				break;
			}
		}

		if (!f)
		{
			ans = max(ans, lenSmall);
		}

		return ;
	}

	if (!vis[pos])
	{
		if (card[pos] == last + 1)
		{
			vis[pos] = 1;
			brute(pos + 1, last + 1, lenCur + 1, lenSmall);
			vis[pos] = 0;
		}
	}
	brute(pos + 1, last, lenCur, lenSmall);
}


void solveTest()
{
	int N;
	cin >> N;

	card.resize(N);
	rep(i, N) cin >> card[i];

	sort(all(card));
	vis.assign(N, 0);	

	ans = 0;
	brute(card.size(), 0, 0, 10000);
	

	if (ans == 10000)
		ans = 0;

	printf("%d\n", ans);
	/*
	dp[0] = 100000000;

	int l = 0;
	int r = card.size();

	while (l < r)
	{
		int straightLen = (l + r) / 2;

		bool can = true;

		vector<int> vis(card.size());

		for (int i = 0; i < card.size(); i++)
		{
			int cnt = 0;
			if (vis[i] != 1)
			{
				while (true)
				{
					int l = card[i];
					int total = 0;

					while (true)
					{
						vis[i] = 1;
						total++;
						
						l++;

						while (card[])
					}
				}

			}		
		}
	}
*/

}


int main(int argc, char* argv[])
{
	freopen("test.in", "r", stdin);

	int T;
	scanf("%d", &T);

	for (int nTest = 1; nTest <= T; nTest++)
	{		
		printf("Case #%d: ", nTest);

		solveTest();

		fflush(stdout);
	} 

	return 0;
}


