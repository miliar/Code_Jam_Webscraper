#include <vector>
#include <list>
#include <ctime>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define ll  long long
#define pb push_back
#define mp make_pair
#define size(v) (int)(v.size())
#define loop(i,n) for(i=0;i<n;i++)
#define all(v) v.begin(), v.end()
#define tr(container, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define vi vector<int>

using namespace std;
ll const inf = 10000000;
vector<int> tre, g, c;
int M;
ll traverse(int i, int d) {
	//cout<<i<<" "<<d<<" "<<tre[i]<<" "<<c[i]<<" "<<g[i]<<endl;
	if (2 * i >= M) {
		if (tre[i] == d)
			return 0;
		else
			return inf;
	}

	if (tre[i] == d)
		return 0;
	int n, ret = inf;

	if (c[i] == 1) {
		if (g[i])
			n = tre[2 * i] | tre[2 * i + 1];
		else
			n = tre[2 * i] & tre[2 * i + 1];
		//cout<<i<<" n:"<<n<<" "<<tre[2*i]<<" "<<tre[2*1+1]<<endl;
		if (n == d)
			return 1;
		ret = 1;

		if (g[i] == 0) {
			if (d) {
				ret += traverse(2 * i, 1) + traverse(2 * i + 1, 1);
				//if( ret>=inf) return inf;
				//else return ret+1;
			} else {
				ret += min(traverse(2 * i, 0), traverse(2 * i + 1, 0));
			}
		} else {
			if (d) {
				ret += min(traverse(2 * i, 1), traverse(2 * i + 1, 1));
			} else {
				ret += traverse(2 * i, 0) + traverse(2 * i + 1, 0);
				//if( ret>=inf) return inf;
				//else return ret+1;
			}
		}
	}
int ret1=inf;
	if (g[i]) {
		if (d) {
			ret1<?=traverse(2*i,1)+traverse(2*i+1,1);
			//if( ret>=inf) return inf;
			//else return ret;
		} else {
			ret1<?= min(traverse(2*i,0),traverse(2*i+1,0));
		}
	} else {
		if (d) {
			ret1<?= min(traverse(2 * i, 1), traverse(2 * i + 1, 1));
		} else {
			ret1 <?= traverse(2 * i, 0) + traverse(2 * i + 1, 0);
			//	if (ret >= inf)
			//	return inf;
			//else
			//return ret;
		}
	}
	//cout<<i<<" "<<ret<<" "<<ret1<<endl;
	return ret<?ret1;

}

int main() {

	int i, j, k;
	int t;
	cin >> t;
	for (int numt = 0; numt < t; numt++) {
		int m, v;
		cin >> m >> v;
		M = m;
		tre.clear();
		g.clear();
		c.clear();

		tre.pb(-1);
		g.pb(-1);
		c.pb(-1);
		for (i = 0; i < (m - 1) / 2; i++) {
			cin >> j >> k;
			tre.pb(-1);
			g.pb(j);
			c.pb(k);
		}
		for (i = 0; i < (m + 1) / 2; i++) {
			cin >> j;
			tre.pb(j);
			g.pb(-1);
			c.pb(-1);
		}
		int pi = (m - 1) / 2;
		for (i = pi; i > 0; i--) {
			if (g[i] == 1)
				tre[i] = tre[2 * i] & tre[2 * i + 1];
			else
				tre[i] = tre[2 * i] | tre[2 * i + 1];
		}

		//for(i=1;i<size(tre);i++) cout<<tre[i]<<" "; cout<<endl;
		int ret = traverse(1, v);
		//cout<<ret<<endl;
		if (ret >= inf)
			cout << "Case #" << numt + 1 << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << numt + 1 << ": " << ret << endl;
	}

	return 0;
}
