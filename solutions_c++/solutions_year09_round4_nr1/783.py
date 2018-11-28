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
int a,b,c,d,i,j,n,m,k,kolt,res;
char str[101];
VI cur;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&kolt);
	rep(hod,kolt)
	{
		scanf("%d",&n);
		cur.clear();
		rept(i,n)
		{
			scanf("%s",&str);
			a=0;
			rept(j,n)
			{
				if (str[j]=='1') a=j;
			}
			cur.pb(a);
		}
		res=0;
		rept(i,L(cur))
		{
			if (cur[i]<=i) continue;
			a=0;
			FOR(j,i+1,L(cur)-1)
			{
				if (cur[j]<=i)
				{
					a=j;
					break;
				}
			}
			while (a>i)
			{
				swap(cur[a],cur[a-1]);
				a--;
				res++;
			}
		}
		printf("Case #%d: %d\n",hod,res);
	}
}
