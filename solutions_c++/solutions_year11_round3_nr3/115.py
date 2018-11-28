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
		
		int N, L, H;
		int tab[1000];

		scanf("%d%d%d", &N, &L, &H);

		fu(a,N){
			scanf("%d", &tab[a]);
		}

		int res = -1;

		for(int a=L; a<=H; a++){
			bool ok = true;
			fu(b,N){
				if( tab[b] % a != 0 && a % tab[b] != 0 ){
					ok = false;
					break;
				}
			}
			if( ok ){
				res = a;
				break;
			}
		}

		if( res == -1 ){
			printf("NO\n");
		} else {
			printf("%d\n", res);
		}
	}

	return 0;
}
