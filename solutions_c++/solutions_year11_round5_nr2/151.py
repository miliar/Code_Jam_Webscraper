#include <algorithm>
#include <cstdlib>
#include <cstdarg>
#include <cassert>
#include <cstring>
#include <complex>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>

using namespace std;

typedef long long i64;
typedef long double d64;

#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()

#define pb push_back
#define mp make_pair

#define eprintf(...) {fprintf(stderr,__VA_ARGS__),fflush(stderr);}

#define forn(i,n) for( int i = 0 ; i < (n) ; i++ )
#define forit(it,c) for( __typeof((c).begin()) it = (c).begin() ; it != (c).end() ; it++ )

#ifdef WIN32
#define INT64 "%I64d"
#else
#define INT64 "%lld"
#endif

const int maxn = 1<<10;

int card[maxn];
int size[maxn],last[maxn];


int main(){
	int T;
	scanf("%d",&T);
	for(int id = 1 ; id <= T ; id++ ){
		int n;
		scanf("%d",&n);
		forn(i,n) scanf("%d",&card[i]);
		sort(card,card+n);
		int deck = 0;
		for(int i = 0 ; i < n ; i++ ){
			int go = -1;
			for(int j = 0 ; j < deck ; j++ ){
				if(last[j]==card[i]-1){
					if(go==-1||size[go]>size[j]) go = j;
				}
			}
			if(go!=-1){
				size[go]++;
				last[go]=card[i];
			}else{
				size[deck]=1;
				last[deck]=card[i];
				deck++;
			}
		}
		int res = n;
		for(int i = 0 ; i < deck ; i++ ) res = min(res,size[i]);
		printf("Case #%d: %d\n",id,res);
	}
	return 0;
}
