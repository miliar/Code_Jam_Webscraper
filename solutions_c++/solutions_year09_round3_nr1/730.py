 
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <list>
#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <algorithm>
using namespace std;

#define rep(i,n) for(int i=0; i<n; i++)
#define forr(i,a,b) for (int i=a; i<=b; i++)
#define ford(i,a,b) for (int i=a; i>=b; i--)
#define mset(a,b) memset(a,b,sizeof(a))
#define sz(a) int( a.size() )
#define all(A) A.begin(),A.end()
#define sqr(q) q*q
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define X first
#define Y second

typedef long long i64;
typedef vector<int> VI;
typedef vector< VI > VVI;
typedef pair<int,int> PII;
typedef vector<string> VS;


string st;
i64 ans;

map<char,int> cod;

void done()
{
	cod.clear();
	bool f=0;
	int n=sz(st);
	int t=0;
	int d[500];
	rep(i,n)
	{
		char ch=st[i];
		if ( cod.count(ch) == 0)
		{
			if (f) 
			{
				cod[ch]=t;
				t++;
				if (t==1) t++;				
			} else
			{
				cod[ch]=1;
				f=1;
			}
		}
	}
	if (t==0) t=2;
	rep(i,n)
		d[i]=cod[ st[i] ];
	i64 b=1; ans=0;
	ford(i,n-1,0)
	{
		ans+=(i64)d[i] * b;
		b*=(i64)t;
	}	
}

int main()
{
	freopen("q.in","r",stdin);
	freopen("q.out","w",stdout);
	int test;
	scanf("%d",&test); getchar();
	char temp[500];
	rep(i,test)
	{
		gets(temp);
		st=string(temp);
		done();
		printf("Case #%d: %I64d\n",i+1,ans);
	}
	
	return 0;
}

