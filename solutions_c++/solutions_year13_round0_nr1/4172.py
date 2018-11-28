#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <cmath>
#include <queue>

using namespace std;

#define MAX 1001
#define INF 10000000000000
#define MOD 1000000009
#define CLR(a,x) memset(a,x,sizeof a)
#define ll long long
#define ALL(v) v.begin(),v.end()
#define FR(i,n) for(ll i=0;i<n;i++)
#define FAB(i,a,b) for(ll i=a;i<b;i++)
#define FBA(i,b,a) for(ll i=b;i>=a;i--)
#define IIN(x) scanf("%d",&x)
#define IIN2(x,y) scanf("%d%d",&x,&y)
#define LIN(x) scanf("%I64d",&x)
#define LIN2(x,y) scanf("%I64d%I64d",&x,&y)
#define PII pair<int,int>
#define PI 3.141592653589793238
#define VI vector<int>
#define VLL vector<ll>
#define VS vector<string>
#define SI set<int>
#define SLL set<ll>
#define SS set<string>
#define MII map<int,int>
#define MIV map<int,VI>
#define MSI map<string,int>
#define MIS map<int,string>
#define PLL pair<ll,ll>

string mat[4];
bool all;

bool O()
{
	bool d1=true, d2=true;
	FR(i,4)
	{
		if(find(mat[i].begin(),mat[i].end(),'X')==mat[i].end() && find(mat[i].begin(),mat[i].end(),'.')==mat[i].end())
			return true;
		if(mat[i][i]=='X' || mat[i][i]=='.') d1=false;
		if(mat[i][3-i]=='X' || mat[i][3-i]=='.') d2=false;
	}
	if(d1 || d2) return true;

	FR(i,4)
	{
		bool f=true;
		FR(j,4)
		{
			if(mat[j][i]=='X' || mat[j][i]=='.') f=false;
			if(mat[j][i]=='.') all=false;
		}
		if(f) return true;
	}
	return false;
}

bool X()
{
	bool d1=true, d2=true;
	FR(i,4)
	{
		if(find(mat[i].begin(),mat[i].end(),'O')==mat[i].end() && find(mat[i].begin(),mat[i].end(),'.')==mat[i].end())
			return true;
		if(mat[i][i]=='O' || mat[i][i]=='.') d1=false;
		if(mat[i][3-i]=='O' || mat[i][3-i]=='.') d2=false;
	}
	if(d1 || d2) return true;

	FR(i,4)
	{
		bool f=true;
		FR(j,4)
		{
			if(mat[j][i]=='O' || mat[j][i]=='.') 
				f=false;
		}
		if(f) return true;
	}
	return false;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int t; cin>>t;
	FR(q,t)
	{
		all=true;
		FR(i,4) cin>>mat[i];
		printf("Case #%d: ",q+1);
		if(O())			printf("O won\n");
		else if(X())	printf("X won\n");
		else if(!all)	printf("Game has not completed\n");
		else			printf("Draw\n");
	}

	return 0;
}