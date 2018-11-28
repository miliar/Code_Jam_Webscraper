#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<algorithm>
#include<queue>
#include<map>
#include<vector>
#include<string>
using namespace std;	

#define sq(a) ((a)*(a))
#define pb(a) push_back(a)
#define Min(a,b) (((a)<(b))?(a):(b))
#define Max(a,b) (((a)>(b))?(a):(b))
#define eps 1e-9
#define inf 1<<29
#define pye 2.*acos(0.)
#define SZ(v) ((int)(v).size())
#define For(i,a,b) for(i=(a);i<(b);++i)
#define Fore(i,a,b) for(i=(a);i<=(b);++i)
#define Forc(i,v) For(i,0,SZ(v))
#define Foro(i,a) For(i,0,a)

map<string,int> mp; 
int n,query[1005],q;
int memo[105][1005];

int make(int now,int pos)
{
	int i,mn=inf;
	if(pos==q)
		return 0;
	if(memo[now][pos]!=-1)
		return memo[now][pos];
	Foro(i,n)
	{
		if(i==now && query[pos]!=now)
			mn=Min(mn,make(now,pos+1));
		else if(query[pos]!=i && i!=now)
			mn=Min(mn,1+make(i,pos+1));
	}
	memo[now][pos]=mn;
	return mn;
}

int main()
{
	int cs,t,i,mn,j;
	string ss;
	char s[105];
	gets(s);
	freopen("out3.txt","w",stdout);
	sscanf(s,"%d",&t);
	Foro(cs,t)
	{
		gets(s);
		mp.clear();
		sscanf(s,"%d",&n);
		Foro(i,n)
			gets(s),ss=s,mp[ss]=i;
		gets(s);
		sscanf(s,"%d",&q);
		Foro(i,q)
			gets(s),ss=s,query[i]=mp[ss];
		mn=inf;
		Foro(i,n+2)
			Foro(j,q+2)
				memo[i][j]=-1;
		Foro(i,n)
			if(i!=query[0])
				mn=Min(mn,make(i,1));
		printf("Case #%d: %d\n",cs+1,mn);
	}
	return 0;
}
