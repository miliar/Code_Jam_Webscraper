#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
#include <cassert>
#include <bitset>
#include <cstring>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define sz(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<tint> vt;
typedef vector<double> vd;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef pair<int,int> pii;

const int maxn = 1000000 + 100;
int L, n, c;
tint t;
tint dist[maxn];

int main(){
	int tc; cin >> tc;	
	forn(ttc, tc){
		cin >> L >> t >> n >> c;
		forn(i, c) cin >> dist[i];
		forn(i, n) if(i >= c) dist[i] = dist[i-c];
		
		//forn(i, n) cout << dist[i] << " "; cout << endl;
		
		tint res = 0;
		vector<tint> seg;
		forn(i, n){
			if(res + 2 * dist[i] >= t){
				//cout << "corto sumo " << (res + 2*dist[i] - t) / 2 << endl;
				seg.pb((res + 2*dist[i] - t) / 2);	
				res += (t - res);
				forsn(j, i+1, n) seg.pb(dist[j]);
				break;
			}else { res += 2*dist[i]; }
		}	
		//forn(i, seg.size()) cout << seg[i] << " "; cout << endl;
		sort(seg.rbegin(), seg.rend());
		forn(i, seg.size()){
			if(i < L) res += seg[i];
			else res += 2 * seg[i];	
		}
		cout << "Case #" << ttc + 1 << ": " << res << endl;
		
	}
	return 0;
}
