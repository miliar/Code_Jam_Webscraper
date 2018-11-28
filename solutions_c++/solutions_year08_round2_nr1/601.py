#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <set>
#include <cmath>
#include <queue>
#include <sstream>
#include <iostream>
using namespace std;
#define sqr(a) (a)*(a)
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define sz(a) (a).size()
#define mset(a,v) memset(a, v, sizeof(a))
#define pb push_back 
#define updateMIN(a, x) if(a > x)a = x 
#define updateMAX(a, x) if(a < x)a = x 
typedef long long ll;
typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string> VS;
#define TEST 100


int main()
{
	int K, k;
	freopen("A-small-attempt2.in", "rt", stdin);
	freopen("output.out", "wt", stdout);
    scanf("%d", &K);
	for(k = 0 ; k < K ; ++k)
	{
		int n, A, B, C, D, x0, y0, M;
		scanf("%d %d %d %d %d", &n, &A, &B, &C, &D);
		scanf("%d %d %d", &x0, &y0, &M);
		vector< pair<ll, ll> > trees;
		trees.pb(make_pair(x0, y0));
		int i;
		for(i = 1 ; i < n ; ++i)
		{
			ll nx, ny;
			nx = ((ll)A * trees[sz(trees)- 1].first + (ll)B) % (ll)M;
			ny = ((ll)C * trees[sz(trees)- 1].second + (ll)D) % (ll)M;
			trees.pb(make_pair(nx, ny));
		}
		int j, q;
		ll res = 0;
		for(i = 0 ; i < sz(trees) ; ++i)
		{
			for(j = i + 1 ; j < sz(trees) ; ++j)
			{
                for(q = j + 1 ; q < sz(trees) ; ++q)
				{
					long long nx = trees[q].first + trees[j].first + trees[i].first;
					long long ny = trees[q].second + trees[j].second + trees[i].second;
					if(nx % 3 == 0 && ny % 3 == 0){
						res++;
					}
				}
			}
		}
		cout << "Case #" << k + 1 << ": " << res << endl;
	}
	return 0;
}

