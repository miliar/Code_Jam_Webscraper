#define _CRT_SECURE_NO_DEPRECATE
#include<vector>
#include<deque>
#include<list>
#include<set>
#include<map>
#include<algorithm>
#include<numeric>
#include<iostream>
#include<sstream>
using namespace std;

#define sz(X) ((int)(X).size())
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define all(X) (X).begin(),(X).end()
#define FOR(I,S,N) for(int I=(S);I<(N);++I)
#define REP(I,N) FOR(I,0,N)
#define PR(X) cout<<#X<<" = "<<(X)<<" "
#define PRL cout<<endl
#define PRV(X) {cout<<#X<<" = {";int __prv;REP(__prv,sz(X)-1) cout<<(X)[__prv]<<",";cout<<(X).back()<<"}"<<endl;}

typedef long long lint;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define SS stringstream
template<typename T> string tos(T q,int w=0){SS A;A.flags(ios::fixed);A.precision(w);A<<q;string s;A>>s;return s;}
template<typename T> T sto(string s){SS A(s);T t;A>>t;return t;}
template<typename T> vector<T > s2v(string s){SS A(s);vector<T > ans;while(A&&!A.eof()){T t;A>>t;ans.pb(t);}return ans;}

// end of pre-inserted code

bool inside(const vector<VI> &a, int k, int dx, int dy, int i, int j, int &ret) {
	int n = sz(a);
	
	if( (i >= dx && i < dx + n && j >= dy && j < dy + n) ) {
		ret = a[i-dx][j-dy];
		return true;
	}
	else return false;
}

bool check(const vector<VI> &a, int k, int dx, int dy) {
	int n = sz(a);
	FOR(i, dx, dx+n) {
		FOR(j, dy, dy+n) {
			int b;
			if(inside(a, k, dx, dy, k-j-1, k-i-1, b))
				if(b != a[i-dx][j-dy])
					return false;
			if(inside(a, k, dx, dy, j, i, b))
				if(b != a[i-dx][j-dy])
					return false;
		}
	}
	return true;
}

vector<VI> rot(vector<VI> a) {
	int n = (sz(a) + 1) / 2;
	vector<VI> b(n);
	REP(i, n) {
		FOR(j, i, i + n) {
			b[i].pb(a[j].back());
			a[j].pop_back();
		}
	}
	return b;
}

int main() {
	//freopen("1.txt", "r", stdin);

	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);


	int tc;
	scanf("%d", &tc);
	FOR(tt, 1, tc+1) {
		int n;
		scanf("%d", &n);
		vector<VI> a(2*n-1);
		REP(i, n) {
			REP(j, i+1) {
				int x;
				scanf("%d", &x);
				a[i].pb(x);
			}
		}
		FOR(i, n, 2*n - 1) {
			REP(j, 2*n - 1 - i) {
				int x;
				scanf("%d", &x);
				a[i].pb(x);
			}
		}

		a = rot(a);

		int ans = 0;
		
		FOR(k, n, 100 * n + 3) {
			ans = k * k - n * n;
			REP(dx, k-n+1) {
				if(check(a, k, dx, 0)) goto brk;
				if(check(a, k, dx, k-n)) goto brk;
				if(check(a, k, 0, dx)) goto brk;
				if(check(a, k, k-n, dx)) goto brk;
			}
			//REP(dx, k-n+1) {
			//	REP(dy, k-n+1) {
			//		if(check(a, k, dx, dy)) {
			//			cerr << "k = " << k << " dx = " << dx << " dy = " << dy << endl;
			//			check(a, k, dx, dy);
			//			goto brk;
			//		}
			//	}
			//}
		}

brk:
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}