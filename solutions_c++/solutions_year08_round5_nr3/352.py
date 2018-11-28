#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <list>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define UNIQUE(v) SORT(v),v.erase(unique(v.begin(),v.end()),v.end())
#define INF 2147483647
#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
#define MP(a,b)  make_pair((a), (b))
#define X first
#define Y second
#define CLR(a,v) memset((a),(v),sizeof(a))

typedef pair<int,int> II;
typedef vector<int> VI;
typedef vector<VI > VVI;
typedef vector<II > VII;
template<typename T>
void outV(const vector<T>& v){cout<<endl;REP(i,v.sz)cout<<v[i]<<" ";cout<<endl;}
template<typename T>
void outVV(const vector<vector<T> >& v){cout<<endl;REP(i,v.sz){REP(j, v[i].sz)cout<<v[i][j]<<" ";cout<<endl;}cout<<endl;}
void outVII(const VII& v){cout<<endl;REP(i,v.sz)cout<<"("<<v[i].first<<", "<<v[i].second<<") ";cout<<endl;}
int gcd(int a,int b){return a==0 ? b : gcd(b%a, a);}

int mem[11][2000];


int a[20][20];

int n, m;

int av[20], vav[20];

int go(int h, int mask)
{
	if (mem[h][mask] != -1)
		return mem[h][mask];

	int ret = 0;

	bool fl = true;
	int cnt = 0;
	REP(i, n)
		if (mask & (1<<i))
		{
			if (a[h][i] == 1)
			{
				fl = false;break;
			}
			cnt++;
		}

	if (fl)
	{
		REP(i,n)
			if (mask & (1<<i))
			{
				if (i-1 >= 0 && (mask & (1<<(i-1))))
				{fl = false;break;}
				if (i+1 < n &&  (mask & (1<<(i+1))))
				{fl = false;break;}
			}
		if (fl)
		{
			if (h == 0)
			{
				ret = cnt;
			}
			else
			{
				int wr = 0;
				memset(av, 0, sizeof(av));
				REP(i, n)
					if (mask & (1<<i))
					{
						if (i > 0)
							av[i-1] = 1;
						if (i+1 < n)
							av[i+1] = 1;
					}
				vector<int> vav;
				REP(i, n)
					if (av[i] == 0)
						vav.pb(i);
				if (vav.sz > 0)
				{
					REP(smask, (1<<vav.sz))
					{
						int nmask = 0;
						REP(j, vav.sz)
							if (smask & (1<<j))
								nmask |= (1<<vav[j]);
						int r = go(h-1, nmask);
						if (r != -2)
						{
							int now = r + cnt;
							if (now > ret)
								ret = now;
						}
					}
				}
			}
		}
	}

	if (!fl)
		ret = -2;
	mem[h][mask] = ret;
	return ret;
}


int main()
{
       freopen("input", "r", stdin);
       freopen("output.txt", "w", stdout);

	   int T;
	   cin>>T;

	   REP(test, T)
	   {
			memset(mem, -1, sizeof(mem));
			memset(a, 0, sizeof(a));
			cin>>m>>n;
			REP(i, m)
			{
				string str;
				cin>>str;
				REP(j, n)
					if (str[j] == 'x')
						a[i][j] = 1;
			}

			int res = 0;

			/*REP(mask1, (1<<n))
			{
				int now = go(m - 1, mask1);
				if (now>res)
					res = now;
			}*/

			REP(i, m)
				REP(mask, (1<<n))
			{
				int now = go(i, mask);
				if (now > res)
					res = now;
			}

		   cout<<"Case #"<<test+1<<": "<<res<<endl;
	   }
       
       return 0;
}
