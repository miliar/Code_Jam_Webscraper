#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <functional>
using namespace std;

#pragma comment(linker,"/STACK:100000000")

int len[10050];
string w[10050];
string order, pattern, ans;
bool use[10050];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input2.txt", "r", stdin);
	freopen("output3.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int tt=0; tt<T; ++tt)
	{
		int n, m;
		int i, j, k, u, y;
		scanf("%d%d", &n, &m);
		for (i=0; i<n; ++i)
		{
			cin >> w[i];
			len[i]=w[i].size();
		}
		cout << "Case #" << tt+1 << ":";
		for (i=0; i<m; ++i)
		{
			int mx=-1;
			cin >> order;
			for (j=0; j<n; ++j)
			{
				int cur=0;
				memset(use, false, sizeof(use));
				pattern="";
				for (u=0; u<len[j]; ++u)
					pattern+="_";
				for (u=0; u<26; ++u)
				{
					for (y=0; y<len[j] && w[j][y]!=order[u]; ++y);
					if (y<len[j])
					{
						for (y=0; y<len[j]; ++y)
							if (w[j][y]==order[u])
								pattern[y]=order[u];
						if (pattern==w[j])
							break;
					}
					else
					{
						for (k=0; k<n; ++k)
						{
							if (len[j]!=len[k] || k==j)
								continue;
							for (y=0; y<len[j] && (pattern[y]=='_' && !use[w[k][y]-'a'] || pattern[y]==w[k][y]); ++y);
							if (y<len[j])
								continue;
							for (y=0; y<len[j] && w[k][y]!=order[u]; ++y);
							if (y<len[j])
								break;
						}
						if (k<n)
							cur++;
					}
					use[order[u]-'a']=true;
				}
				if (cur>mx)
				{
					mx=cur;
					ans=w[j];
//					printf("%d ", mx);
				}
			}
			cout << " " << ans;
		}
		cout << endl;
	}
	return 0;
}
