
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)

int N;
struct Level{
	ll P, L, id;
} le[1100];
ll gcd(ll a, ll b){
	if(b==0)return a;
	return gcd(b,a%b);
}
bool operator <(const Level & a, const Level & b){
	if(a.L==b.L && a.P == b.P)return a.id < b.id;
	ll gc = gcd(a.L,b.L);
	double v1 = pow(a.P*0.01,b.L/gc);
	double v2 = pow(b.P*0.01,a.L/gc);
	double mi = min(v1,v2);
	if(abs(v1-v2)/mi>eps)return v1 < v2;
	return a.id < b.id;
}
int main() {
	int tc;
	cin >> tc;
	FOR(tcc,1,tc+1){
		cin >> N;
		FOR(i,0,N)le[i].id = i;
		FOR(i,0,N)cin >> le[i].L;
		FOR(i,0,N)cin >> le[i].P;
		FOR(i,0,N)le[i].P = 100 - le[i].P;
		sort(le,le+N);
		cout << "Case #" << tcc <<":";
		FOR(i,0,N)cout << " " << le[i].id;
		cout << endl;
	}
	return 0;
}
