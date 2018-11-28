#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;
int x[10], y[10], n, ans;
void dfs(int d, __int64 sum, int visited[])
{
	if(d == n && ans > sum)
		ans = sum;
	for(int i = 1; i <=n; i++)
	{
		if(visited[i]) continue;
		visited[i] = 1;
		dfs(d+1, sum+x[i]*y[d+1], visited);
		visited[i] = 0;
	}
}
int main()
{
	int visited[10];
	int T;
	ifstream cin("1.txt");
	ofstream cout("output.txt");
	cin>>T;
	for(int Case = 1; Case <= T; Case++)
	{
		cin>>n;
		for(int i = 1; i <= n; i++) cin>>x[i];
		for(int i = 1; i <= n; i++) cin>>y[i];
		ans = (1<<30);
		memset(visited, 0, sizeof(visited));
		dfs(0, 0, visited);
		
		cout<<"Case #"<<Case<<": "<<ans<<"\n";
	}
}