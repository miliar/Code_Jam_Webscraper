#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cfloat>
#include <cctype>
#include <algorithm>
#include <sstream>
#include <bitset>

#define REP(i,a) for(i=0;i<a;++i)
#define FOR(i,a,b) for(i=a;i<=b;++i)
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
#define sz(x) (int)(x).size()
using namespace std;

int mat[400][400];
bool readed[400][400];
int maxa,mina;
int maxb,minb;

bool sym(int i, int j) {
	int a,b;
	int m = 0;
	int newa,newb;
	FOR(a,mina,200) {
		newa = 2*i-a;
		for(b=200-m;b<=200+m;b+=2) {
			newb = 2*j-b;
			if (newa >= 0 && newa <= 399 && readed[newa][b] && mat[a][b] != mat[newa][b])
				return false;
			if (newb >= 0 && newb <= 399 && readed[a][newb] && mat[a][b] != mat[a][newb])
				return false;
			//cout << a << ' ' << b << ' ' << mat[a][b] << ' ' << mat[a][newb] << endl;
		}
		++m;
	}
	--m;
	FOR(a,200+1,maxa) {
		--m;
		newa = 2*i-a;
		for(b=200-m;b<=200+m;b+=2) {
			newb = 2*j-b;
			if (newa >= 0 && newa <= 399 && readed[newa][b] && mat[a][b] != mat[newa][b])
				return false;
			if (newb >= 0 && newb <= 399 && readed[a][newb] && mat[a][b] != mat[a][newb])
				return false;
			//cout << a << ' ' << b << ' ' << mat[a][b] << ' ' << mat[a][newb] << endl;
		}
	}

	return true;
}

void main() {
	int T,k;
	scanf("%d", &T);
	int i,j;
	int a,b;

	REP(i,T) {
		scanf("%d", &k);
		memset(readed,0,sizeof(readed));
		maxa = 0;
		mina = 400;
		maxb = 0;
		minb = 400;

		int m = 0;
		FOR(a,200-k+1,200) {
			for(b=200-m;b<=200+m;b+=2) {
				scanf("%d", &mat[a][b]);
				readed[a][b] = true;
				minb = min(minb,b);
				maxb = max(maxb,b);
			}
			mina = min(mina,a);
			maxa = max(maxa,a);
			++m;
		}
		--m;
		FOR(a,200+1,200+k-1) {
			--m;
			for(b=200-m;b<=200+m;b+=2) {
				scanf("%d", &mat[a][b]);
				readed[a][b] = true;
			}
			maxa = max(maxa,a);
		}

		int res = 1000000;
		m = k + (k%2?0:1);
		int adder = 1;
		FOR(a,200-k,200) {
			for(b=200-m;b<=200+m;++b) {
				//cout << "check " << a << ' ' << b << endl;
				if (sym(a,b)) {
					int t1 = (abs(mina-a) + abs(200-b));
					t1 += (t1%2?1:1);
					int t2 = (abs(maxa-a) + abs(200-b));
					t2 += (t2%2?1:1);
					int t3 = (abs(200-a) + abs(minb-b));
					t3 += (t3%2?1:1);
					int t4 = (abs(200-a) + abs(maxb-b));
					t4 += (t4%2?1:1);
					int r = 1;
					r = max(r,t1);
					r = max(r,t2);
					r = max(r,t3);
					r = max(r,t4);
					res = min(res,r);
					//cout << t1 << ' '<< t2 << ' ' << t3 << ' ' << t4 << endl;
					//cout << "res " << a << ' ' << b << ' '<< r << ' ' << res << endl;
				}
			}
			m += adder;
			adder *= -1;
		}

		FOR(a,200+1,200+k) {
			for(b=200-m;b<=200+m;++b) {
				//cout << "check " << a << ' ' << b << endl;
				if (sym(a,b)) {
					int t1 = (abs(mina-a) + abs(200-b));
					t1 += (t1%2?1:1);
					int t2 = (abs(maxa-a) + abs(200-b));
					t2 += (t2%2?1:1);
					int t3 = (abs(200-a) + abs(minb-b));
					t3 += (t3%2?1:1);
					int t4 = (abs(200-a) + abs(maxb-b));
					t4 += (t4%2?1:1);
					int r = 1;
					r = max(r,t1);
					r = max(r,t2);
					r = max(r,t3);
					r = max(r,t4);
					res = min(res,r);
					//cout << t1 << ' '<< t2 << ' ' << t3 << ' ' << t4 << endl;
					//cout << "res " << a << ' ' << b << ' '<< r << ' ' << res << endl;
				}
			}
			m += adder;
			adder *= -1;
		}

		cout << "Case #" << (i+1) << ": " << res*res - k*k << endl;
	}
}