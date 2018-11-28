#include<iostream>
#include<stdio.h>
using namespace std;
#include<vector>
#include<map>
#include<algorithm>
#include<string>
#include<stdlib.h>
#include<set>
#include<queue>
#include<map>
int a[1000];
int b[1000];
queue<int> remove1;
struct info
{
	int flavor;
	int malted;
};
vector<info> info_v[3000];
int finish[3000];
int res[3000];
int main()
{
	int n;
	int i;
	freopen( "test.in", "r", stdin );
	freopen( "test.out", "w", stdout );
	int c;
	scanf("%d", &c);
	for(i = 0; i < c; i++)
	{
		int n;
		while(!remove1.empty())
			remove1.pop();
		memset(res, 0,sizeof(res));
		memset(finish, 0,sizeof(finish));
		int m;
		scanf("%d%d", &n, &m);
		int j;
		int finish_num = 0;
		for(j = 0; j < m; j++)
		{
			info_v[j].clear();
			int t;
			scanf("%d", &t);
			int k;
			for(k = 0; k < t; k++)
			{
				int x, y;
				scanf("%d%d", &x, &y);
				info temp;
				temp.flavor= x; temp.malted = y;
				info_v[j].push_back(temp);
				if(t == 1 && y == 1)
				{
					if(res[x] == 0)
					{
						remove1.push(x);
					}
					res[x] = 1;
					finish[j] = 1;
					finish_num++ ;
				}
			}
		}
		int flag = 0;
		while(!remove1.empty() && finish_num < m && flag == 0)
		{
			int temp = remove1.front();
			remove1.pop();
			for(j = 0; j < m; j++)
			{
				if(finish[j] == 0)
				{
					vector<info>::iterator p;
					for(p = info_v[j].begin(); p!= info_v[j].end(); p++)
					{
						if(p->flavor == temp)
						{
							if(p ->malted == 1)
							{
								finish[j] = 1;
								finish_num++;
							}
							else
							{
								info_v[j].erase(p);
							}
							break;
						}
					}
					if(finish[j] == 1)
						continue;

					if(info_v[j].size() == 0)
					{
						flag = 1;
						break;
					}
					if(info_v[j].size() == 1 && info_v[j][0].malted == 1)
					{
						int temp = info_v[j][0].flavor;
						finish[j] = 1;
						finish_num++;
						if(res[temp] == 0)
						{
							res[temp] = 1;
							remove1.push(temp);
						}
					}
				}
			}
		}
		if(flag == 0)
		{
			printf("Case #%d:", i + 1);
			for(j = 1; j <= n; j++)
			{
				printf(" %d", res[j]);
			}
			printf("\n");
		}
		else 
			printf("Case #%d: IMPOSSIBLE\n", i + 1);
	}
}