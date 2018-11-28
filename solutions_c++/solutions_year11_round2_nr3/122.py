#pragma comment(linker,"/STACK:256000000")
#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <math.h>
#include <set>
#include <map>
using namespace std;

vector<vector<int>> home;
int f(vector<int> &d, int k,int pr)
{
	if(d.size()==k)
	{
		int ye=1;
		for(int i=0;i<home.size();i++)
		{
			vector<int> yes(pr);
			int ys=1;
			for(int j=0;j<home[i].size();j++)
				yes[d[home[i][j]]]=1;
			for(int j=0;j<pr;j++)
				if(yes[j]==0)
				{
					ys=0;
					break;
				}
			if(ys==0)
			{
				ye=0;
				break;
			}
		}
		if(ye)
				return 1;
	}
	else
	{
		for(int i=0;i<pr;i++)
		{
			d[k]=i;
			if(f(d,k+1,pr)==1)
				return 1;
		}
	}
	return 0;
}
			
			




int main()
{
	//freopen("1.txt","rt",stdin);
	freopen("C-small-attempt0.in","rt",stdin);
	//freopen("C-large.in","rt",stdin);
	freopen("OutSmallC.txt","wt",stdout);
	//freopen("OutLargeC.txt","wt",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int n,m;
		cin>>n>>m;
		vector<int> u(m);
		vector<int> v(m);
		for(int j=0;j<m;j++)
		{
			cin>>u[j];
			u[j]--;
		}
		for(int j=0;j<m;j++)
		{
			cin>>v[j];
			v[j]--;
		}
		home.clear();
		vector<int> s(n);
		for(int j=0;j<n;j++)
			s[j]=j;
		home.push_back(s);
		for(int j=0;j<m;j++)
		{
			
			for(int k=0;k<home.size();k++)
			{
				int y1=0,y2=0;
				for(int p=0;p<home[k].size();p++)
				{
					if(home[k][p]==v[j]) y1=1;
					if(home[k][p]==u[j]) y2=1;
				}
				if(y1 && y2)
				{
					int v1=v[j];
					int u1=u[j];
					if(u1<v1) swap(v1,u1);
					for(int p=0;p<home[k].size();p++)
					{
						if(home[k][p]==v1) y1=p;
						if(home[k][p]==u1) y2=p;
					}
					vector<int> s1;
					vector<int> s2;
					for(int p=0;p<home[k].size();p++)
					{
						if(p>=y1 && p<=y2) s1.push_back(home[k][p]);
						if(p<=y1 || p>=y2) s2.push_back(home[k][p]);
					}
					home.push_back(s1);
					home.push_back(s2);
					home.erase(home.begin()+k,home.begin()+k+1);
					break;
				}
			}
		}
		int max=10;
		for(int j=0;j<home.size();j++)
			if(max>home[j].size()) max=home[j].size();
		vector<int> d(n);
		vector<int> res;
		int mi=0;
		for(int j=2;j<=max;j++)
			if(f(d,0,j)==1)
			{
				res=d;
				mi=j;
			}
		printf("Case #%d: %d\n",i,mi);
		for(int j=0;j<res.size();j++)
		{
			if(j!=0) printf(" ");
			printf("%d",res[j]+1);
		}
		printf("\n");
		
	}

					


	





			



fclose(stdout);
}