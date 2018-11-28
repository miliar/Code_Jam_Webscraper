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
		
		int C, D, N;

		int cc[26][26];
		memset(cc,-1,sizeof cc);

		bool oposed[26][26];
		memset(oposed,0,sizeof oposed);

		int ile[26];
		memset(ile,0,sizeof ile);

		scanf("%d", &C);
		fu(a,C){
			string tmp;
			cin >> tmp;

			cc[ tmp[0]-'A' ][ tmp[1]-'A' ] = tmp[2]-'A';
			cc[ tmp[1]-'A' ][ tmp[0]-'A' ] = tmp[2]-'A';
		}

		scanf("%d", &D);
		fu(a,D){
			string tmp;
			cin >> tmp;

			oposed[ tmp[0]-'A' ][ tmp[1]-'A' ] = true;
			oposed[ tmp[1]-'A' ][ tmp[0]-'A' ] = true;
		}

		vi res;

		scanf("%d", &N);
		string tmp;
		cin >> tmp;

		for(int a=0; a<tmp.sz; a++){
			res.pb( tmp[a]-'A' );

			if( res.sz < 2 ) continue;

			if( cc[ res[res.sz-2] ][ res[res.sz-1] ] >= 0 ){
				res[ res.sz-2 ] = cc[ res[res.sz-2] ][ res[res.sz-1] ];
				res.pop_back();
			} else {
				bool ok = false;
				
				fu(b,res.sz-1) if( oposed[ res[b] ][ res[res.sz-1] ] ){
					ok = true;
					break;
				}

				if( ok ){
					res.clear();
					memset(ile,0,sizeof ile);
					continue;
				}
			}
		}

		printf("[");
		fu(a,res.sz){
			printf("%c", (char)(res[a]+'A'));

			if( a+1 < res.sz ) printf(", ");
		}
		printf("]\n");
	}

	return 0;
}
