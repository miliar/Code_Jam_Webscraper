#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <complex>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <complex>
#include <stack>
#include <memory.h>
#ifdef NEV_DEBUG
#include <ctime>
#endif
using namespace std;

const int SIZE = 32;
const double pi = 3.1415926535897932384626433832795;


typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int uint;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef LL matrix[SIZE][SIZE];

#define sz size()
#define mp make_pair
#define pb push_back
#define ALL(a) (a).begin(), (a).end()
#define FOR(i,a,b) for(int i=(a),_b(b); i<_b; ++i)
#define RFOR(i,a,b) for(int i=(a)-1,_b(b); i>=_b; --i)
#define CLR(a,b) memset(a,b,sizeof(a))
#define CPY(a,b) memcpy(a,b,sizeof(a))
#define sqr(a) ((a)*(a))
#define MIN(a,b) ((a)<(b)?(a):(b))

char ch[1<<20];
string gs() {scanf("%s",ch); return string(ch);}
string gl() {gets(ch); return string(ch);}
template <class T>
T gcd(T a, T b) { return (!a)?b:gcd(b%a,a); }
void error(){ int yyy=0; cout << 7/yyy; }

PII A[1<<20];
PII B[1<<20];
void solve() {
	int X,S,R,N,T;
	scanf("%d%d%d%d%d",&X,&S,&R,&T,&N);
	int n=0;
	FOR(i,0,N) {
		int a,b,w;
		scanf("%d%d%d",&a,&b,&w);
		B[n]=mp(a,b);
		A[n++]=mp(w,(b-a));
	}
	int m=n;
	B[m++]=mp(0,0);
	B[m++]=mp(X,X);
	sort(B,B+m);
	int total=0;
	int last=B[0].first;
	FOR(i,1,m) {
		if (B[i].first>last) {
			total+=B[i].first-last;
			last=B[i].second;
		} else {
			last=max(last,B[i].second);
		}
	}
	if (total) {
		A[n++]=mp(0,total);
	}
	sort(A,A+n);

	double res=0.0;
	double left=T;
	FOR(i,0,n) {
		int aa=A[i].first;
		int bb=A[i].second;
		double tm=(double)A[i].second/(double)(A[i].first+R);
		double t = min(left,tm);
		double a = t+((double)A[i].second - t*((double)(A[i].first+R)))/(double)(A[i].first+S);
		res+=a;
		left-=t;
	}
	printf("%.10lf\n",res);
}

int main() {
#ifdef NEV_DEBUG
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    clock_t beg = clock();
#else
    //freopen("union.in","r",stdin);
    //freopen("union.out","w",stdout);
#endif

	int tests; scanf("%d",&tests); 
	for(int tn=1; tn<=tests; ++tn){
		fprintf(stderr, "Case #%d ... ",tn);
		printf("Case #%d: ",tn);
		solve();
		fprintf(stderr, "Done\n");
	}

#ifdef NEV_DEBUG
    fprintf(stderr,"*** Total time: %.3lf ***\n",1.0*(clock()-beg)/CLOCKS_PER_SEC);
#endif
    return 0;
}