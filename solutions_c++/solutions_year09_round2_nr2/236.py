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
		char c;
		while( ((c=getchar()) < '0' || c > '9') && c != EOF );
		
		vi res;
		res.pb( c-'0' );
		while( (c=getchar()) >= '0' && c <= '9') res.pb( c-'0' );
		
		cout << "Case #" << q << ": ";
		bool ok = false;
		while( next_permutation(ALL(res)) ){
			if( res[0] == 0 ) continue;
			ok = true;
			break;
		}

		if( ok ){
			fu(a,res.sz) cout << res[a];
			cout << endl;	
		} else {
			res.pb(0);
			sort(ALL(res));
			if( res[0] == 0 ){
					fu(a,res.sz) if( res[a] != 0 ){
						swap(res[0],res[a]);
						break;		
					}

			}
			fu(a,res.sz) cout << res[a];
			cout << endl;
		}
	}

	return 0;
}
