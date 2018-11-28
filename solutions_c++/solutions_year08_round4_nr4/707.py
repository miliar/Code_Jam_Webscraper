#include <iostream>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
int k, ans;
int visited[6], v[6];
char tmp[2001];
string s;
void dfs(int d, int visited[6], int v[6])
{
	if(d == k)
	{
			for(int j = 0; j < s.length(); j+=k)
			{
				for(int l = j; l < j + k; l++)
				{
					tmp[l] = s[j+v[l-j]-1];
				}
			}
			tmp[s.length()] = '\0';
			int ret = 1;
			char target = tmp[0];
			for(int i = 0; i < s.length(); i++)
			{
				if(tmp[i] == target) continue;
				ret++;
				target = tmp[i];
			}
			if(ans > ret) ans = ret;
		//}
	}
	for(int i = 1; i <= k; i++)
	{
		if(visited[i]) continue;
		visited[i] = 1;
		v[d] = i;
		dfs(d+1, visited, v);
		visited[i] = 0;
	}
}
int main()
{
	freopen("d.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	//ifstream cin("d.txt");
	//ofstream cout("out.txt");
	int T;
	scanf("%d", &T);
	for(int Case = 1; Case <= T; Case++)
	{
		printf("Case #%d: ", Case);
		cin>>k>>s;
		ans = s.length();
		memset(visited, 0, sizeof(visited));
		dfs(0, visited, v);
		printf("%d\n", ans);
	}
}