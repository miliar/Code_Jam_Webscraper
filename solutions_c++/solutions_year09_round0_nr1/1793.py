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
int a,b,c,d,i,j,n,m,k,l;
vector <string> words;
bool ok[16][30];
int main()
{
	freopen("A-small.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>l>>d>>n;
	words.clear();
	rept(i,d)
	{
		string s;
		cin>>s;
		words.pb(s);
	}
	rep(hod,n)
	{
		string s;
		cin>>s;
		//if (!hod) cerr<<s<<endl;
		C(ok);
		a=0;
		b=0;
		while (a<L(s))
		{
			if (s[a]!='(' && s[a]!=')')
			{
				ok[b++][s[a]-'a']=1;
				a++;
			} else
			{
				while (s[a]!=')')
				{
					ok[b][s[a]-'a']=1;
					a++;
				}
				a++;
				b++;
			}
		}
		k=0;
		rept(i,d)
		{
			a=1;
			rept(j,l)
			{
				if (!ok[j][words[i][j]-'a'])
				{
					a=0;
					break;
				}
			}
			k+=a;
		}
		printf("Case #%d: %d\n",hod,k);
	}
}
