/*
 * b.cpp
 * Another buggy code by mostafa_saad
 *
 *  Created on: Sep 3, 2009
 */


#include<set>
#include<map>
#include<list>
#include<iomanip>
#include<cmath>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<complex>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<stdio.h>
using namespace std;

#define all(v)				((v).begin()), ((v).end())
#define sz(v)				((int)((v).size()))
#define clr(v, d)			memset(v, d, sizeof(v))
#define repi(i, j, n) 		for(int i=(j);i<(int)(n);++i)
#define repd(i, j, n) 		for(int i=(j);i>=(int)(n);--i)
#define repa(v)				repi(i, 0, sz(v)) repi(j, 0, sz(v[i]))
#define rep(i, v)			repi(i, 0, sz(v))
#define lp(i, cnt)			repi(i, 0, cnt)
#define lpi(i, s, cnt)		repi(i, s, cnt)
#define P(x)				cout<<#x<<" = { "<<x<<" }\n"
#define pb					push_back
#define MP					make_pair

typedef vector<int>       vi;
typedef vector<double>    vd;
typedef vector< vi >      vvi;
typedef vector< vd >      vvd;
typedef vector<string>    vs;
typedef long long         ll;
typedef long double   	  ld;

const int OO = (int)1e8;	//Small -> WRONG, Large -> OVERFLOW

const double PI  = acos(-1.0);
const double EPS = (1e-7);

int dcmp(double x, double y) {	return fabs(x-y) <= EPS ? 0 : x < y ? -1 : 1;	}

int vis[150][150];
int grid[150][150];

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

int main()
{
	freopen("bl.in", "rt", stdin);
	freopen("bl.out", "wt", stdout);
	int cases;

	cin>>cases;
	lp(cc, cases) {
		int h, w;
		cin>>h>>w;
		clr(vis, -1);

		lp(i, h) lp(j, w)
			cin>>grid[i][j];

		int compId = 0;

		lp(i, h) lp(j, w) if(vis[i][j] == -1) {
			int color = compId++;

			int curi = i, curj = j;

			vector< pair<int, int> > v;

			while(true) {
				v.push_back( make_pair(curi, curj));

				int nxti = -1, nxtj = -1, val = -1;
				lp(d, 4) {
					int ni = curi+dx[d], nj = curj+dy[d];
					if(ni >= 0 && ni < h && nj >= 0 && nj < w && grid[curi][curj] > grid[ni][nj]) {
						if(val == -1 || val > grid[ni][nj]) {
							val = grid[ni][nj], nxti = ni, nxtj = nj;
						}
					}
				}
				if(val == -1)	break;
				if(vis[nxti][nxtj] != -1) {
					color = vis[nxti][nxtj];
					compId--;
					break;
				}
				curi = nxti, curj = nxtj;
			}
			rep(i, v)	vis[v[i].first][v[i].second] = color;
		}
		cout<<"Case #"<<cc+1<<":\n";
		lp(i, h) {
			lp(j, w) {
				if(j)	cout<<" ";
				cout<<(char)(vis[i][j]+'a');
			}
			cout<<"\n";
		}
	}

	return 0;
}
