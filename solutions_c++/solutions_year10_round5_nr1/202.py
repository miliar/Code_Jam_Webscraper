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
int a,b,c,d,i,j,n,m,k,kolt,cand;
bool npr[1000001],found;
int pr[1000001];
inline void gen(int n)
{
	k=0;
	C(npr);
	npr[1]=1;
	FOR(i,2,n)
	{
		if (!npr[i])
		{
			pr[k++]=i;
			if ((ll)i*i>n) continue;
			for (int j=i*i;j<=n;j+=i) npr[j]=1;
		}
	}
}
int mas[11];
int gcd (int a, int b, int & x, int & y)
{
	if (a == 0)
	{
		x = 0; y = 1;
		return b;
	}
	int x1, y1;
	int d = gcd (b%a, a, x1, y1);
	x = y1 - (b / a) * x1;
	y = x1;
	return d;
}
inline bool check(int a,int b,int p)
{
	rept(i,n-1)
	{
		int nx=((ll)a*mas[i]+(ll)b)%p;
		if (mas[i+1]!=nx) return 0;
	}
	return 1;
}
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&kolt);
	rep(hod,kolt)
	{
		cerr<<hod<<endl;
		printf("Case #%d: ",hod);
		scanf("%d%d",&d,&n);
		a=1;
		rep(i,d) a*=10;
		gen(a);
		rept(i,n) scanf("%d",&mas[i]);
		if (n==1)
		{
			printf("I don't know.\n");
			continue;
		}
		cand=-1;
		rept(pp,k)
		{
			int p=pr[pp];
			if (p<=mas[0]) continue;
			rept(a,p)
			{
				b=((ll)mas[1]-(ll)a*mas[0]+(ll)p*INF)%p;
				if (check(a,b,p))
				{
					int tcand=((ll)a*mas[n-1]+(ll)b)%p;
					if (cand!=-1 && cand!=tcand)
					{
						cand=INF;
						break;
					}
					cand=tcand;
				}
			}
			if (cand==INF) break;
		}
		if (cand==INF || cand==-1) printf("I don't know.\n"); else
		printf("%d\n",cand);
	}
}
