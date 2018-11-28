#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <queue>
#include <algorithm>
#include <map>
#include <stack>
#include <vector>
#include <stdlib.h>
#include <cmath>
#include <fstream>
using namespace std;
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
#define INF 0x7f7f7f7f
#define INFL (1LL<<60)
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

struct Node
{
	Node(int b,int e,int s):B(b),E(e),S(s){}
	Node(){}
	friend bool operator < (const Node &a,const Node &b)
	{
		return a.S>b.S;
	}
	int B,E;
	int S;
};
bool cmp(const Node &a,const Node &b)
{
	return a.B<b.B;
}
bool cmp2(const Node &a,const Node &b)
{
	return a.S<b.S;
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int cas = 0;
	int T;
	scanf("%d",&T);
	while(T--)
	{
		int X,S,R,t,N;
		scanf("%d%d%d%d%d",&X,&S,&R,&t,&N);
		vector<Node> SAVE;
		
		for(int i=0;i<N;i++)
		{
			int b,e,w;
			scanf("%d%d%d",&b,&e,&w);
			SAVE.push_back(Node(b,e,w+S));	
		}
		sort(SAVE.begin(),SAVE.end(),cmp);
		int now = 0;
		for(int i=0;i<N;i++)
		{
			if(SAVE[i].B>now)
			{
				SAVE.push_back(Node(now,SAVE[i].B,S));
			}
			now = SAVE[i].E;
		}
		if(SAVE[N-1].E<X)SAVE.push_back(Node(SAVE[N-1].E,X,S));
		sort(SAVE.begin(),SAVE.end(),cmp2);
		vector<double> ADD;
		double left = (double)t;
		for(int i=0;i<SAVE.size();i++)
		{
			int len = SAVE[i].E-SAVE[i].B;
			if(left<=0)
			{
				ADD.push_back((double)len/SAVE[i].S);
				continue;
			}
			int SS;
			if(SAVE[i].S>S)
			{
				SS = R+SAVE[i].S-S; 
			}
			else
			{
				SS = R;
			}
			if(SS*left >= (double)len)
			{
				double cost = (double)len/SS;
				ADD.push_back(cost);
				left -= cost;
			}
			else
			{
				double ll = len - SS*left;
				ADD.push_back(ll/SAVE[i].S+left);
				left = 0;
			}
		}
		double ans = 0;
		for(int i=0;i<SAVE.size();i++)
		{
			ans+=ADD[i];
		}
		printf("Case #%d: %lf\n",++cas,ans);
	}
    return 0;
}
