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

int main(){

	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		printf("Case #%d: ",q);

		int h,w,r,x2[100],y2[100];

		cin >> h >> w >> r;

		fu(a,r) cin >> y2[a] >> x2[a];
		
		int x[100000], y[100000], lewy=0, prawy=1;
	    int	v[200][200];
		fu(a,200) fu(b,200) v[a][b] = 0;	
		
		ll score = 0;
		v[1][1] = 1;
		x[0] = 1; y[0] = 1;

		bool ok;

		while( lewy < prawy ){
			//cout << lewy << " : " << x[lewy] << " : " << y[lewy] << endl;
			if( x[lewy] == w && y[lewy] == h ) score++;
			else {
				if( x[lewy]+2 <= w && y[lewy]+1 <= h ){ 
					ok = true;	
					fu(a,r) if( x[lewy]+2 == x2[a] && y[lewy]+1 == y2[a] ){ ok=false; }
					if( ok ){
					if( v[ y[lewy]+1 ][ x[lewy]+2 ] == 0 ){ 
							x[prawy] = x[lewy]+2; y[prawy] = y[lewy]+1; prawy++; 
					}
					v[ y[lewy]+1 ][ x[lewy]+2 ] = ( v[ y[lewy]+1 ][ x[lewy]+2 ] + v[y[lewy]][x[lewy]] )%10007;		
					}
				}

				if( x[lewy]+1 <= w && y[lewy]+2 <= h ){ 
					ok = true;
					fu(a,r) if( x[lewy]+1 == x2[a] && y[lewy]+2 == y2[a] ){ ok=false; }
					if( ok ){
					if( v[ y[lewy]+2 ][ x[lewy]+1 ] == 0 ){ 
							x[prawy] = x[lewy]+1; y[prawy] = y[lewy]+2; prawy++;
					} 
					v[ y[lewy]+2 ][ x[lewy]+1 ] = ( v[ y[lewy]+2 ][ x[lewy]+1 ] + v[y[lewy]][x[lewy]] )%10007;	
					}
				}
				v[y[lewy]][x[lewy]]=0;
			}
			lewy++;
		}

		cout << v[h][w]%10007 << endl;
		
	}

	return 0;
}
