// {{{
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <complex>
#include <stack>
#include <cmath>
#include <iostream>
#include <sstream>
#include <cctype>
#include <cstdlib>
#include <utility>
#include <bitset>
#include <assert.h>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VII;
typedef vector<string> VS;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PI;
typedef pair<LD,LD> PD;

#define VAR(v,n) __typeof(n) v=(n)
#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a); i<=(b); i++)
#define FORD(i,a,b) for(int i=(a); i>=(b); i--)
#define FORE(i,c) for(VAR(i,(c).begin()); i!=(c).end(); i++)
#define CLR(A,v) memset((A),v,sizeof((A)))

#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define ALL(x) x.begin(),x.end()
#define SIZE(x) ((int)(x).size())
// }}}

#define M 1005

int R,k,n;
int T[M];
int kiedy[M],ile[M];
int wynik[M];


int main() {
	int test,number=0;
	scanf("%d",&test);
	while (test--) {
		printf("Case #%d: ",++number);
		scanf("%d%d%d",&R,&k,&n);
		REP(i,n) scanf("%d",&T[i]);

		REP(i,n) kiedy[i]=-1;

		int x=0,akt=0,s,e;
		while (kiedy[x]==-1) {
			kiedy[x]=akt;
			s=0,e=0;
			while (e<n && T[(x+e)%n]+s<=k)
				s+=T[(x+e)%n],e++;
			ile[x]=e,wynik[x]=s;
			x=(x+e)%n;
			akt++;
		}

		/* mamy cykl */
		int d=akt-kiedy[x];

		int y=0;
		LL res=0LL;
		while (R>0 && y!=x)
			res+=(LL)wynik[y],y=(y+ile[y])%n,R--;

		LL w=0LL;
		REP(i,d) w+=(LL)wynik[y],y=(y+ile[y])%n;

		res+=((LL)(R/d))*w;
		R%=d;

		REP(i,R) res+=wynik[y],y=(y+ile[y])%n;

		printf("%lld\n",res);
	}
	return 0;
}
