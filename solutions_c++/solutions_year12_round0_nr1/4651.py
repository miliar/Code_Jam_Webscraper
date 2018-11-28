#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdarg>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>

using namespace std;

typedef long long LL;
typedef long double LD;

#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define y1 y1_gedjcdgfce
#define y0 y0_sadasdasdsa
#define ws ws_sadsadsada
#define left left_asdsadsadsadsa
#define right right_asdasdsadasda
#define hash hash_asdasdasdsad

#ifdef DEBUG
#define eprintf(...) {fprintf(stderr,__VA_ARGS__),fflush(stderr);}
#else
#define eprintf(...) {}
#endif

#define forn(i,n) for( int i = 0 ; i < (n) ; i++ )
#define forit(it,c) for( __typeof((c).begin()) it = (c).begin() ; it != (c).end() ; it++ )

#ifdef WIN32
#define INT64 "%I64d"
#else
#define INT64 "%lld"
#endif

#define TASK "task"

map<char,char> F,invF;
 
int main(){
	#ifdef DEBUG
	assert(freopen(TASK".in","rt",stdin));
	assert(freopen(TASK".out","wt",stdout));
	#endif
	string in = string("our language is impossible to understand") + 
				string("there are twenty six factorial possibilities") + 
				string("so it is okay if you want to just give up") + 
				string("aozq");
	string out = string("ejp mysljylc kd kxveddknmc re jsicpdrysi") + 
			     string("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd") +
			     string("de kr kd eoya kw aej tysr re ujdr lkgc jv") +
			     string("yeqz"); 
	assert(sz(in)==sz(out));
	for( int i = 0 ; i <sz(in) ; i++ ){
		F[out[i]] = in[i];
		invF[in[i]] = out[i];
	}
	assert(sz(F)==27);
	assert(sz(invF)==27);
	int T; scanf("%d\n",&T);
	for( int test = 1 ; test <= T ; test++ ) {
		string s;
		getline(cin,s);
		printf("Case #%d: ",test);		
		for( int i = 0 ; i < sz(s) ; i++ ) printf("%c",F[s[i]]);
		printf("\n");
	}
	return 0;
}
