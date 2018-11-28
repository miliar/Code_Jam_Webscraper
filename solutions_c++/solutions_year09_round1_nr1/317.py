#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<map>
#include<cmath>
#include<algorithm>
#include<set>
using namespace std;

#define sz(q) ((int)(q).size())
#define _fill(mem,v) memset(mem,v,sizeof(mem))
#define FOR(i,q1,q2) for(int i=(q1); i<=(q2); ++i)
#define FORD(i,q1,q2) for(int i=(q1); i>=(q2); --i)
#define FOREACH(it,mp) for(typeof((mp).begin()) it=(mp).begin(); it!=(mp).end(); ++it)

#define isdig(c) ('0'<=(c) && (c)<='9')

#define inbit(i,n) ((n & (1<<i))>0?1:0)
#define bit(i) (1<<i)

#define mp make_pair
#define xx first
#define yy second

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

#define MAXK 1001000

int bb[11], T, N;
char tmp[100100];
int ans[11][MAXK], dep[MAXK];

int squaresum(int q, int b) {
	int res = 0;
	while( q>0 ) {
		res += (q%b)*(q%b);
		q/=b;
	}
	return res;
}

bool ff(int q, int b) {
	if( q<MAXK ) {
		if( ans[b][q]!=-1 ) return ans[b][q];
		if( dep[q] ) return false;
		dep[q] = true;
	}

	//cerr << q << " sq=" << squaresum(q, b) << endl;
	int res = 0;
	if( q==1 ) res = 1;
	else res = ff(squaresum(q, b) ,b);
	
	if( q<MAXK ) {
		ans[b][q] = res;
		dep[q] = false;
	}
	return res;
}

vector<int> ss[11];
int it[11];

int solve() {
		if( N==0 ) return 2;
		int num = 2;
		while( true ) {
			bool ok = true;
			for(int i=0; i<N; ++i) {
				//cerr << "testing " << num << " base=" << bb[i] << endl;
				if( !ff(num, bb[i]) )
					ok = false;
			}
			if( ok ) break;
			num++;
			//if( num>=MAXK ) cerr << "MAXK overflowed" << endl;
		}
		return num;
}

map< set<int>, int> anss;
int e;

void check() {
	set<int> q;
	cerr << "checking N=" << N << endl;
	for(int i=0; i<N; ++i) {
		q.insert(bb[i]);
		cerr << bb[i] << " ";
	}
	cerr << endl;
	anss[q] = solve();
	cerr << "done " << ++e << endl;
}

void gen(int ind) {
	if( ind==11 ) {
		check();
		return;
	}
	
	gen(ind+1);
	bb[N++] = ind;
	gen(ind+1);
	N--;
}

int main() {
	memset(ans, -1, sizeof(ans));

	if( true ) {
		N = 0;
		gen(2);
	}
	
	//printf("Press in I am ready\n");
	char tmp[100];
	scanf("%s", tmp);
	
	freopen("input", "r", stdin);
	gets(tmp);
	sscanf(tmp,"%d",&T);
	
	for(int t=1; t<=T; ++t) {	
		gets(tmp);
		N = 0;
		for(int i=-1; i==-1 || tmp[i]!=0; ++i)
			if( i==-1 || tmp[i]==' ' ) {
				int base;
				sscanf(tmp+i+1, "%d", &base);
				bb[N++] = base;
			}
		
		if( true ) {
			set<int> q;
			for(int i=0; i<N; ++i)
				q.insert(bb[i]);
			printf("Case #%d: %d\n", t, anss[q]);
		} else {
			int num = solve();
			printf("Case #%d: %d\n", t, num);
		}
		cerr << "done " << t << "/" << T << endl;
	}
	
	return 0;
}
