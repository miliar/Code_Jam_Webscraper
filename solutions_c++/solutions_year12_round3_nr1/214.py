#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <stdio.h>
#include <map>
#include <vector>
#include <queue>
using namespace std;
int N;
vector<int> vec[1002];
int vis[1002];
int main()
{

	//freopen("D:\\visual studio 2008\\google code jam\\A-large.in", "r", stdin ) ;

	//freopen("D:\\visual studio 2008\\google code jam\\A-large.out", "w", stdout ) ;

	int cases;
	cin>>cases;
	for(int kk=1;kk<=cases;++kk)
	{
		scanf("%d", &N);
		for(int i=1;i<=N;++i)
			vec[i].clear();
					int num, a;
		for (int i = 1;i <= N; i++) 
		{

			scanf("%d" ,&num);
			while(num--)
			{
				scanf("%d" ,&a);
				vec[i].push_back(a);
			}
		}
		printf("Case #%d:", kk);
		int  ok = 0;
		for (int i = 1; i <= N&&!ok; i++) 
		{
			queue<int> que;
			memset(vis, 0, sizeof(vis));
			que.push(i);
			vis[i] = 1;
			while(!que.empty()&&!ok) 
			{
				int k = que.front();
				que.pop();
				for (int j = 0; j < vec[k].size(); j++)
				{
					que.push(vec[k][j]);
					if (vis[vec[k][j]])  
					{
						ok = 1;
						break;
					}
					vis[vec[k][j]] = 1;
				}
			}
		}
		if(ok)
			printf(" Yes\n");
		else
			printf(" No\n");
	}
	return 0;
}
