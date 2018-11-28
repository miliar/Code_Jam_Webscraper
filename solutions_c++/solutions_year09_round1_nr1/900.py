// By mirosuaf v.2.1 modified for CodeJam
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(f,w) ({ bool _ok=true; f _ok=_ok && (w); _ok; })
#define EXISTS(f,w) (!ALL(f,!(w)))
typedef long long LL;
typedef vector<int> VI; 

LL changeBase(int x,int baza) {
//	cout << "CHANGE " << x << " B= " << baza << endl;
	LL res=0;
	while (x>0) {
		res*=10;
		res+=(x%baza);
		x/=baza;
	}
	LL rres=0;
	while (res>0) {
		rres*=10;
		rres+=res%10;
		res/=10;
	}
	return rres;
}

LL przesumuj(LL x) {
	int wynik=0;
	while (x>0) {
		wynik+=(x%10)*(x%10);
		x/=10;
	}
	return wynik;
}

int main() {
	LL INF = 1000000000LL*1000000000;
	int KONIEC = 50000;

	int wyni[1000];
	int liczba=224;
	REP(liczba,512) if (__builtin_popcount(liczba)>=2 && __builtin_popcount(liczba)<=3) {
		VI list;
		int tmp=liczba;
		REP(i,10) if ((tmp|(1<<i))==tmp) list.push_back(i+2);
//		REP(i,list.size()) cout << list[i] << " "; cout << endl; 
	
		FOR(start,2,KONIEC) {
			bool niet=false;
			REP(i,list.size()) {
				LL val=changeBase(start,list[i]);
				LL poprz=INF;
				REP(ii,100) {
//				while (val<poprz) {
					poprz=val;
					val=changeBase(przesumuj(val),list[i]);
				}
				if (val!=1) {
					i=list.size();
					niet=true;
				}
			}
			if (!niet) {
				REP(i,list.size()) cout << list[i] << " "; cout << "-->"; 
				cout  << start << endl;
				wyni[liczba]=start;
				start=KONIEC;
			}
		}
		if (wyni[liczba]==0) cout << "!!!!!!!!!!!!!!!!!!!!!!!!!!" << endl;
	}

		char ch[10000];
	int ile;
	scanf("%d",&ile);gets(ch);
	FOR(iile,1,ile) {
		gets(ch);
		string tmp=ch;
		stringstream aa;
		aa<<tmp;
		int x=-1,y=-1,z=-1;
		aa>>x>>y>>z;
//		cout << x << " " << y << " " << z << endl;
		int rr=((1<<(x-2))|(1<<(y-2)));
				if (z!=(-1)) rr|=(1<<(z-2));
		int res=wyni[rr];				


		printf("Case #%d: %d\n",iile,res);
	}
	
	return 0;
}

