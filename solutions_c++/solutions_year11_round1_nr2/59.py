// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#define N 10010
#define M 110
#define S 12
#define SZ(x) ((int)(x).size())
#define MP make_pair
using namespace std;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef VI::iterator VIT;
typedef vector<PII> VII;
int n,m;
char dic[N][S];
char lst[M][30];
VI has[N][26];
void input() {
	scanf("%d%d",&n,&m);
	for ( int i=0; i<n; i++ ) scanf("%s",dic[i]);
	for ( int i=0; i<m; i++ ) scanf("%s",lst[i]);
	for ( int i=0; i<n; i++ ) {
		for ( int j=0; j<26; j++ ) has[i][j].clear();
		for ( int j=0; dic[i][j]; j++ ) has[i][dic[i][j]-'a'].push_back(j);
	}
}
VII v[N];
void build( char *s ) {
	for ( int i=0; i<n; i++ ) v[i].clear();
	for ( int i=0; i<n; i++ ) {
		v[i].push_back(MP(strlen(dic[i]),-1));
		for ( int j=0; s[j]; j++ ) {
			VI &now=has[i][s[j]-'a'];
			for ( VIT it=now.begin(); it!=now.end(); it++ ) v[i].push_back(MP(j,*it));
		}
	}
	sort(v,v+n);
	/*
	for ( int i=0; i<n; i++ ) {
		printf("%d:",i);
		for ( int j=0; j<SZ(v[i]); j++ ) printf(" (%d,%d)",v[i][j].first,v[i][j].second);
		puts("");
	}
	*/
}
bool chk( VII &now ) {
	if ( now>v[n-1] ) return 0;
	VII s=*lower_bound(v,v+n,now);
	for ( int i=0; i<SZ(now); i++ ) {
		//if ( s[i]!=now[i] ) printf("(%d,%d) vs (%d,%d)\n",now[i].first,now[i].second,s[i].first,s[i].second);
		if ( i<SZ(now)-1 && s[i]!=now[i] ) return 0;
		if ( s[i].first != now[i].first ) return 0;
	}
	return 1;
}
int solve( int id, char *s, char *t ) {
	int cnt=0,i;
	VII now; now.push_back(MP(strlen(t),-1));
	for ( i=0; s[i]; i++ ) {
		//printf("== i=%d\n",i);
		int p=s[i]-'a';
		if ( !has[id][p].empty() ) {
			for ( VIT it=has[id][p].begin(); it!=has[id][p].end(); it++ ) now.push_back(MP(i,*it));
			//printf("now=");
			//for ( int j=0; j<SZ(now); j++ ) printf(" (%d,%d)",now[j].first,now[j].second);
			//puts("");
		} else {
			now.push_back(MP(i,-1));
			if ( chk(now) ) cnt++;
			now.pop_back();
		}
	}
	return cnt;
}
int solve( char *s ) {
	int ret=-1,big=-1,i;
	build(s);
	for ( i=0; i<n; i++ ) {
		//printf("i=%d\n",i);
		int now=solve(i,s,dic[i]);
		//printf("%d: %d\n",i,now);
		if ( now>big ) {
			big=now;
			ret=i;
		}
	}
	return ret;
}
void solve() {
	static int cas=0;
	printf("Case #%d: ",++cas);
	for ( int i=0; i<m; i++ ) printf("%s%c",dic[solve(lst[i])],i==m-1?'\n':' ');
}
int main()
{
	int t;
	scanf("%d",&t);
	while ( t-- ) {
		input();
		solve();
	}
	return 0;
}
