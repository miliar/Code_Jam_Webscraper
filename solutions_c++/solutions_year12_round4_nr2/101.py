#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <queue>

using namespace std;

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define REP(i,a)    FOR(i,0,a)
#define ZERO(m)     memset(m,0,sizeof(m))
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()
#define LL          long long
#define LD          long double
#define MP          make_pair
#define X           first
#define Y           second
#define VC          vector
#define PII			pair <int, int>
#define VI          VC<int>
#define VPII		VC < PII >
#define VS          VC<string>
#define DB(a)		cout << #a << ": " << a << endl;

void print(VI v) {cerr << "[";if (v.S) cerr << v[0];FOR(i, 1, v.S) cerr << ", " << v[i];cerr << "]\n";}
void print(VS v) {cerr << "[";if (v.S) cerr << v[0];FOR(i, 1, v.S) cerr << ", " << v[i];cerr << "]\n";}
template<class T> string i2s(T x) {ostringstream o; o << x; return o.str(); }
VS splt(string s, char c = ' ') {VS rv; int p = 0, np; while (np = s.find(c, p), np >= 0) {if (np != p) rv.PB(s.substr(p, np - p)); p = np + 1;} if (p < s.S) rv.PB(s.substr(p)); return rv;}

#define TRIES 1000

double randDouble() {
	return (rand() + 0.5) / (RAND_MAX + 1.0);
}

double DIST(double x0,double y0,double x1,double y1) {
	return (x0-x1)*(x0-x1)+(y0-y1)*(y0-y1);
}

double px[10000];
double py[10000];
double rx[10000];
double ry[10000];
int main() {
	srand(1);
	int tc;
	cin >> tc;
	FOR(atc, 1, tc + 1) {
		int n, w, l;
		cin >> n >> w >> l;
		VPII v(n); 
		VI rr(n);
		REP(i, n) {
			cin >> rr[i];
			v[i].X = rr[i];
			v[i].Y = i;
		}
		sort(ALL(v)); 
		reverse(ALL(v));
		
		REP(i, n) {
			double bx = 1e15;
			double by = 1e15;
			
			int t = 0;
			while (t < TRIES || bx > 1e12) {
				double x = randDouble() * w;
				double y = randDouble() * l;
				REP(j, i) if (DIST(x,y,px[j],py[j]) < (double)(v[i].X + v[j].X) * (v[i].X + v[j].X) + 1e-3) goto next;
				if (x + y < bx + by) {
					bx = x; 
					by = y;
				}
				next: ;
				t++;
			}
			px[i] = bx;
			py[i] = by;
		}
		REP(i, n) {
			rx[v[i].Y] = px[i];
			ry[v[i].Y] = py[i];
		}
		
		/*
		REP(i, n) REP(j, i) if (DIST(rx[i],ry[i],rx[j],ry[j]) < (double)(rr[i]+rr[j])*(rr[i]+rr[j]) + 1e-3) {
			printf("error: %.9lf,%.9lf:%d %.9lf,%.9lf:%d --> %.9lf %.9lf\n", rx[i],ry[i],rr[i],rx[j],ry[j],rr[j],DIST(rx[i],ry[i],rx[j],ry[j]),(double)(rr[i]+rr[j])*(rr[i]+rr[j]) + 1e-3);
		}
		*/
			
		printf("Case #%d:", atc);
		REP(i, n) printf(" %.9lf %.9lf", rx[i], ry[i]);
		printf("\n");
	}
}