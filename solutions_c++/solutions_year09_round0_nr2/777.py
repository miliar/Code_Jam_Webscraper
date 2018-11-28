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
int t[105][105];
int res[105][105];
int bx[] = {0,-1,1,0};
int by[] = {-1,0,0,1};

int main(){

	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		int wys,sze, ile=0;
		scanf("%d%d",&wys,&sze);
	
		vector< pair<int, pair<int,int> > > mapa; mapa.clear();

		fu(a,wys) fu(b,sze){
			scanf("%d",&t[a][b]);
			mapa.pb( mp(t[a][b], mp(a,b) ) );
		}
		
		sort(ALL(mapa));

		memset(res,-1,sizeof res);

		fu(a,mapa.sz){
			int h = mapa[a].first;
			int y = mapa[a].second.first;
			int x = mapa[a].second.second;
		

			int gdziex, gdziey=-1;	
			fu(b,4) if( y+by[b] >= 0 && y+by[b] < wys && x+bx[b] >= 0 && x+bx[b] < sze ){
				if( t[y][x] >  t[y+by[b]][x+bx[b]] ){
					if( gdziey == -1 || t[y+by[b]][x+bx[b]] < t[ gdziey ][ gdziex ] ){
						gdziey = y + by[b];
						gdziex = x + bx[b];
					}
				}
			}

			if( gdziey == -1 || res[ gdziey ][ gdziex ] == -1 ){
				res[ y ][ x ] = ile++;
			} else {
				res[ y ][ x ] = res[ gdziey ][ gdziex ];
			}
		}
		
		int ile2 = 0, mapa2[30];
		memset(mapa2,-1,sizeof mapa2);
			
		printf("Case #%d:\n",q);
		fu(a,wys){
			fu(b,sze){
				if( mapa2[ res[a][b] ] == -1 ){
					mapa2[ res[a][b] ] = ile2++;
				} 
				printf("%c ",(char)(mapa2[ res[a][b] ]+'a'));
			}
			printf("\n");
		}
	}

	return 0;
}
