#include <algorithm>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
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
inline int next_int() { int x; scanf("%d",&x); return x; }
#define all(A) (A).begin(),(A).end()
#define st first
#define nd second
#define mp make_pair
#define pb push_back

int tab[1000][1000];
char buff[1000];

double wp[1000];
double owp[1000];
double aowp[1000];

int ile_win[1000];
int total[1000];

void solve() {	
	int n;
	scanf("%d\n",&n);
	FOR(i,1,n)
	FOR(j,1,n)
		tab[i][j] = 0;
	FOR(i,1,n){
		gets(buff);
		FOR(j,1,n){
			if(buff[j-1] == '.') continue;
			if(buff[j-1] == '1') tab[i][j] = 1; else tab[i][j] = -1;
		}	
	}
	
	FOR(i,1,n){
		wp[i]=0;
		ile_win[i]=0;
		total[i]=0;
		
		FOR(j,1,n){
			if(j==i)continue;
			if(tab[i][j]==1){ ++total[i]; ++ile_win[i]; }
			else if(tab[i][j]==-1){ ++total[i]; }
		}
		
		wp[i] = double(ile_win[i])/double(total[i]);		
	}
	
	FOR(i,1,n){
		owp[i] = 0;
		int il=0;
		FOR(j,1,n){
			if(j==i) continue;
			if(tab[i][j]==0)continue;
			int ilew=ile_win[j] - (tab[j][i]==1?1:0);
			int tot=total[j] - (tab[j][i]!=0?1:0);
			double tempwp=double(ilew)/double(tot);
			owp[i] += tempwp;
			++il;
		}
		owp[i] /= il;
	}
	
	FOR(i,1,n){
		aowp[i]=0;
		int il=0;
		FOR(j,1,n){
			if(i==j)continue;
			if(tab[i][j]==0)continue;
			aowp[i] += owp[j];
			++il;
		}
		aowp[i] /= il;
	}
	
	FOR(i,1,n){
		double wynik = 0.25*wp[i] + 0.5*owp[i] + 0.25 *aowp[i];
		printf("%.10lf\n",wynik);
	}	
}

int main() {
	int tests=next_int();
	FOR(test,1,tests){
		printf("Case #%d:\n",test);
		solve();
	}
	return 0;
}



















