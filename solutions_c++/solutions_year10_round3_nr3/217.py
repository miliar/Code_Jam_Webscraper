#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <cstring>
#include <ctime>
using namespace std;
#define pb push_back
#define INF 1000000000
#define L(s) (int)((s).end()-(s).begin())
#define FOR(i,a,b) for (int _n(b), i(a); i <= _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define C(a) memset((a),0,sizeof(a))
#define llint long long
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define VI vector<int>
#define ppb pop_back
#define mp make_pair
#define pii pair<int,int>
#define pdd pair<double,double>
#define x first
#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pi 3.1415926535897932384626433832795028841971
#define tt (ll+rr)/2
#define rnd() ((rand() << 16) ^ rand())

int bits(char c)
{
	if (c <= '9') return c - '0';
	else		  return c - 'A' + 10;
}

string s[2048];
int a[2048][2048], used[2048][2048];

int main()
{
	freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);
	
	int tc, TC;
	cin >> TC;
	rep(tc, TC)
	{
		int n, m;
		map<int,int> mc;
		scanf("%d%d",&n, &m);
		rept(i, n)
			cin >> s[i];
		memset(used,0,sizeof(used));
		memset(a,0,sizeof(a));
		rept(i, n)
			rept(j, m)
			{
				int w =  bits(s[i][j / 4]);
				w = w >> (3 - j % 4);
				w = w & 1;
				a[i][j] = w;
			}
		cerr << tc << endl;
	/*	rept(i,n)
		{
			rept(j,n)
			printf("%d",a[i][j]);
			puts("");
		}
		*/
		for (int h = min(n, m); h > 0; h--)
		{
			rept(i, n)
				rept(j, m)
				{
					bool fl = true;
					for (int k = 0; k < h && fl; k++)
						for (int t = 0; t < h && fl; t++)
						{
							if (used[i + k][j + t])
							{
								fl = false;
							}
							if ((i + k + j + t) % 2 == (i + j) % 2) 
							{
								if (a[i + k][j + t] != a[i][j]) fl = false; 
							} 
							else
							{
								if (a[i + k][j + t] == a[i][j]) fl = false;
							}
						}
					if (fl)
					{
						rept(k, h)
							rept(t, h)
								used[i + k][j + t] = true;
						mc[h]++;
					}
				}
		}
		printf("Case #%d: ",tc);
		printf("%d\n", mc.size());
		vector<pii> v;
		for (map<int,int>::iterator it = mc.begin(); it != mc.end(); it++)
		{
			v.push_back(mp(it->first, it->second));
			
		}
		reverse(all(v));
		rept(i, v.size())
			printf("%d %d\n", v[i].x, v[i].y);
	}
	
	return 0;
}






