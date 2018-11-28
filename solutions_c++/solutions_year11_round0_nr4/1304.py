#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

#define see(x) cout<<#x<<" "<<x<<endl
#define sp system("pause")

int a[1010];
bool vis[1010];

int main(int argc, char *argv[])
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.txt", "w", stdout);
	int t, T;
	cin>>T;
	for(t = 1; t <= T; t++)
	{
		memset(vis, false, sizeof(vis));
		int n, res = 0;
		cin>>n;
		for(int i = 0, j = n; i < n && j >0; ++i, --j)
		{
			cin>>a[i];
			a[i]--;
			//a[i] = j;
			//cout<<j<<endl;
		}
		for(int i = 0; i < n; ++i)
			if(!vis[i])
			{
				vis[i] = true;
				int cnt = 1;
				for(int j = a[i]; !vis[j] ; j = a[j])
				{
					vis[j] = true;
					cnt++;
				}
				//see(cnt);
				if(cnt != 1)
					res += cnt;
			}
		printf("Case #%d: %.6lf\n", t, 1.0*res);
	}
	return 0;
}
