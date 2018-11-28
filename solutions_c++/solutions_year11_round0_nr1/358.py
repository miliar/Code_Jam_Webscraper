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
#define pdd pair<double,double>
int t,n;
vector< pii > a;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	rp(num,t)
	{
		cin>>n;
		a.clear();
		rp(i,n)
		{
			char ch;
			int x;
			cin>>ch>>x;
			if (ch=='O')
				a.pb(mp(0,--x));
			else
				a.pb(mp(1,--x));
		}
		int ci=0,cj=0,ans=0,pi=0,pj=0;
		while(pi<n && a[pi].x!=0)
			++pi;
		while(pj<n && a[pj].x!=1)
			++pj;
		while(pi<n || pj<n)
		{
			ans++;
			if (pi<pj)
			{
				if (ci==a[pi].y)
				{
					++pi;
					while(pi<n && a[pi].x!=0)
						++pi;
				}
				else
					ci+=(a[pi].y-ci)/abs(a[pi].y-ci);
				if (pj!=n && cj!=a[pj].y)
					cj+=(a[pj].y-cj)/abs(a[pj].y-cj);
			}
			else
			{
				if (cj==a[pj].y)
				{
					++pj;
					while(pj<n && a[pj].x!=1)
						++pj;
				}
				else
					cj+=(a[pj].y-cj)/abs(a[pj].y-cj);
				if (pi!=n && ci!=a[pi].y)
					ci+=(a[pi].y-ci)/abs(a[pi].y-ci);
			}
		}
		printf("Case #%d: %d\n",num+1,ans);
	}
}