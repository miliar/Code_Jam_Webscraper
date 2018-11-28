/*
Author : OmarEl-Mohandes
PROG   : A
LANG   : C++
*/
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <complex>
#include <valarray>
#include <memory.h>
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define REP(i,k,m) for(int i=k;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define oo ((int)1e9)

int main()
{
	freopen("A.in" , "rt" , stdin);
	freopen("A.out" , "wt" , stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		int a , b , n;
		vector<pair<int , int> >p;
		cin >> n;
		for (int k = 0; k < n; ++k) {
			cin >> a >> b;
			p.pb(mp(a , b));
		}
		int res = 0;
		for (int k = 0; k < n; ++k) {
			int c = 0;
			for (int j = 0; j < n; ++j) {
				if(j == k)continue;
				if(p[k].second < p[j].second && p[k].first > p[j].first)
					c++;
			}
			res += c;
		}
		cout << "Case #" << i+1 << ": " << res << endl;

	}
	return 0;
}
