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
int tab[25];

int main(){

	scanf("%d",&ileTestow);

/*	
	for(int q=1; q<=ileTestow; q++){
		printf("Case #%d: ",q);
	
		int N;
		scanf("%d",&N);
		N--;
		int res = 0;
		
		fu(a,(1<<N)){
			memset(tab,-1,sizeof tab);
			int rank = 0;

			fu(b,N) if( a & (1<<b) ){
				tab[b] = rank++;
			}
			
			if( tab[ N-1 ] == -1 ) continue;

//fu(b,N) cerr << tab[b] << " "; cerr << endl;

			int gdzie = tab[ N-1 ];
			while( gdzie > 0 ){
				gdzie = tab[ gdzie-1 ];
			}

			if( gdzie == 0 ){
				res++;
//cerr << "OK" << endl;
			}

		}
				
		printf("%d\n",res);
	}

	*/

	int res[] = { 
984911,
513350,
268066,
140268,
73562,
38674,
20388,
10780,
5719,
3045,
1628,
874,
472,
256,
140,
77,
43,
24,
14,
8,
5,
3,
2,
1
			};
	for(int q=1; q<=ileTestow; q++){
		printf("Case #%d: ",q);
		int N;
		scanf("%d",&N);

		N-=2;
		N = 23 - N;

		printf("%d\n", res[N] % 100003);	
	}

	return 0;
}
