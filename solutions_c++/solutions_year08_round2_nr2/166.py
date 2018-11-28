#include <vector>
#include <iostream>
#include <string>
#include <cstdio>
#include <set>
#include <map>
#include <queue>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <stack>
using namespace std;

#define LET(x,a) typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a); i!=b; i++)
#define EACH(i,v) for(LET(i,v.begin()); i!=v.end(); i++)
#define REP(i,n) FOR(i,0,n)
#define DBG(x) cout<<#x<<" --> "<<x<<"\t"
#define DBE(x) cout<<#x<<" --> "<<x<<"\n"
#define sz size()
#define ins insert
#define pb push_back
#define INF (int)1e8
#define COUNT(f,x) ({int _=0; f if(x) _++; _;})
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef vector<VS> VVS;
typedef pair<int,int> PII;
typedef long long LL;
typedef long double LD;
#define GI ({int t;scanf("%d",&t);t;})
#define INF (int)1e8

VI P;
const int M = 1000001;
void gen(void) {
	FOR(i,2,1000001) {
		int flag=1;
		for(int j=0;j<P.sz and P[j]*P[j] <= i; j++)
			if(i%P[j] == 0) {
				flag = 0; break;
			}
		if(flag) P.pb(i);
	}
}

LL parent[M], rank[M],A,B,p;

int f(int a) {
	int root = a,t;
	while(parent[root]!=root) root = parent[root];
	while(parent[a] != root) {
		t = parent[a];
		parent[a] = root;
		a = t;
	}
	return root;
}
 
void unionset(int a,int b) {
	if(a == b) return;
	if(rank[a] > rank[b]) parent[b] = a;
	else parent[a] = b;
	if(rank[a]==rank[b]) rank[b]++;
}

int main() {
	int C = GI;
	gen();
	REP(kase, C) {
		cerr << kase << endl;
		//A = GI, B = GI, p = GI;
		cin >> A >> B >> p;
		for(long long i = A; i<=B;i++) {
			parent[i-A] = i-A, rank[i-A] = 0;
		}
		REP(i,P.sz) if(P[i]>=p and P[i]<=B) {
			LL st = (A/P[i])*P[i];
			if(st < A) st+=P[i];
			LL init = st;
			//cout << "here\n";
			for(; st <= B; st+=P[i]) {
				unionset(f(st-A), f(init-A));				
			}
		}
		set<int> S;	for(long long i=A; i<=B;i++) S.insert(f(i-A)); 
		printf("Case #%d: %d\n", kase+1, S.sz);		
	}
	return 0;
}
