#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <cctype>
#include <algorithm>
#include <vector>
#include <numeric>
#include <set>
#include <queue>
#include <map>
#include <list>
#include <string>
#include <iostream>
#include <stack>
#include <sstream>
using namespace std; 
#define PB push_back
#define MP make_pair
#define F first
#define S second 
#define BE(a) a.begin(),a.end() 
#define CLS(a,b) memset(a,b,sizeof(a))
#define SZ(a) ((int)a.size())
const long double pi=acos(-1.0);
#define torad(a) ((a)*pi/180.0)
typedef vector<int> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ; 
typedef pair<int,int> pii ; 
typedef long long ll ; 
typedef long double ld ; 
typedef double dl ; 
class node {public:
int c,a,b;
};
node all[305];
node cur[305];
int cnt;
typedef vector<node> vn ; 
int cases,g;
int n,m;
map<string,int> ind;
int best=500;
int end=10000;
bool cmp(node a,node b)
{
	return a.a<b.a;
}
void solve(int c1,int c2,int c3)
{
	int i,j,k,cbest=0,x,pos;
	m=0;
	for(i=0;i<n;i++)
		if(all[i].c==c1 ||  all[i].c==c2 || all[i].c==c3)
			cur[m++]=all[i];
	i=0;
	x=1;
	while(x<=end && i<m)
	{
		pos=-1;
		for(j=i;j<m && cur[j].a<=x;j++)
			pos=max(pos,cur[j].b);
		if(pos==-1)break;
		i=j;
		cbest++;
		x=pos+1;
	}
	if(x>end)
		best=min(best,cbest);
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
////////////////////////////////////////////
	int i,j,k;
	string color;
	node tmp;
	scanf("%d",&cases);
	for(g=0;g<cases;g++)
	{
		ind.clear();
		best=500;
		scanf("%d",&n);
		cnt=0;
		for(i=0;i<n;i++)
		{
			cin >> color;
			if(ind[color]==0)
			{
				ind[color]=++cnt;
				tmp.c=cnt;
			}
			else
				tmp.c=ind[color];

			scanf("%d%d",&tmp.a,&tmp.b);
			all[i]=tmp;
		}
		sort(all,all+n,cmp);
		for(i=1;i<=cnt;i++)
			for(j=i;j<=cnt;j++)
				for(k=j;k<=cnt;k++)
				{
					solve(i,j,k);
				}

		if(best>n)
			printf("Case #%d: IMPOSSIBLE\n",g+1);
		else
			printf("Case #%d: %d\n",g+1,best);

	}

	return 0;
}