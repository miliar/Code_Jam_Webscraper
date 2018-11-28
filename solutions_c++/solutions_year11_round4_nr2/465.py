#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef long double LD;
#define REP(I,N) for(int I=0;I<(N);++I)
#define FOR(I,A,B) for(int I=(A);I<=(B);++I)
#define FORD(I,A,B) for(int I=(A);I>=(B);--I)
#define FOREACH(I,C) for(__typeof((C.begin())) I=(C).begin();I!=(C).end();++I)
template<class T> inline void debug(const T&c) { cout << "{"; FOREACH(it,c) cout << *it << ","; cout << "}" << endl; }
template<class T> inline void setmin(T &a,const T& b){if(b<a) a=b;}
template<class T> inline void setmax(T &a,const T& b){if(b>a) a=b;}
template<class T> inline int size(const T&c) { return (int)c.size(); }
template<class T> inline string to_str(const T& a) { ostringstream os(""); os << a; return os.str(); }
template<class T> inline T sqr(const T&a) { return a*a; }
template<class T> T next() { T x; cin >> x; return x; }
int nint() { int x; scanf("%d",&x); return x; }
#define all(A) (A).begin(),(A).end()
#define st first
#define nd second
#define mp make_pair
#define pb push_back

LL sum[509][509];
LL sumx[509][509];
LL sumy[509][509];

LL tab[509][509];
int R,C;

bool check(int i, int j, int k) {
	LL i2,j2,i3,j3,i4,j4;
	LL cx,cy;
	LL sx,sy,s;

	if ((k%2)==0){
		i2 = i + k/2;
		j2 = j + k/2;
		i3 = i - k/2;
		j3 = j - k/2;
		i4 = i - k/2 + 1;
		j4 = j - k/2 + 1;
		cx = i*2 + 1;
		cy = j*2 + 1;
		if (i2>R||i3<0) return false;
		if (j2>C||j3<0) return false;			
		sx = sumx[i2][j2] - sumx[i2][j3] - sumx[i3][j2] + sumx[i3][j3];
		sy = sumy[i2][j2] - sumy[i2][j3] - sumy[i3][j2] + sumy[i3][j3];
		s = sum[i2][j2] - sum[i2][j3] - sum[i3][j2] + sum[i3][j3];
		sx *= 2;
		sy *= 2;
	} else {
		i2 = i + k/2;
		j2 = j + k/2;
		i3 = i - k/2 - 1;
		j3 = j - k/2 - 1;
		i4 = i - k/2;
		j4 = j - k/2;
		cx = i;
		cy = j;	
		if (i2>R||i3<0) return false;
		if (j2>C||j3<0) return false;	
		sx = sumx[i2][j2] - sumx[i2][j3] - sumx[i3][j2] + sumx[i3][j3];
		sy = sumy[i2][j2] - sumy[i2][j3] - sumy[i3][j2] + sumy[i3][j3];
		s = sum[i2][j2] - sum[i2][j3] - sum[i3][j2] + sum[i3][j3];
	}
	
	//printf("%lld %lld %lld %lld\n",sum[i2][j2], sum[i2][j3], sum[i3][j2],sum[i3][j3]);
	//printf("%d %d %d\n",i,j,k);
	//printf("%lld %lld %lld %lld\n",i2,j2,i3,j3);
	//printf("%lld %lld %lld (%lld %lld)\n",sx,sy,s,cx,cy);
	//fflush(stdout);
		
	sx -= (LL)tab[i2][j2] * i2 * ((k%2)==0?2:1);
	sx -= (LL)tab[i2][j4] * i2 * ((k%2)==0?2:1);
	sx -= (LL)tab[i4][j2] * i4 * ((k%2)==0?2:1);
	sx -= (LL)tab[i4][j4] * i4 * ((k%2)==0?2:1);
	sy -= (LL)tab[i2][j2] * j2 * ((k%2)==0?2:1);
	sy -= (LL)tab[i2][j4] * j4 * ((k%2)==0?2:1);
	sy -= (LL)tab[i4][j2] * j2 * ((k%2)==0?2:1);
	sy -= (LL)tab[i4][j4] * j4 * ((k%2)==0?2:1);
	s -= (LL)tab[i2][j2];
	s -= (LL)tab[i2][j4];
	s -= (LL)tab[i4][j2];
	s -= (LL)tab[i4][j4];
	
	if (LL(cx)*s!=sx) return false;
	if (LL(cy)*s!=sy) return false;		
	
	return true;	
}

char buff[509];
void solve() {
	R=nint();
	C=nint();
	int D=nint();
	
	FOR(i,0,R)
	FOR(j,0,C){
		sum[i][j]=sumx[i][j]=sumy[i][j]=0;	
	}
	
	scanf(" \n");
	FOR(i,1,R)
	{
		gets(buff);
		FOR(j,1,C)
		{
			tab[i][j] = D + (buff[j-1]-'0');
		}
	}
		
	FOR(i,1,R)
	FOR(j,1,C){
		sum[i][j] = tab[i][j] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1];
		sumx[i][j] = (tab[i][j] * i) + sumx[i-1][j] + sumx[i][j-1] - sumx[i-1][j-1];
		sumy[i][j] = (tab[i][j] * j) + sumy[i-1][j] + sumy[i][j-1] - sumy[i-1][j-1];
	}
	
	
	//printf("%d\n",check(4,4,5));
	
	
	int best=0;
	FOR(i,1,R)
	FOR(j,1,C) 
	FOR(k,3,500)
		if (check(i,j,k)) best = max(best,k);

	if(best!=0)printf("%d\n",best);	
	else printf("IMPOSSIBLE\n");
}

int main() {
	int tests;
	scanf("%d\n",&tests);
	FOR(test,1,tests) {
		printf("Case #%d: ", test);
		solve();
	}
	return 0;
}

















