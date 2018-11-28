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
		printf("Case #%d:\n",q);
			
		int r, c;
		char tab[100][100];
		bool ok = true;
		
		scanf("%d%d", &r, &c);
		
		fu(a,r){
			scanf("%s", tab[a]);		
		}
		
		fu(a,r){
			fu(b,c){
				if( tab[a][b] == '#' ){
					if( a+1 < r && b+1 < c && tab[a+1][b] == '#' && tab[a][b+1] == '#' && tab[a+1][b+1] == '#' ){
						tab[a][b] = '/';
						tab[a+1][b] = '\\';
						tab[a][b+1] = '\\';			
						tab[a+1][b+1] = '/';
					} else {
						ok = false;
					}
				}
			}
		}
		
		if( ok ){
			fu(a,r){
				printf("%s\n", tab[a]);		
			}
		} else {
			printf("Impossible\n");
		}
	}

	return 0;
}
