// gcj_a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <deque>
#include <string>
#include <cmath>
#include <map>
#include <algorithm>

using namespace std;

#define rep(i,n) for(int i=0; i<n; i++)
#define pb(z) push_back(z)
#define forr(i,a,b) for(int i=a; i<=b; i++)
#define ford(i,a,b) for(int i=a; i>=b; i--)
#define mset(a,b) memset(a,b,sizeof(a))
#define sz size
#define min(a,b) (a<b ? a : b) 
#define max(a,b) (a<b ? b : a)
#define sqr(a) a*a
#define X first
#define Y second
#define all(A) A.begin,A.end

typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef pair<int,int> PII;
typedef long long i64;
typedef vector<string> VS; 

string s[1000],st;
int f[1000];
char temp[1000];


int main()
{
	FILE * fin = freopen("q.in","r",stdin);
	FILE * fout = freopen("q.out","w",stdout);
	int kil,n,k,t,g;
	scanf("%d",&kil);
	int ans;
	rep(tc,kil)
	{
		scanf("%d\n",&n);

		rep(i,n)
		{
			gets(temp);
			s[i]=string(temp);
		}
		ans=0;
		mset(f,0);
		scanf("%d\n",&k);
		rep(u,k)
		{
			gets(temp);
			st=string(temp);
			rep(i,n) if ( !f[i] && s[i].sz()==st.sz())
			{
				t=0;
				while (t<st.sz() && s[i][t]==st[t]) t++;
				if (t==st.sz()) f[i]=2;
			}
			g=0;
			rep(i,n) if (!f[i]) { g=1; break; }
			if (g) {rep(i,n) if (f[i]) f[i]=1;}
			else { rep(i,n) f[i]--; ans++; }			
		}
		printf("Case #%d: %d\n",tc+1,ans);
	}
	fclose(fin); fclose(fout);
	return 0;
}

