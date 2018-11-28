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
int prev[1000010];
int way[1000010];
int v[1000010];

int main(){

	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		printf("Case #%d: ",q);
		
		int dl, chod, bieg, t, N;
		scanf("%d%d%d%d%d", &dl, &chod, &bieg, &t, &N);
		
		multimap< int, pair<int,int> > mapa;

		fu(a,N){
			int b, e, w;
			scanf("%d%d%d", &b, &e, &w);

			mapa.insert( mp(e, mp(b,w)) );
		}
		
		prev[0] = -1;
		way[0] = 0;
		v[0] = 0;

		multimap< int, pair<int,int> >::iterator it = mapa.begin();
		for(int gdzie=1; gdzie<=dl; gdzie++){
			prev[gdzie] = gdzie-1;
			way[gdzie] = 0;
			v[gdzie] = v[gdzie-1];
			
			while( it != mapa.end() && it->first == gdzie ){
				int e = it->first;
				int b = it->second.first;
				int w = it->second.second;
				if( v[gdzie] < v[b] + (e-b) * w ){
					v[gdzie] = v[b] + (e-b) * w;		
					way[gdzie] = w;
					prev[gdzie] = b;
				}

				it++;
			}
		}
		
		double res = 0.0;
		double czas = t;
		int gdzie = dl;

		multimap< int, int > mapa2;

		while( gdzie > 0 ){
			int predkosc = way[gdzie];
			int dokad = prev[gdzie];
			int odl = gdzie - dokad;	

			mapa2.insert( mp( predkosc, odl ) );
	/*	
cerr << "gdzie: " << gdzie << " dokad: " << dokad << " czas: " << czas << " ### " << res << endl;
			
			if( czas > 0 ) {
				if( (double) odl / (predkosc+bieg) <= czas ){
					czas -= (double) odl / (predkosc+bieg);
					res += (double) odl / (predkosc+bieg);
				} else {
					double droga = czas * (predkosc+bieg);

cerr << "### droga: " << droga << " left: " << (double)(odl-droga) << endl;
				
					res += czas + (double) (odl - droga) / (predkosc+chod);
					czas = 0;
				}
			} else {
				res += (double) odl / (predkosc + chod);
			}
	*/

			gdzie = dokad;
		}
		
		multimap< int, int >::iterator it2 = mapa2.begin();

		for( ; it2 != mapa2.end() ; it2++){
			int predkosc = it2->first;
			int odl = it2->second;

			if( czas > 0 ){
				if( (double) odl / (predkosc+bieg) <= czas ){
					czas -= (double) odl / (predkosc+bieg);
					res += (double) odl / (predkosc+bieg);
				} else {
					double droga = czas * (predkosc+bieg);
					res += czas + (double) (odl - droga) / (predkosc+chod);
					czas = 0;
				}
			} else {
				res += (double)odl / (predkosc+chod);
			}
		}

		printf("%.7f\n", res);
	}

	return 0;
}
