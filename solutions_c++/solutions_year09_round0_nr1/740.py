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

int L, D, N;
char lang[5100][20];

int main(){

	scanf("%d%d%d",&L,&D,&N);
	
	fu(a,D){
		scanf("%s",lang[a]);
	}
	
	char pattern[500];
	int n;
	bool v[20][26];

	fu(a,N){
		scanf("%s",pattern);

		n = strlen(pattern);
		memset(v,0,sizeof v);
		
		bool in = 0;	
		int gdzie = 0;	
		fu(b,n){
			if( pattern[b] == '(' ){
				in = 1;
				continue;
			} else if( pattern[b] == ')' ){
				in = 0;
				gdzie ++;
			} else {
				v[gdzie][ pattern[b] - 'a' ] = 1;
				if( !in ) gdzie++;
			}
		}

		int res = 0;
		fu(c,D){
			bool ok = true;
			fu(b,L){
				if( v[b][ lang[c][b] - 'a' ] == 0 ){
					ok = false;
					break;
				}
			}
			if( ok ) res++;		
		}

		printf("Case #%d: %d\n",a+1,res);
	}

	return 0;
}
