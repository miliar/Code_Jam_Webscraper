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

int ileTestow;
int N, M;

set<string> mapa;

vector<string> split( string nazwa ){
	vector<string> tmp;
	string tmp2 = "";
	fu(a,nazwa.sz){
		if( nazwa[a] == '/' ){
			if( tmp2 != "" ) tmp.pb( tmp2 );
			tmp2 = "";
		} else {
			tmp2 += nazwa[a];
		}
	}
	if ( tmp2 != "" ) tmp.pb( tmp2 );
	return tmp;
}

int main(){

	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		printf("Case #%d: ",q);
		
		scanf("%d%d",&N,&M);
		mapa.clear();
		
		string nazwa;

		fu(a,N){
			cin >> nazwa;		

			vector<string> tmp = split(nazwa);

			string s = "";
			fu(b,tmp.sz){
				s = s + "/" + tmp[b];
				mapa.insert( s );
			}
		}
	
		int res = 0;
	
		fu(a,M){
			cin >> nazwa;

			vector<string> tmp = split(nazwa);

			string s = "";
			fu(b,tmp.sz){	
				s = s + "/" + tmp[b];
				if( mapa.find( s ) == mapa.end() ){
					mapa.insert( s );
					res++;
				}
			}
		}

		printf("%d\n", res);
	}

	return 0;
}
