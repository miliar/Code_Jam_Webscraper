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
		
		int n;
		int tab[100];
		char t[100];

		scanf("%d",&n);

		fu(a,n){
			scanf("%s",t);
			tab[a] = 0;
			for(int b=n-1; b>=0 ; b--){
				if( t[b] == '1' ){ tab[a] = b; break; }	
			}
		}

		bool v[100];
		memset(v,0,sizeof v);
		
		int res = 0;

		fu(a,n*n){
			fu(b,n-1) if( tab[b] > b ){
				int c=b+1;
				for( ; c < n && tab[c] > b ; c++);
				res += c-b;
				for( ; c > b ; c--) swap( tab[c], tab[c-1]); 
			}
		}

		printf("%d\n",res);
	}

	return 0;
}
