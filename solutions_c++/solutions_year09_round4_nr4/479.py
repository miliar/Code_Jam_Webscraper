#include<Cstdio>
#include<queue>
#include<vector>
#include<stack>
#include<algorithm>
#include<cmath>
#include<Cstring>
#include<string>
#include<memory>
#include<iostream>

using namespace std;

int n;
pair<pair<double,double>,double> a[200],p[2];

double dist(pair<pair<double,double>,double> p1,pair<pair<double,double>,double> p2)
{
	return sqrt((p1.first.first-p2.first.first)*(p1.first.first-p2.first.first)+(p1.first.second-p2.first.second)*(p1.first.second-p2.first.second));
}

void input()
{
	cin >> n;
	for(int i=0;i<n;i++)
	{
		cin >> a[i].first.first >> a[i].first.second >> a[i].second;
	}
}

double process()
{
	double res=99999999;
	for(int i=0;i<n;i++)
	{
		double v=a[i].second;
		int pc=0;
		for(int j=0;j<n;j++)
		{
			if(j==i) continue;
			p[pc++]=a[j];
		}
		if(pc==0);
		else if(pc==1)
			v=max(v,p[0].second);
		else
			v=max(v,(p[0].second+p[1].second+dist(p[0],p[1]))/2);
		if(v<res) res=v;
	}
	return res;
}

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		input();
		printf("Case #%d: %lf\n",i+1,process());
	}
}