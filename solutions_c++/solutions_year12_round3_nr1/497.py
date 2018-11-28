#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <string>
#include <bitset>
#include <map>

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>

using namespace std;

#define MAX 1010

int n,m;
bool okay;
vector <int> a[MAX];
bool used[MAX];

void dfs(int source)
{
	int now,i;
	stack <int> s;
	s.push(source);
	while(!s.empty())
	{
		now = s.top();
		s.pop();
		for(i=0;i<a[now].size();i++)
		{
			if(!used[ a[now][i] ])
			{
				s.push(a[now][i]);
				used[ a[now][i] ] = 1;
			}
			else
			{
				okay = 1;
				return;
			}
		}
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-out.txt","w",stdout);
	int t,T;
	int i,j,x;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		scanf("%d",&n);
		for(i=1;i<=n;i++) { a[i].clear(); }
		for(i=1;i<=n;i++)
		{
			scanf("%d",&m);
			for(j=0;j<m;j++)
			{
				scanf("%d",&x);
				a[i].push_back(x);
			}
		}
		okay = 0;
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++) used[j]=0;
			dfs(i);
			if(okay) break;
		}
		printf("Case #%d: %s\n",t,okay ? "Yes" : "No");
	}
	return 0;
}



