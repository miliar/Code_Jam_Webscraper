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

bool ok2(int y, int x ){
	if( y < 0 || x < 0 ) return false;
	return true;
}

int ileTestow;

int main(){

	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		printf("Case #%d: ",q);
		
		bool v[100][100];
		memset(v,0,sizeof v);
		
		int ile;
		scanf("%d",&ile);
		
		fu(a,ile){
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1, &y1, &x2, &y2);
			x1--;
			y1--;
			x2--;
			y2--;
			for(int b=x1; b<=x2; b++) 
				for( int c=y1; c<=y2; c++)
					v[c][b] = 1;
		}

		int res = 0;
		while( ++res ){
			bool v2[100][100];
			fu(a,100) fu(b,100) {
				if( v[a][b] ){
					v2[a][b] = 1;
					if( (!ok2(a-1,b) || !v[a-1][b]) && (!ok2(a,b-1) || !v[a][b-1]) ) v2[a][b] = 0;
				} else {
					v2[a][b] = 0;
					if( (ok2(a-1,b) && v[a-1][b]) && (ok2(a,b-1) && v[a][b-1]) ) v2[a][b] = 1;
				}
			}
			
			bool ok = false;
			fu(a,100) fu(b,100){
					 v[a][b] = v2[a][b];
				if( v[a][b] ) ok = true;
			}
			if (!ok) break;
		}
		
		printf("%d\n",res);
	}

	return 0;
}
