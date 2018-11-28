#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <string>
#include <iostream>
#include <queue>
#include <cmath>
#include <set>
#include <memory.h>

using namespace std;

bool equal(int a,int b)
{
	if (a==b||a==-1||b==-1) return true;
	return false;
}

bool hor_sym(int n,vector < vector <int> > d)
{
	bool ans=true;
	for(int i=1;i<2*n;i++)
	{
		int ci=d[i-1].size();
		for(int j=0;j<ci;j++)
			if (equal(d[i-1][j],d[i-1][ci-1-j])==false) ans=false;
	}
	return ans;
}

bool ver_sym(int n,vector < vector <int> > d)
{
	bool ans=true;
	for(int i=1;i<2*n;i++)
	{
		int ci=d[i-1].size();
		for(int j=0;j<ci;j++)
			if (equal(d[i-1][j],d[2*n-i-1][j])==false) ans=false;
	}
	return ans;
}

int main()
{
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	ifstream dat("input.txt");
	ofstream sol("output.txt");
	int T;
	dat >> T;
	for(int t=1;t<=T;t++)
	{
		int n,n2,sn,ans=0;
		dat >> n;
		n2=n; sn=n;
		vector <vector <int> > diam(2*n-1,vector <int>()),diam2;
		for(int i=1;i<=n;i++)
			for(int j=0;j<i;j++)
			{
				int a;
				dat >> a;
				diam[i-1].push_back(a);
			}
		for(int i=n+1;i<2*n;i++)
		{
			for(int j=0;j<2*n-i;j++)
			{
				int a;
				dat >> a;
				diam[i-1].push_back(a);
			}
		}
//		sol << hor_sym(n,diam) << "	" << ver_sym(n,diam) << endl;
		diam2=diam; sn=n;
		int l1=0,l2=0,l3=0,l4=0;
		while(true)
		{
			if (hor_sym(n,diam)) break;
			for(int i=1;i<2*n;i++)
				diam[i-1].push_back(-1);
			diam.insert(diam.begin(),vector <int>(1,-1));
			diam.push_back(vector <int>(1,-1));
			l1++,n++;
		}
		n=sn; diam=diam2;
		while(true)
		{
			if (ver_sym(n,diam)) break;
			for(int i=n+1;i<2*n;i++)
			{
				diam[i-1].push_back(-1);
				diam[i-1].insert(diam[i-1].begin(),-1);
			}
			diam.push_back(vector <int>(2,-1));
			diam.push_back(vector <int>(1,-1));
			l2++,n++;
		}
		n=sn; diam=diam2;
		while(true)
		{
			if (hor_sym(n,diam)) break;
			for(int i=1;i<2*n;i++)
				diam[i-1].insert(diam[i-1].begin(),-1);
			diam.insert(diam.begin(),vector <int>(1,-1));
			diam.push_back(vector <int>(1,-1));
			l3++,n++;
		}
		n=sn; diam=diam2;
		while(true)
		{
			if (ver_sym(n,diam)) break;
			for(int i=1;i<n;i++)
			{
				diam[i-1].push_back(-1);
				diam[i-1].insert(diam[i-1].begin(),-1);
			}
			diam.insert(diam.begin(),vector <int>(2,-1));
			diam.insert(diam.begin(),vector <int>(1,-1));
			l4++,n++;
		}
		ans=(sn+min(l1,l3)+min(l2,l4))*(sn+min(l1,l3)+min(l2,l4))-sn*sn;
		sol << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}

