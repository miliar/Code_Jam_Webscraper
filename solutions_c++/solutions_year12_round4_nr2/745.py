#pragma warning(disable : 4996)
#include <cstdio>
#include <cmath>
#include <ctime>
#include <vector>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <string>
using namespace std;
typedef std::vector<int> vi;
typedef std::vector<vi> vvi;
typedef std::pair<int,int> ii;
typedef std::pair<int,ii> iii;
typedef std::vector<ii> vii;
typedef std::vector<string> vs;
typedef std::vector<double> vd;

#define sz(a) int(a.size())
#define REP(i,n) for(int i = 0; i < n; ++i)
#define FOR(i,a) for(int i = 0; i < sz(a); ++i)

inline bool isdig(int a){return unsigned(a-'0') < 10;}
template<class T> static inline T getnum(){
   unsigned i; T j;
   do i = getchar(); while(!isdig(i));
   j = i-'0';  i=getchar() ;
   while(isdig(i)){ j = (j<<1)+(j<<3)+(i-'0'); i = getchar(); }
   return j;
}

int N, T;

struct posit{
	double x,y,r;
	posit(double xx, double yy, double rr){
		x = xx, y = yy, r = rr;
	}
};
double sqr(double a){
	return a*a;
}
double eps = 1e-9;
int main(int argc, char *argv[]){
	bool out = true;
	#ifndef ONLINE_JUDGE
		freopen("d:/home/code/GCJ/Bb.txt","r",stdin);
		if( out){
			freopen("d:/home/code/GCJ/Out.txt","w",stdout);
		}
	#endif
	int nt = getnum<int>();
	for(int numt = 1; numt <= nt; ++numt){
		int N = getnum<int>();
		int W = getnum<int>();
		int L = getnum<int>();
		vii r(N);
		vd x(N), y(N);
		for(int i = 0; i < N; ++i){
			int rr = getnum<int>();
			r[i] = ii(rr,i);
		}
		sort(r.begin(), r.end(), greater<ii>());
		bool transp = L > W;
		if( transp ) {
			swap(W,L);
		}
		list<ii> pos;
		double xx = -r[0].first, yy=0;
		int ci = 0;
		for(; ci < N; ++ci){
			if( xx + r[ci].first +eps >  W ) break;
			x[ci] = xx+ r[ci].first, y[ci] = 0;
			xx+=2*r[ci].first+eps;
		}
		
		while( ci < N ){
			double My = W, my = 0, mx=0, Mx=0, lx = 0;
			double rr = r[ci].first;
			for( int j = 0; j < 100; j++){
				double cy = (My + my)*0.5;
				Mx = W+r[0].first;
				mx = 0;
				bool invalid = false;
				for( int j2 = 0; j2 < 100; j2++){
					double cx = (Mx + mx)/2;
					bool ok = true;
					for(int i = 0; i < ci; ++i){
						if( sqr(cx-x[i])+ sqr(cy-y[i]) < sqr(r[i].first+rr) ){
							ok = false;break;
						}
					}
					if( ok ) Mx = cx; else mx = cx;
					if( mx > W-1e-9 ){
						invalid = true;
						break;
					}
				}
				if( invalid ){
					my = cy; 
				} else {
					My = cy;
					lx = Mx;
				}
			}
			x[ci] = lx; y[ci] = My+eps;
			ci++;
		}
		vd x2(N), y2(N);
		for(int i = 0; i < N; ++i){
			x2[r[i].second] = x[i];
			y2[r[i].second] = y[i];
		}
		printf( "Case #%d:", numt);
		if( transp){
			for(int i = 0; i < N; ++i){
				printf( " %.12f %.12f", y2[i], x2[i] );
			}
		} else {
			for(int i = 0; i < N; ++i){
				printf( " %.12f %.12f", x2[i], y2[i] );
			}
		}
		printf("\n");
		fflush(stdout);
	}
	return 0;	
}
