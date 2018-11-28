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
#define sz(x) int((x).size())
#define INF 1000000000
#define FOR(i,a,b) for (int _n(b), i(a); i <= _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define L(s) (int)((s).end()-(s).begin())
#define C(a) memset((a),0,sizeof(a))
#define val(ch) (int)(ch)-(int)('0')
#define toch(a) (char)((int)(a)+(int)('0'))
#define VI vector <int>
#define ll long long
const int di[]={-1,0,0,1};
const int dj[]={0,-1,1,0};
int a,b,c,d,i,j,n,m,k,kolt;
int mas[101][101];
char num[101][101];
char ans[101][101];
inline int v(int ci,int cj)
{
	if (ci<0 || cj<0 || ci>=n || cj>=m) return INF; else
	return mas[ci][cj];
}
inline bool edge(int ci,int cj,int ni,int nj)
{
	if (abs(ci-ni)+abs(cj-nj)!=1) return 0;
	if (ni<0 || nj<0 || ni>=n || nj>=m) return 0;
	if (v(ci,cj)>=v(ni,nj)) return 0;
	int sm=INF;
	int zi=-1,zj=-1;
	rept(l,4)
	{
		int ri=ni+di[l];
		int rj=nj+dj[l];
		if (v(ri,rj)<sm)
		{
			sm=v(ri,rj);
			zi=ri;
			zj=rj;
		}
	}
	if (zi!=ci || zj!=cj) return 0; else
	return 1;
}
void dfs(int ci,int cj,char cur)
{
	if (num[ci][cj]!=-1) return;
	num[ci][cj]=cur;
	rept(l,4)
	{
		int ni=ci+di[l];
		int nj=cj+dj[l];
		if (edge(ci,cj,ni,nj)) 
		{
			dfs(ni,nj,cur);
		}
	}
}
void dfs2(int ci,int cj,char cur)
{
	if (ans[ci][cj]!=-1) return;
	ans[ci][cj]=cur;
	rept(l,4)
	{
		int ni=ci+di[l];
		int nj=cj+dj[l];
		if (ni<0 || nj<0 || ni>=n || nj>=m) continue;
		if (num[ni][nj]==num[ci][cj]) dfs2(ni,nj,cur);
	}
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&kolt);
	rep(hod,kolt)
	{
		scanf("%d%d",&n,&m);
		rept(i,n) rept(j,m) scanf("%d",&mas[i][j]);
		memset(num,-1,sizeof(num));
		memset(ans,-1,sizeof(ans));
		char cur='a';
		printf("Case #%d:\n",hod);
		rept(i,n)
		{
			rept(j,m)
			{
				if (num[i][j]==-1)
				{
					bool ok=1;
					rept(l,4)
					{
						int ci=i+di[l];
						int cj=j+dj[l];
						if (v(ci,cj)<v(i,j))
						{
							ok=0;
							break;
						}
					}
					if (!ok) continue;
					dfs(i,j,cur++);
				}
			}
		}
		cur='a';
		rept(i,n)
		{
			rept(j,m)
			{
				if (ans[i][j]==-1) dfs2(i,j,cur++);
				if (j) printf(" ");
				printf("%c",ans[i][j]);
			}
			printf("\n");
		}
	}
}
