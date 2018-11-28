#include <iostream>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cassert>
using namespace std;
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz(x) ((int)((x).size()))
#define rep(i, N) for (int i = 0; i < N; ++i)
#define foreach(it,v) for(__typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define print(x) cerr<<#x<<" = ";pr(x);cerr<<endl;
#define PRC(l,r) pr(l);foreach(it,v)pr(it==v.begin()?"":","),pr(*it);pr(r);
template<class T>void pr(T x){cerr<<x;} 
template<class T>void pr(vector<T>v){PRC('[',']');} 
template<class T1,class T2>void pr(pair<T1,T2>x){pr(x.first);pr(':');pr(x.second);} 
template<class T>void pr(set<T>v){PRC('{','}');} 
template<class T1,class T2>void pr(map<T1,T2>v){PRC('{','}');}
typedef long long lint;
typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long double Double;
typedef vector<long double> vd;

void solve(int num) {
	printf("Case #%d: ", num);
	int L;
	lint t;
	int N, C;
	cin >> L >> t >> N >> C;
	vector<lint> A(N);
	vector<lint> sum(N + 1);
	for (int i = 0; i < C; ++i) {
		cin >> A[i];
		sum[i + 1] = sum[i] + A[i];	
	}
	for (int i = C; i < N; ++i) {
		A[i] = A[i % C];
		sum[i + 1] = sum[i] + A[i];	
	}
	if (L == 0 || t / 2 >= sum[N]) {
		cout << 2 * sum[N] << endl;
		return;
	}
	int p = 0;
	while (sum[p] <= t / 2) ++p;
	vector<lint> v;
	v.pb(sum[p] - t / 2);
	for (int i = p; i < N; ++i) 
		v.pb(A[i]);

	sort(all(v));
	reverse(all(v));
	lint s = 0;
	for (int i = 0; i < L && i < sz(v); ++i) {
		s += v[i];
	}
	lint ans = s + (sum[N] - s) * 2;
	cout << ans << endl;
}

int main() {
    int tst;
    cin >> tst;
    for (int i = 1; i <= tst; ++i) 
        solve(i);
    return 0;
}
