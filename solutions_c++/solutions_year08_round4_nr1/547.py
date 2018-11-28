#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <memory>
#define sz size()
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define fu(i,n) for(int i=0; i<(n); i++)
#define ALL(a) (a).begin(),(a).end()
#define cl(a,co) memset(a,co,sizeof a)
#define un(a) sort(ALL(a)),a.erase( unique(ALL(a)), a.end() )
typedef long long ll;
//istringstream is(s); is >> a;

using namespace std;

struct Data {
	int typ, ok;
	int wart;
};
Data d[10001];

int ileTestow, ile, kolor;

bool dfs( int gdzie ){
	if( d[gdzie].wart != -1 ) return d[gdzie].wart;
	bool lewy=dfs(gdzie*2), prawy=dfs(gdzie*2+1);
	if( d[gdzie].typ==1 ){
		if( lewy == 1 && prawy == 1 ) return (d[gdzie].wart=1);
		return (d[gdzie].wart=0);
	} 
	if( lewy == 1 || prawy == 1 ) return (d[gdzie].wart=1);
	return (d[gdzie].wart=0);
}

int barwa( int gdzie ){
	if( gdzie <= ile ) return d[gdzie].wart;
	return -1;
}

int popraw( int gdzie, int kolor ){
	if( d[gdzie].wart == kolor ) return 0;
	if( gdzie > (ile-1)/2 ) return -1;
	if( d[gdzie].ok == 1 ){
		if( kolor == 0 ){ // ma byc 0 jest 1 
			if( d[gdzie].typ == 0 ){
				if(barwa(gdzie*2)==0||barwa(gdzie*2+1)==0) return 1;
				int lewy = popraw( gdzie*2, 0 );
				int prawy = popraw( gdzie*2+1, 0 );
				if( lewy != -1 && prawy != -1 ) return 1+min(lewy,prawy);
				if( lewy != -1 ) return 1+lewy;
				if( prawy != -1 ) return 1+prawy;
				return -1;
			} else if( d[gdzie].typ == 1) {
				int lewy = popraw( gdzie*2, 0 );
				int prawy = popraw( gdzie*2+1, 0 );
				if( lewy != -1 && prawy != -1 ) return min(lewy,prawy);
				if( lewy != -1 ) return lewy;
				if( prawy != -1 ) return prawy;
				return -1;
			}
		} else { // ma byc 1 jest 0 
			if( d[gdzie].typ == 0 ){
				int lewy = popraw( gdzie*2, 1 );
				int prawy = popraw( gdzie*2+1, 1 );
				if( lewy != -1 && prawy != -1 ) return min(lewy,prawy);
				if( lewy != -1 ) return lewy;
				if( prawy != -1 ) return prawy;
				return -1;
			} else if( d[gdzie].typ == 1 ){
				if(barwa(gdzie*2)==1||barwa(gdzie*2+1)==1) return 1;
				int lewy = popraw( gdzie*2, 1 );
				int prawy = popraw( gdzie*2+1, 1 );
				if( lewy != -1 && prawy != -1 ) return 1+min(lewy,prawy);
				if( lewy != -1 ) return 1+lewy;
				if( prawy != -1 ) return 1+prawy;
				return -1;
			}
		}
	} else if( d[gdzie].ok == 0 ){
		if( kolor == 0 ){
			if( d[gdzie].typ == 0 ){
				int lewy = popraw( gdzie*2, 0 );
				int prawy = popraw( gdzie*2+1, 0 );
				if( lewy != -1 && prawy != -1 ) return lewy+prawy;
				return -1;
			} else if( d[gdzie].typ == 1){
				int lewy = popraw( gdzie*2, 0 );
				int prawy = popraw( gdzie*2+1, 0 );
				if( lewy != -1 && prawy != -1 ) return min(lewy,prawy);
				if( lewy != -1 ) return lewy;
				if( prawy != -1 ) return prawy;
				return -1;
			}
		} else {
			if( d[gdzie].typ == 0 ){
				int lewy = popraw( gdzie*2, 1 );
				int prawy = popraw( gdzie*2+1, 1 );
				if( lewy != -1 && prawy != -1 ) return min(lewy,prawy);
				if( lewy != -1 ) return lewy;
				if( prawy != -1 ) return prawy;
				return -1;
			} else if( d[gdzie].typ == 1){
				int lewy = popraw( gdzie*2, 1 );
				int prawy = popraw( gdzie*2+1, 1 );
				if( lewy != -1 && prawy != -1 ) return lewy+prawy;
				return -1;
			}
		}
	}
	return -1;
}

int main(){
	
	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		scanf("%d%d",&ile,&kolor);

		fu(a,ile) d[a+1].wart = d[a+1].typ = d[a+1].ok = -1;

		fu(a,(ile-1)/2) scanf("%d%d",&d[a+1].typ,&d[a+1].ok);
		fu(a,(ile+1)/2) scanf("%d",&d[(ile-1)/2+a+1].wart);

		bool root = dfs(1);

		//fu(a,ile) cerr << a+1 << " typ:" << d[a+1].typ << " ok:" << d[a+1].ok << " wart:" << d[a+1].wart << endl;

		int score = popraw(1,kolor);

		if( score >= 0 ) printf("Case #%d: %d\n",q,score);
		else printf("Case #%d: IMPOSSIBLE\n",q);
	}

	return 0;
}
