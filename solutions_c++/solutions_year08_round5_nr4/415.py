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

long long mem[200][200];

#define mod 10007LL

int dx[] = {2,1};
int dy[] = {1,2};


int main()
{
       freopen("input", "r", stdin);
       freopen("output.txt", "w", stdout);

	   int T;
	   cin>>T;

	   REP(test, T)
	   {
			memset(mem, 0, sizeof(mem));
			int w, h, r;
			cin>>h>>w>>r;
			REP(i, r)
			{
				int x,y;
				cin>>x>>y;
				mem[x][y] = -1;
			}

			mem[1][1] = 1;
			FOR(i,1,h+1)
				FOR(j,1,w+1)
					if(mem[i][j] != -1)
					{
						REP(k,2)
						{
							int nx = i + dx[k], ny = j + dy[k];
							if (nx <= h && ny <= w)
							{
								if (mem[nx][ny] == -1)continue;
								mem[nx][ny] += mem[i][j], mem[nx][ny] %= mod;
							}
						}
					}

			long long res = mem[h][w];

		   cout<<"Case #"<<test+1<<": "<<res<<endl;
	   }
       
       return 0;
}
