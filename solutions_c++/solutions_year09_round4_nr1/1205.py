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
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>

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
#define INF			0x3f3f3f3f
#define M			105

int r[M];



bool OK(vector<int> p)
{
	int i;
	TR(i,p)
		if(r[p[i]]>i)
			return false;
	return true;
}

int fun(vector<int> p)
{
	map< vector<int> , int > seen;
	
	queue< vector<int> > q;
	q.push(p);
	
	seen[p]=0;
	
	while(q.empty()==false)
	{
		vector<int> now=q.front();
		q.pop();
		
		if(OK(now))
			return seen[now];
			
		int dist=seen[now]+1;
		int i;
		for(i=1;i<SZ(now);++i)
		{
			vector<int> next=now;
			swap(next[i],next[i-1]);
			if(seen.find(next)==seen.end())
			{
				q.push(next);
				seen[next]=dist;
			}
		}
	}
	return INF;
}

int main()
{
	int t,tc;
	int n;
	scanf("%d",&tc);
	for(t=1;t<=tc;++t)
	{
		scanf("%d",&n);
		int i,j;
		char a[M][M];
		for(i=0;i<n;++i)
		{
			scanf("%s",a[i]);
			int len=strlen(a[i]);
			r[i]=0;
			for(j=0;j<len;++j)
				if(a[i][j]=='1')
					r[i]=j;
		}
		int ans=INF;
		
		vector<int> p(n);
		TR(i,p)
			p[i]=i;
		ans=fun(p);
		assert(ans<INF);
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
