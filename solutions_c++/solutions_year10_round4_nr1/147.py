#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cstring>
#pragma comment(linker, "/STACK:16777216")
using namespace std;
#define pb push_back
#define ppb pop_back
#define pi 3.1415926535897932384626433832795028841971
#define mp make_pair
#define x first
#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pii pair<int,int>
#define pdd pair<double,double>
#define INF 1000000000
#define FOR(i,a,b) for (int _n(b), i(a); i <= _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define L(s) (int)((s).size())
#define C(a) memset((a),0,sizeof(a))
#define VI vector <int>
#define ll long long
int a,b,c,d,i,j,n,m,k,kolt;
int mas[101][101];
int len[101];
bool sl[301],sr[301];
inline bool checkl(int cj)
{
	int bj=cj;
	rept(i,n)
	{
		if (!cj) break;
		rept(j,cj)
		{
			if (bj-i>=n || bj-j>=n) continue;
			if (mas[i][j]!=mas[bj-j][bj-i]) return 0;
		}
		--cj;
	}
	return 1;
}
inline bool checkr(int cj)
{
	int bj=cj,bi=n-cj-1;
	FORD(i,n-1,0)
	{
		if (!cj) break;
		rept(j,cj)
		{
			if (bj-n+i+1>=n || bi+j<0) continue;
			if (mas[i][j]!=mas[bi+j][bj-n+i+1]) return 0;
		}
		--cj;
	}
	return 1;
}
inline bool check(int m)
{
	int dd1=m-1,dd2=n-1;
	rept(i,m-n+1)
	{
		int d1=dd1,d2=dd2;
		rept(j,m-n+1)
		{
			bool ok1=0,ok2=0;
			if (d1>=2*n-1 || d1<0) ok1=1; else
			ok1=sl[d1];
			if (d2>=2*n-1 || d2<0) ok2=1; else
			ok2=sr[d2];
			if (ok1 && ok2) return 1;

			--d1; --d2;
		}
		--dd1; ++dd2;
	}
	return 0;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&kolt);
	rep(hod,kolt)
	{
		cerr<<hod<<endl;
		printf("Case #%d: ",hod);
		scanf("%d",&n);
		C(len);
		rept(i,n)
		{
			rept(j,i+1)
			{
				scanf("%d",&a);
				mas[j][len[j]++]=a;
			}
		}
		d=1;
		FOR(i,n,2*n-2)
		{
			c=d; d++;
			rept(j,2*n-i-1)
			{
				scanf("%d",&a);
				mas[c][len[c]++]=a;
				c++;
			}
		}
		/*rept(i,n)
		{
			rept(j,n)
			{
				if (j) cerr<<" ";
				cerr<<mas[i][j];
			}
			cerr<<endl;
		}*/
		C(sl); C(sr);
		rept(h,2*n-1)
		{
			sl[h]=checkl(h);
			sr[h]=checkr(h);
		}
		int l=n;
		while (!check(l))
		{
			++l;
		}
		printf("%d\n",l*l-n*n);
	}
}
