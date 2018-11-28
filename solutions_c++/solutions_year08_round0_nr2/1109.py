// gcd_b.cpp : Defines the entry point for the console application.
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

const int inf=60000;
 
int main()
{
	FILE * f=freopen("q.in","r",stdin);
	FILE * g=freopen("q.out","w",stdout);
	int n[2],t,m,h,u,ans[2],s,kil,v;
	PII a[2][120];
	scanf("%d",&kil);
	rep(tc,kil)
	{
		scanf("%d %d %d",&t,&n[0],&n[1]);
		rep(i,n[0])
		{
			scanf("%d:%d",&h,&m); a[0][i].X=h*60+m;
			scanf("%d:%d",&h,&m); a[0][i].Y=h*60+m+t;
		}

		rep(i,n[1])
		{
			scanf("%d:%d",&h,&m); a[1][i].X=h*60+m;
			scanf("%d:%d",&h,&m); a[1][i].Y=h*60+m+t;
		}
		/*printf("First:\n");
		rep(i,n[0]) printf("%d %d\n",a[0][i].X,a[0][i].Y);
		printf("Second:\n");
		rep(i,n[1]) printf("%d %d\n",a[1][i].X,a[1][i].Y);*/

		ans[0]=ans[1]=0;
		do
		{
			t=-1; 
			rep(i,n[0]) 
				if (a[0][i].X<inf)
				{
					if (t == -1) t=i, u=0;
					if (a[0][i].X<a[u][t].X) t=i, u=0;
				};
			rep(i,n[1]) 
				if (a[1][i].X<inf)
				{
					if (t == -1) t=i, u=1;
					if (a[1][i].X<a[u][t].X) t=i, u=1;
				}

		 if (t != -1)
		 {
			// printf("%d %d %d %d > ",u,t,a[u][t].X,a[u][t].Y);
			 ans[u]++;
			 a[u][t].X=inf;
			 do
			 {
				 s=-1;
				 v=u;
				 u=1-u;
				 rep(i,n[u])
					 if (a[u][i].X<inf && a[u][i].X>=a[v][t].Y)
					 {
						 if (s == -1) s=i;
						 if (a[u][i].X < a[u][s].X || (a[u][i].X == a[u][s].X && a[u][i].Y<a[u][s].Y) ) s=i;
					 }
				 if (s != -1)
				 {
					// printf("%d %d %d %d > ",u,s,a[u][s].X,a[u][s].Y);
					 a[u][s].X=inf;
					 t=s;
				 }
			 } while (s != -1);
			// printf("\n");
		 }
			
		} while (t != -1);
		printf("Case #%d: %d %d\n",tc+1,ans[0],ans[1]);
	}

	fclose(f); fclose(g);
	return 0;
}

