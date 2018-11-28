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

struct tr
{
	int x,y,z;
	tr():x(0),y(0),z(0) {}
	tr(int _x,int _y,int _z):x(_x),y(_y),z(_z) {}
};
int a,b,c,d,i,j,n,m,k,kolt,ans;
char str[3];
pii mas[101];
int dp[101][101][101];
queue<tr> q;

inline void go(tr &t1,tr &t2)
{
	if (t2.y<0 || t2.y>=100 || t2.z<0 || t2.z>=100) return;
	if (t2.x==n)
	{
		ans=min(ans,dp[t1.x][t1.y][t1.z]+1);
		return;
	}

	if (dp[t2.x][t2.y][t2.z]>dp[t1.x][t1.y][t1.z]+1)
	{
		dp[t2.x][t2.y][t2.z]=dp[t1.x][t1.y][t1.z]+1;
		q.push(t2);
	}
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&kolt);
	rep(hod,kolt)
	{
		cerr<<hod<<endl;
		scanf("%d",&n);
		rept(i,n)
		{
			scanf("%s%d",str,&a);
			if (str[0]=='O') mas[i]=mp(0,a-1); else
			mas[i]=mp(1,a-1);
		}
		memset(dp,63,sizeof(dp));
		dp[0][0][0]=0;
		ans=INF;
		q.push(tr(0,0,0));
		
		while (!q.empty())
		{
			tr cur=q.front();
			q.pop();

			go(cur,tr(cur.x,cur.y-1,cur.z));
			go(cur,tr(cur.x,cur.y+1,cur.z));
			go(cur,tr(cur.x,cur.y,cur.z-1));
			go(cur,tr(cur.x,cur.y,cur.z+1));
			go(cur,tr(cur.x,cur.y-1,cur.z-1));
			go(cur,tr(cur.x,cur.y-1,cur.z+1));
			go(cur,tr(cur.x,cur.y+1,cur.z-1));
			go(cur,tr(cur.x,cur.y+1,cur.z+1));

			if (mas[cur.x].x==0 && mas[cur.x].y==cur.y)
			{
				go(cur,tr(cur.x+1,cur.y,cur.z));
				go(cur,tr(cur.x+1,cur.y,cur.z-1));
				go(cur,tr(cur.x+1,cur.y,cur.z+1));
			}

			if (mas[cur.x].x==1 && mas[cur.x].y==cur.z)
			{
				go(cur,tr(cur.x+1,cur.y,cur.z));
				go(cur,tr(cur.x+1,cur.y-1,cur.z));
				go(cur,tr(cur.x+1,cur.y+1,cur.z));
			}
		}

		printf("Case #%d: %d\n",hod,ans);
	}
}
