#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <algorithm>
#include <cstring>
using namespace std;

int groups[1000];
int next[1000];
long long cou[1000];
bool vis[1000];
int main()
{
	ifstream cin("C-large.in");
	ofstream cout("C-large.out");
	int T;
	cin >> T;
	for(int cc = 1; cc <= T; cc++)
	{
		long long R, k, N;
		cin >> R >> k >> N;
		for(int i = 0; i < N; i++)
			cin >> groups[i];

		for(int s = 0; s < N; s++)
		{
			long long cap = k - groups[s];
			int n = 1;
			while(n < N)
			{
				if(groups[(s+n)%N] > cap)
					break;
				cap -= groups[(s+n)%N];
				n++;
			}

			next[s] = (s+n)%N;
			cou[s] = k-cap;
		}

		memset(vis,false,sizeof(vis));
		int node = 0;
		long long profit = 0;
		while(R && !vis[node])
		{
			R--;
			vis[node] = true;
			profit += cou[node];
			node = next[node];

		}

		if(R > 0)
		{
			int ss = node;
			int cycle = 1;
			long long cprof = cou[node];
			//profit -= cprof;
			node = next[node];
			while(node != ss)
			{
				cycle++;
				cprof += cou[node];
				node = next[node];
			}

			profit += (R/cycle)*cprof;
			R %= cycle;

			while(R--)
			{
				profit += cou[node];
				node = next[node];
			}
		}

		cout << "Case #" << cc << ": " << profit << endl;

	}
}