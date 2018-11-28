#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

const int inf = 10000000;
const pair<int,int> nullp = pair<int,int>(inf,inf);
const pair<int,int> nulla = pair<int,int>(0,0);

int NA, NB, T;
int SA[3000], SB[3000];
vector<int> p;

pair<int,int> dp[2][602][602];

int tomins(char s[10])
{
	int h, m;
	sscanf(s, "%d:%d", &h, &m);
	return h * 60 + m;
}


int main()
{	
	int test, tests;
	scanf("%d", &tests);
	for (test = 1; test <= tests; ++test)
	{
		// inicijalizujem
		memset(SA, 0, sizeof SA);
		memset(SB, 0, sizeof SB);
		p.clear();
		for (int i = 0; i < 2; ++i)
		for (int j = 0; j < 202; ++j)
		for (int k = 0; k < 202; ++k)
		dp[i][j][k] = nullp;
		
		// ucitam
		scanf("%d", &T);
		scanf("%d %d", &NA, &NB);
		
		char s[10];
		
		for (int i = 0; i < NA; ++i)
		{
			scanf("%s", s);
			int f = tomins(s);
			scanf("%s", s);
			int t = tomins(s) + T;
			p.push_back(f);
			p.push_back(t);
			SA[f]--;
			SB[t]++;
		}
		
		for (int i = 0; i < NB; ++i)
		{
			scanf("%s", s);
			int f = tomins(s);
			scanf("%s", s);
			int t = tomins(s) + T;
			p.push_back(f);
			p.push_back(t);
			SB[f]--;
			SA[t]++;
		}
		sort(p.begin(),p.end());
		p.resize(unique(p.begin(),p.end()) - p.begin());
		
		// uradim
		if (NA == 0 && NB == 0)
		{
			printf("Case #%d: 0 0\n", test);
			continue;
		}
		
		int idx = 0, nidx = 1;
		dp[0][0][0] = nulla;
		for (int tidx = 0; tidx < p.size(); ++tidx, idx ^= 1, nidx ^= 1)
		{
			for (int j = 0; j < 302; ++j)
			for (int k = 0; k < 302; ++k)
			dp[nidx][j][k] = nullp;
			
			int t = p[tidx];
			for (int i = 0; i <= 2*(NA + NB); ++i)
			{
				for (int j = 0; j <= 2*(NA + NB); ++j)
				{
					if (dp[idx][i][j] == nullp) continue;
	
					int idx1, idx2, add1 = 0, add2 = 0;
					
					// za A
					if (i >= -SA[t])
						idx1 = i + SA[t];
					else
					{
						idx1 = 0;
						add1 = -(i+SA[t]);
					}
					
					// za B
					if (j >= -SB[t])
						idx2 = j + SB[t];
					else
					{
						idx2 = 0;
						add2 = -(j+SB[t]);
					}
					
					dp[nidx][idx1][idx2] = make_pair(dp[idx][i][j].first + add1, dp[idx][i][j].second + add2);
				}
			}
		}
		
		// print solution
		int cnt = inf;
		pair<int,int> sol;
		for (int i = 0; i < 201; ++i)
		for (int j = 0; j < 201; ++j)
		{
			pair<int,int> pr = dp[idx][i][j];
			if (pr != nullp)
			{
				if (pr.first + pr.second< cnt)
				{
					cnt = pr.first + pr.second;
					sol = pr;
				}
			}
		}
		
		printf("Case #%d: %d %d\n", test, sol.first, sol.second);
	}
	
	//system("pause");
	return 0;
}
