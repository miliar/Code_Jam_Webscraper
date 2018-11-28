#include "stdafx.h"
  
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


const int SUS=10000;

string ex="welcome to code jam";
int ans[20];
int tc;
char st[520];



int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&tc);
	getchar();
	rep(ti,tc)
	{
		gets(st);
		mset(ans,0);
		int n=strlen(st);
		rep(i,n)
			rep(j,20)
			 if (st[i]==ex[j])
			 {
				 if (j) ans[j]=(ans[j]+ans[j-1])%SUS;
				 else ans[j]++;
			 };;
		printf("Case #%d: %04d\n",ti+1,ans[18]);
	}
	
	
	return 0;
}

