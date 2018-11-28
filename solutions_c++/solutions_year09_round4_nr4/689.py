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
struct cir
{
	double x,y,r;
};
int a,b,c,d,i,j,n,m,k,kolt;
cir mas[3],mas1[3];
double ans;
int main()
{
	freopen("D-small.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>kolt;
	rep(hod,kolt)
	{
		printf("Case #%d: ",hod);
		cin>>n;
		ans=0.0;
		rept(i,n)
		{
			cin>>mas[i].x>>mas[i].y>>mas[i].r;
			ans=max(ans,mas[i].r);
		}
		if (n<=2)
		{
			printf("%.9lf\n",ans);
			continue;
		}
		ans=INF;
		rept(i,3) mas1[i]=mas[i];
		rept(i,8)
		{
			int a=0;
			if (i&1) a++;
			if (i&2) a++;
			if (i&4) a++;
			if (a!=1) continue;
			double rz=0.0;
			rept(j,3)
			{
				if (i&1<<j) 
				{
					rz=mas[j].r;
					swap(mas[j],mas[2]);
					break;
				}
			}
			double rr=D(mas[0],mas[1]);
			rr+=mas[0].r;
			rr+=mas[1].r;
			rr/=2.0;
			rz=max(rz,rr);
			ans=min(ans,rz);
			rept(j,3) mas[j]=mas1[j];
		}
		printf("%.9lf\n",ans);
	}
}
