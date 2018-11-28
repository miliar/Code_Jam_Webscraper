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
		char tab[550], c;
		int n = 0;

		while( ((c=getchar()) < 'a' || c > 'z') && c != EOF );
		
		tab[ n++ ] = c;
		
		while( ((c=getchar()) >= 'a' && c <= 'z') || c == ' ' ) tab[n++] = c;
	
		string pattern = "maj edoc ot emoclew";

		int res[550];
		
		fu(a,n) if( tab[a] == 'm' ) res[a] = 1; else res[a] = 0;

		fu(a,pattern.sz){
			fu(b,n) 
				if( tab[b] == pattern[a] ){
					if( a == 0 ){
						res[b] = 1;		
					} else {
						res[b] = 0;
						for(int c=b+1; c<n; c++) if( tab[c] == pattern[a-1] ) res[b] += res[c];
						res[b] %= 10000;
					}
				} else {
					res[b] = 0;
				}
		}

		int score = 0;
		fu(a,n) score = (score + res[a]) % 10000;
		
		if( score < 10 ) printf("Case #%d: 000%d\n",q,score);
		else if( score < 100 ) printf("Case #%d: 00%d\n",q,score);
		else if( score < 1000 ) printf("Case #%d: 0%d\n",q,score);
		else printf("Case #%d: %d\n",q,score);
	}

	return 0;
}
