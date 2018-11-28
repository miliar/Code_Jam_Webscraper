#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <bitset>
#include <string>
#include <vector>
#include <algorithm>
#include <ctime>
#include <queue>
#include <cstring>
#include <set>
#include <map>
#include <sstream>
#include <cmath>
#include <fstream>
#include <list>
using namespace std;
#define rp(i,n) for(int (i)=0;(i)<(n);++(i))
#define pb push_back
#define L(s) (int)s.size()
#define mp make_pair
#define pii pair<int,int>
#define x first 
#define y second
#define inf 1000000000
#define VI vector<int>
#define ll long long
#define all(s) (s).begin(),(s).end()
#define C(u) memset((u),0,sizeof((u)))
#define ull unsigned ll
#define uint unsigned int
int tests;
pair< pair<double,double> ,double > a[4111];
int n;
double s,r,l,t;
inline bool cmp(const pair<pair<double,double>,double> &a, const pair<pair<double,double>,double> &b)
{
	return a.y<b.y;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>tests;
	for(int test=1;test<=tests;++test)
	{
		cerr<<test<<endl;
		cin>>l>>s>>r>>t>>n;
		rp(i,n)
			cin>>a[i].x.x>>a[i].x.y>>a[i].y;
		a[n++]=mp(mp(l,l),0);
		sort(a,a+n);
		int m=n;
		double prev=0;
		rp(i,n)
		{
			if (a[i].x.x>prev)
				a[m++]=mp(mp(prev,a[i].x.x),0);
			prev=a[i].x.y;
		}

		n=m;
		sort(a,a+n,cmp);
		double ans=0;
		rp(i,n)
		{
			double len=a[i].x.y-a[i].x.x;
			double sp=a[i].y;
			if (t*(sp+r)>=len)
			{
				ans+=len/(sp+r);
				t-=(len/(sp+r));
			}
			else
			{
				ans+=t+(len-t*(sp+r))/(sp+s);
				t=0;
			}
		}
		cout<<"Case #"<<test<<": ";
		printf("%0.9lf\n",ans);
	}
}
