// Author -Swarnaprakash.U
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

const bool debug=true;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define PB 			push_back
#define SZ(x)		((int)((x).size()))
#define TR(i,x) 	for(i=0;i<(x).size();++i)
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;
#define HELLO		if(debug) puts("hello");
#define LL 			long long
#define INF			100000000
#define M			1005

int s[M];
int rank[M];

void createset(int);
void setunion(int,int);
int findset(int);


vector<int> getv(int n,int p)
{
	int i;
	vector<int> ans;
	for(i=2;i*i<=n;++i)
		if(n%i==0)
		{
			if(i>=p)
				ans.PB(i);
			while(n%i==0)
				n/=i;
		}
	if(n!=1 && n>=p)
		ans.PB(n);
	return ans;
}

int main()
{
	vector<int> v[1005];
	int i,j;
	int t,tc,p;
	int a,b;
	cin>>tc;
	for(t=1;t<=tc;++t)
	{
		cin>>a>>b>>p;
	
	
	for(i=a;i<=b;++i)
	{
		createset(i);
		v[i]=getv(i,p);
		
	}
	
	int x,y;
	
	for(i=a;i<=b;++i)
	{
		
		for(j=a;j<i;++j)
		{
			
			for(x=0;x<v[i].size();++x)
				for(y=0;y<v[j].size();++y)
					if(v[i][x]==v[j][y])
						setunion(i,j);
			
		}
		
	}
	set<int> zz;
	for(i=a;i<=b;++i)
		zz.insert(findset(i));
		printf("Case #%d: %d\n",t,(int)zz.size());
	}
	return 0;
}

void createset(int x)
{
	s[x]=x;
	rank[x]=0;
}

void setunion(int x,int y)
{
	int px,py;
	px=findset(x);
	py=findset(y);

	if(rank[px]>rank[py])
		s[py]=px;
	else
		s[px]=py;
	if(rank[px]==rank[py])
		rank[py]++;
}
int findset(int x)
{
	if(x!=s[x])
		return x=findset(s[x]);
	return s[x];
}


