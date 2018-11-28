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
ll tab[1000000], sum[1000000];

int main(){
	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		printf("Case #%d: ",q);
		
		ll L, t, N, C;
		scanf("%lld%lld%lld%lld", &L, &t, &N, &C);

		fu(a,C){
			scanf("%lld", &tab[a]);
		}

		ll res = 0;
		multiset<ll> secik;
	
		int gdzie = 0;
		fu(a,N){
			tab[a] = tab[gdzie++];
			sum[a] = tab[a];

			if( a > 0 ){
				sum[a] += sum[a-1];
			}

			if( (ll)sum[a] >= (ll)t/2 ){
				ll start = (ll)sum[a] - (ll)tab[a];

				if( (ll)start >= (ll)t/2 ){ // 1
					secik.insert( -(ll)tab[a] );
				} else { //2 
					ll d1 = (ll)t/2 - (ll)start;
					ll d2 = (ll)tab[a] - (ll)d1;
//cerr << "tab[a]: " << tab[a] << " start: " << start << " d1: " << d1 << " d2: " << d2 << endl;
					secik.insert( -(ll)d2 );
				}
			}

			if( gdzie >= C ) 
				gdzie = 0;

			res = (ll) res + (ll)tab[a] * 2LL;
		}
		
		//cerr << endl;
		//cerr << "res: " << res << endl;

		multiset<ll>::iterator it = secik.begin();
		for(int a=0; a<L && it!=secik.end(); a++, it++){
			//cerr << "*it => " << *it << endl;

			res += *it;	
		}

		printf("%lld\n", res);
	}

	return 0;
}
