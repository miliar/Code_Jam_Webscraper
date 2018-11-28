#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <sstream>
#define sz size()
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define fu(i,n) for(int i=0; i<(n); i++)
#define ALL(a) (a).begin(),(a).end()
typedef long long ll;

using namespace std;

int ileTestow, bonus, ileA, ileB;
char tmp[10];

int main(){
	
	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		scanf("%d",&bonus);
		scanf("%d%d",&ileA,&ileB);

		multimap<int, pair<int,int> > mapa; mapa.clear();

		for(int a=0; a<ileA; a++){
			scanf("%s",tmp);
			int skad=((tmp[0]-'0')*10 + (tmp[1]-'0'))*60 + (tmp[3]-'0')*10 + (tmp[4]-'0');
			scanf("%s",tmp);
			int dokad=((tmp[0]-'0')*10 + (tmp[1]-'0'))*60 + (tmp[3]-'0')*10 + (tmp[4]-'0');
			mapa.insert( mp(skad, mp(1,dokad)) );
		}

		for(int a=0; a<ileB; a++){
			scanf("%s",tmp);
			int skad=((tmp[0]-'0')*10 + (tmp[1]-'0'))*60 + (tmp[3]-'0')*10 + (tmp[4]-'0');
			scanf("%s",tmp);
			int dokad=((tmp[0]-'0')*10 + (tmp[1]-'0'))*60 + (tmp[3]-'0')*10 + (tmp[4]-'0');
			mapa.insert( mp(skad, mp(2,dokad)) );
		}

		int pA=0,pB=0;
		vector<int> p1; p1.clear();
		vector<int> p2; p2.clear();

		multimap<int, pair<int,int> >::iterator it=mapa.begin();
		for( ; it!=mapa.end(); it++){
			int skad=it->first;
			int gdzie=it->second.first;
			int dokad=it->second.second;

			if( gdzie == 1 ){
				if( p1.empty() || p1[0] > skad ){
					pA++;
					p2.pb( dokad+bonus ); 
					sort(ALL(p2));
				} else {
					swap( p1[0], p1[ p1.sz-1 ] );
					p1.pop_back();
					sort(ALL(p1));

					p2.pb( dokad+bonus ); 
					sort(ALL(p2));
				}
			} else {
				if( p2.empty() || p2[0] > skad ){
					pB++;
					p1.pb( dokad+bonus ); 
					sort(ALL(p1));
				} else {
					swap( p2[0], p2[ p2.sz-1 ] );
					p2.pop_back();
					sort(ALL(p2));

					p1.pb( dokad+bonus ); 
					sort(ALL(p1));
				}
			}
		}

		printf("Case #%d: %d %d\n",q,pA,pB);
	}

	return 0;
}
