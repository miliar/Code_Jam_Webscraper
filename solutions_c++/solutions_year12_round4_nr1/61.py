
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

const int MAXN = 11000;
int N, D[MAXN], L[MAXN], CL[MAXN], DI, B[MAXN], F[MAXN];
bool inside[MAXN];
bool check(){
	memset(CL,0,sizeof(CL));
	memset(F,0,sizeof(B));
	memset(B,0,sizeof(F));
	memset(inside,0,sizeof(inside));
	queue<int> q;
	q.push(0);
	CL[0] = D[0];
	while(!q.empty()){
		int n = q.front();
		q.pop();
	//	cout << n << " " << CL[n] << endl;
		inside[n] = 0;
		if(abs(DI - D[n])<=CL[n])return true;
		while(B[n] < n){
			int to = n - B[n] - 1;
			if(CL[n] >= abs(D[n] - D[to])){
				int nl = min(abs(D[n] - D[to]), L[to]);
				if(nl > CL[to]){
					CL[to] = nl;
					if(!inside[to]){
						inside[to] = 1;
						q.push(to);
					}
				}
				B[n]++;
			} else {
				break;
			}
		}
		while(F[n]+n < N-1){
			int to = n + F[n] + 1;
			if(CL[n] >= abs(D[n] - D[to])){
				int nl = min(abs(D[n] - D[to]), L[to]);
				if(nl > CL[to]){
					CL[to] = nl;
					if(!inside[to]){
						inside[to] = 1;
						q.push(to);
					}
				}
				F[n]++;
			} else {
				break;
			}
		}
	}
	return false;
}
int main() {
	int tc;
	cin >> tc;
	FOR(tcc,1,tc+1){
		cout << "Case #" << tcc << ":";
		cin >> N;
		FOR(i,0,N)cin >> D[i] >> L[i];
		cin >> DI;
		if(check())cout << " YES\n";
		else cout << " NO\n";
	}
	return 0;
}
