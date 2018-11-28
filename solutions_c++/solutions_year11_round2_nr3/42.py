#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;

vector<vector<int> >parts;
int best;
vector<int>ans;
int col[10];

void rec(int cur,int n,int u,int maxu)
{
	if (cur==n)
	{
		if (best>=u) return ;
		for(int i=0;i<parts.size();i++)
		{
			bool used[5]={0};
			for(int j=0;j<parts[i].size();j++) used[col[parts[i][j]]]=true;
			for(int j=0;j<u;j++)
				if (!used[j]) return ;
		}
		best=u;
		ans.clear();
		for(int i=0;i<n;i++) ans.push_back(col[i]+1);
		return ;
	}

	for(int i=0;i<u;i++) 
	{
		col[cur]=i;
		rec(cur+1,n,u,maxu);
	}

	if (u<maxu)
	{
		col[cur]=u;
		rec(cur+1,n,u+1,maxu);
	}
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int n,m,i,j,k,l,q,T;

	cin>>T;
	for(int test=1;test<=T;test++)
	{
		cin>>n>>m;
		int u[10], v[10];
		for(i=0;i<m;i++) cin>>u[i];
		for(i=0;i<m;i++) cin>>v[i];

		vector<int>x;
		for(i=0;i<n;i++) x.push_back(i);
		parts.clear();
		parts.push_back(x);

		for(i=0;i<m;i++)
		{
			--u[i]; --v[i];
			vector<vector<int>> newparts;
			for(j=0;j<parts.size();j++)
			{
				for(k=0;k<parts[j].size();k++)
					if (parts[j][k]==u[i]) break;
				for(l=0;l<parts[j].size();l++)
					if (parts[j][l]==v[i]) break;
				if (k==parts[j].size() || l==parts[j].size()) 
				{
					newparts.push_back(parts[j]);
					continue;
				}
				if (l<k) swap(k,l);
				x.clear();
				for(q=k;q<=l;q++) x.push_back(parts[j][q]);
				newparts.push_back(x);
				x.clear();
				for(q=0;q<parts[j].size();q++)
				{
					if (q>k && q<l) continue;
					x.push_back(parts[j][q]);
				}
				newparts.push_back(x);
			}
			parts=newparts;
		}

		best=0;
		ans.clear();
		rec(0,n,0,5);
		
		printf("Case #%d: ",test);
		printf("%d\n",best);
		for(i=0;i<ans.size();i++) printf("%d ",ans[i]);
		puts("");
	}

	return 0;
}