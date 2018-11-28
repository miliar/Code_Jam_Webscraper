
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
const int MAXN = 1100;
int N, X, Y, R[MAXN];
double x[MAXN], y[MAXN];
pair<int,int> order[MAXN];

double gRand(){
	double res = 0.0;
	FOR(i,0,5){
		res = (res + abs(rand()))/ RAND_MAX;
	}
	return res;
}
const int MAXFAIL = 1000000;
bool check(int i){
	int n = order[i].second;
	FOR(j,0,i){
		int id = order[j].second;
		double dx = x[n] - x[id];
		double dy = y[n] - y[id];
		double dr = R[n] + R[id] + 0.01;
		if(dx*dx + dy * dy < dr * dr)return false;
	}
	return true;
}
bool tryput(){
	int failct = 0;
	FOR(i,0,N){
		int n = order[i].second;
		bool ok = 0;
		while(!ok){
			x[n] = gRand() * X;
			y[n] = gRand() * Y;
			x[n] = max(0.001, min(X - 0.001, x[n]));
			y[n] = max(0.001, min(Y - 0.001, y[n]));
			ok = check(i);
			if(!ok){
				failct++;
				if(failct > MAXFAIL)return false;
			}
			double d = max(x[n], y[n]);
			while(d > 0.01){
				if(x[n] > d){
					x[n] -= d;
					if(!check(i))x[n]+=d;
				}
				if(y[n] > d){
					y[n] -= d;
					if(!check(i))y[n] += d;
				}
				d *= 0.5;
			}
		}
	}
	FOR(i,0,N)printf(" %.3lf %.3lf", x[i], y[i]);
	cout << endl;
	return true;
}
int main() {
	int tc;
	cin >> tc;
	FOR(tcc ,1,tc+1){
		cin >> N >> X >> Y;
		FOR(i,0,N)cin >> R[i];
		FOR(i,0,N)order[i] = mp(-R[i], i);
		sort(order, order + N);
		cout << "Case #" << tcc <<":";
		while(!tryput());
	}
	return 0;
}
