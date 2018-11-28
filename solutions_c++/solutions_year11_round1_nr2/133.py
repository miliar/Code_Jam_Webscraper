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

const int maxn = 10000+123;
char dict[maxn][15];
int word[maxn][30];
int p[maxn];
char str[30];

int mycmp(int a,int b){
	if(word[a][0]!=word[b][0]) return word[a][0] < word[b][0];
	forn(i,26){
		if(word[a][str[i]-'a'+1]!=word[b][str[i]-'a'+1])
			return word[a][str[i]-'a'+1]<word[b][str[i]-'a'+1];
	}
	return a<b;
}

int n,m;

pair<int,int> rec(int lvl,int l,int r){
	//eprintf("%d %d %d\n",lvl,l,r);
	if(l+1==r) return mp(0,-p[l]);
	pair<int,int> res = mp(-1,-1);
	pair<int,int> tmp;
	if(lvl==-1){
		for(int i = l ; i < r ; i++ ){
			int j=i;
			while(j<r&&word[p[i]][0]==word[p[j]][0]) j++;
			tmp = rec(0,i,j);
			res = max(res,tmp);
			i = j-1;
		}
		return res;
	}
	for(int i = l ; i < r ; i++ ){
		int j = i;
		while(j<r&&word[p[i]][str[lvl]-'a'+1]==word[p[j]][str[lvl]-'a'+1]) j++;
		tmp = rec(lvl+1,i,j);
		if(j!=r&&word[p[i]][str[lvl]-'a'+1]==0){
			tmp.first++;
		}
		res = max(tmp,res);
		i = j-1;
	}
	return res;
}

int main(){
	int T ;
	scanf("%d",&T);
	for(int test = 1 ; test <= T ; test++ ){
		int n,m;
		scanf("%d",&n);
		scanf("%d",&m);
		forn(i,n) scanf("%s",dict[i]),p[i]=i;
		memset(word,0,sizeof word);
		forn(i,n){
			int l = strlen(dict[i]);
			word[i][0]=l;
			forn(j,l){
				word[i][dict[i][j]-'a'+1]+=1<<j;
			}
		}
		printf("Case #%d:",test);
		forn(t,m){
			scanf("%s",str);
			sort(p,p+n,mycmp);
			//forn(i,n) printf("%d%c",p[i]," \n"[i+1==n]);
			pair<int,int> res = rec(-1,0,n);
			//eprintf("%d %d\n",res.first,res.second);
			printf(" %s",dict[-res.second]);
		}
		printf("\n");
		eprintf("test %d ok.\n",test);
	}
	return 0;
}
