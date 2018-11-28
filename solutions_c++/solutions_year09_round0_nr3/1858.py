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
int a,b,c,d,i,j,n,m,k,kolt;
char str[503];
int f[503][31];
const int len=20;
const char tx[30]=" welcome to code jam.";
//const char tx[5]=" wc.";
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	gets(str);
	sscanf(str,"%d",&kolt);
	rep(hod,kolt)
	{
		printf("Case #%d: ",hod);
		gets(str+1);
		n=(int)strlen(str);
		str[n++]='.';
		C(f);
		rept(i,n) f[i][0]=1;
		rep(i,n-1)
		{
			rep(j,len)
			{
				f[i][j]=f[i-1][j];
				if (str[i]==tx[j]) f[i][j]=(f[i][j]+f[i-1][j-1])%10000;
				//if (f[i][len]==2) cerr<<i<<endl;
			}
		}
		a=f[n-1][len];
		if (a<10) printf("000%d\n",a); else
		if (a<100) printf("00%d\n",a); else
		if (a<1000) printf("0%d\n",a); else
		printf("%d\n",a);
	}
}
