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
#define M			10009

int n,i,v;

struct node
{
	int best0;
	int best1;
	int gate;
	int change;
	
}m[M];

void doit(int x)
{
	int left,right;
	left=2*x;
	right=left+1;
	if(left>n)
		return;
	doit(left);
	doit(right);
	
	//best0
	
	int a,b;
	int z1,z2;
	
	z1=z2=INF;
	
	//z1 and
	//z2 or
	
	a=m[left].best0;
	b=min(m[right].best0,m[right].best1);
	z1=min(z1,a+b);
		
	a=m[right].best0;
	b=min(m[left].best0,m[left].best1);
	z1=min(z1,a+b);
	
	z2=min(z2,m[left].best0+m[right].best0);
	

	//best1
	int z3,z4;
	z3=z4=INF;
	//z3 and
	//z4 or
	
	z3=min(z3,m[left].best1+m[right].best1);
	
	a=m[left].best1;
	b=min(m[right].best0,m[right].best1);
	z4=min(z4,a+b);
	
	a=m[right].best1;
	b=min(m[left].best0,m[left].best1);
	z4=min(z4,a+b);
	
	m[x].best0=m[x].best1=INF;
	if(m[x].gate)
	{
		m[x].best0=min(m[x].best0,z1);
		m[x].best1=min(m[x].best1,z3);
		if(m[x].change)
		{
			m[x].best0=min(m[x].best0,z2+1);
			m[x].best1=min(m[x].best1,z4+1);
		}
	}
	else
	{
		m[x].best0=min(m[x].best0,z2);
		m[x].best1=min(m[x].best1,z4);
		if(m[x].change)
		{
			m[x].best0=min(m[x].best0,z1+1);
			m[x].best1=min(m[x].best1,z3+1);
		}
	}
}

int main()
{
	int t,tc;
	scanf("%d",&tc);
	
	int tmp;
	for(t=1;t<=tc;++t)
	{
		scanf("%d %d",&n,&v);
		
		for(i=1;i<=(n>>1);++i)
		{
			scanf("%d %d",&m[i].gate,&m[i].change);
		}
		for(;i<=n;++i)
		{
			scanf("%d",&tmp);
			if(tmp)
			{
				m[i].best1=0;
				m[i].best0=INF;
			}
			else
			{
				m[i].best0=0;
				m[i].best1=INF;
			}
		}
		
		doit(1);
		int ans;
		if(v)
			ans=m[1].best1;
		else
			ans=m[1].best0;
			
		printf("Case #%d: ",t);
		if(ans>=INF)
			puts("IMPOSSIBLE");
		else
			printf("%d\n",ans);
	}
	return 0;
}
