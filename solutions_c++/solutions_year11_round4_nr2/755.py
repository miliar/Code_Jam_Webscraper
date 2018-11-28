#include <iostream>
#include <vector>
#include <set>
#include <iomanip>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <map>
#include <assert.h>
#include <cmath>
#include <queue>
#include <stack>
using namespace std;

#define For(i,a,b) for(int i=(a);i<(b);i++)
#define rep(i,x) For(i,0,x)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i!=(c).end(); ++i)

#define mp make_pair
#define pb push_back
#define sz(x) int((x).size())
#define TWO(x) (1<<(x))
#define F first
#define S second
#define setmax(a,b) a=max(a,b)
#define setmin(a,b) a=min(a,b)

typedef vector<int> Vi;
typedef vector<Vi> Vvi;
typedef pair<int,int> Pii;

typedef pair<int,int> Pii;
typedef vector<Pii> Vpii;
typedef vector<Vpii> Vvpii;
typedef long long ll;
typedef pair<double,double> Pdd;

#define eps 1e-9
#define C first
#define W second

Pdd combine(Pdd a, Pdd b)
{
		double w = a.W + b.W;
		return mp(w > 0 ? (a.C * a.W + b.C *b.W)/w : 0.0, w);
}
Pdd erase(Pdd a, Pdd b){
	double w = a.W - b.W;
	if(w < eps) return mp(0.0, 0.0);
	double c = (a.C * a.W - b.C*b.W)/w;
	return mp(c,w);
}
#define DIM 50
pair<double,double> C[DIM][DIM][DIM];
double W[DIM][DIM];
int nr, nc;
double d;

int main() {
int np; cin>>np;
rep(tp,np){
	cin>>nr>>nc; cin >> d;
	rep(r, nr){
		string s; cin>>s;
		rep(c,nc) W[r][c] = s[c] - '0' + d;
	}
	rep(c,nc){
		rep(a, nr) rep(b,nr+1){
			C[c][a][b] = mp(0.0, 0.0);
			if(a < b){
				C[c][a][b] = combine(C[c][a][b-1], mp(b-1, W[c][b-1]));
			}
		}
	}

	int lim = min(nr, nc) + 1;
	int best = 0;
	Pdd X, Y;
	//printf("%d %d\n", nr, nc);
	For(s, 3, lim){
		//printf("S: %d\n", s);
		rep(r, nr - s + 1){
			X = Y = mp(0,0);
			rep(i, s){
				Pdd use = (i > 0 && i < s-1) ? C[i][r][r+s] : C[i][r+1][r+s-1];
				//printf("%f %f\n", use.W, use.C);
				X = combine(X, mp(i, use.W));
				Y = combine(Y, use);
			}
			rep(c, nc - s + 1){
				//printf("%d %d ==> %f %f %f %f\n", r, c, X.C, Y.C, X.W, Y.W);
				if(abs(X.C - (double(2*c + s)/2.0 - 0.5)) < eps &&
						abs(Y.C - (double(2*r + s)/2.0 - 0.5)) < eps) setmax(best, s);

				if(c +  s < nc){
					Pdd gone = C[c][r+1][r+s-1];
					Pdd c1 = C[c+1][r][r+1];
					Pdd c2 = C[c+1][r+s-1][r+s];
					Pdd c3 = C[c+s-1][r][r+1];
					Pdd c4 = C[c+s-1][r+s-1][r+s];
					Pdd nnew = C[c+s][r+1][r+s-1];
					Pdd in = combine(nnew, combine(c3, c4));
					Pdd out = combine(gone, combine(c1, c2));
					Y = combine(erase(Y, out), in);

					gone.C = c;
					c1.C = c2.C = c+1;
					c3.C = c4.C = c+s-1;
					nnew.C = c+s;
					in = combine(nnew, combine(c3, c4));
					out = combine(gone, combine(c1, c2));
					X = combine(erase(X, out), in);

				}
			}

		}
	}

	printf("Case #%d: ", tp + 1);
	if(best) printf("%d\n", best);
	else  printf("IMPOSSIBLE\n");
}
}
