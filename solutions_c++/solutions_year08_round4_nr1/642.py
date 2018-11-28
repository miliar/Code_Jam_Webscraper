#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream> 
#include <cmath>
#include <cstring>

using namespace std;

#define pb push_back
#define mp make_pair
#define PII pair<int,int> 
#define A first
#define B second
#define PIII pair<int,PII> 

#define I(x,y) x <y> :: iterator 
#define set(a,c) memset(a,c,sizeof(a))

#define REP(i,n) for(int i=0;i<n;i++)

typedef unsigned long long LLU;
typedef long long LL;
typedef long double LD;
int m,v;
int g[10001],c[10001],b[10001];

struct ret{
	int changes;
	int orig_val;
};

ret number[10001];
ret f(int x){
	ret &r = number[x];
	if(r.changes!=-1)
		return r;
	if(x > (m-1)/2)
	{
		if(b[x])
			r.changes=0;
		else
			r.changes = -2;
		r.orig_val = b[x];
		return r;
	}
	if(g[x]){
		ret left = f(2*x),right = f(2*x+1);
		r.orig_val=left.orig_val&&right.orig_val;
		if(r.orig_val==1)
		{
			r.changes=0;
			return r;
		}
		int cc=10000000,cn=1000000;
		if(left.changes==-2 && right.changes==-2)
			r.changes = -2;
		else if(c[x])
		{
			if(left.changes==-2)
				r.changes = right.changes +1;
			else if(right.changes==-2)
				r.changes = left.changes +1;
			else
				r.changes = min(min(left.changes,right.changes)+1,(left.changes+right.changes));
		}
		else if(left.changes==-2 || right.changes==-2)
			r.changes = -2;
		else
			r.changes = left.changes+ right.changes ;
		return r;
	}

		ret left = f(2*x),right = f(2*x+1);
		r.orig_val=left.orig_val||right.orig_val;
		if(r.orig_val==1)
		{
			r.changes=0;
			return r;
		}
		if(left.changes==-2 && right.changes==-2)
			r.changes = -2;
		else if(left.changes==-2)
			r.changes = right.changes;
		else if(right.changes ==-2)
			r.changes = left.changes;
		else
			r.changes = min(left.changes, right.changes);
		return r;
}

ret h(int x){
	ret &r = number[x];
	if(r.changes!=-1)
		return r;
	if(x > (m-1)/2)
	{
		if(!b[x])
			r.changes=0;
		else
			r.changes = -2;
		r.orig_val = b[x];
		return r;
	}
	if(!g[x]){
		ret left = h(2*x),right = h(2*x+1);
		r.orig_val=left.orig_val||right.orig_val;
		if(r.orig_val==0)
		{
			r.changes=0;
			return r;
		}
		if(left.changes==-2 && right.changes==-2)
			r.changes = -2;
		else if(c[x])
		{
			if(left.changes==-2)
				r.changes = right.changes +1;
			else if(right.changes==-2)
				r.changes = left.changes +1;
			else
				r.changes = min(min(left.changes,right.changes)+1,(left.changes+right.changes));
		}
		else if(left.changes==-2 || right.changes==-2)
			r.changes = -2;
		else
			r.changes = left.changes+ right.changes ;
		return r;
	}

		ret left = h(2*x),right = h(2*x+1);
		r.orig_val=left.orig_val&&right.orig_val;
		if(r.orig_val==0)
		{
			r.changes=0;
			return r;
		}
		if(left.changes==-2 && right.changes==-2)
			r.changes = -2;
		else if(left.changes==-2)
			r.changes = right.changes;
		else if(right.changes ==-2)
			r.changes = left.changes;
		else
			r.changes = min(left.changes, right.changes);
		return r;
}

int main()
{
	int KASES;
	scanf("%d",&KASES);
	for(int kases=0;kases<KASES;kases++)
	{
		set(number,-1);
		printf("Case #%d: ",kases+1);
		scanf("%d %d",&m,&v);
		for(int i=1;i<=(m-1)/2;i++)
			scanf("%d %d",&g[i],&c[i]);

		for(int i=1;i<=(m+1)/2;i++)
			scanf("%d",&b[i+(m-1)/2]);
		
		int answer;
		if(v==0)
			answer=h(1).changes;
		else
			answer= f(1).changes;
		if(answer==-2)
			printf("IMPOSSIBLE\n");
		else printf("%d\n",answer);
	}
}

