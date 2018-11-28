#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#define L 1010
#define N 130
#define FOR(it,c) for ( __typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )
using namespace std;
const char from[9]="oieastbg",to[9]="01345789";
int tbl[130];
char str[L];
int len;
void input() {
	scanf("%*d %s",str);
	len=strlen(str);
}
int in[N],out[N],e[N][N],m;
void add( int a, int b ) {
	if ( e[a][b] ) return;
	e[a][b]=1;
	in[b]++;
	out[a]++;
	m++;
}
void build() {
	m=0;
	memset(e,0,sizeof(e));
	memset(in,0,sizeof(in));
	memset(out,0,sizeof(out));
	for ( int i=1; i<len; i++ ) {
		int a=str[i-1],b=str[i];
		add(a,b);
		if ( tbl[a] ) add(tbl[a],b);
		if ( tbl[b] ) add(a,tbl[b]);
		if ( tbl[a] && tbl[b] ) add(tbl[a],tbl[b]);
	}
}
int calc() {
	int ret=0;
	for ( int i=0; i<N; i++ )
		if ( in[i]>out[i] ) ret+=in[i]-out[i];
	return ret;
}
char s1[L],s2[L];
int ee[N][N],n1,n2;
void dfs1( int p ) {
	for ( int i=0; i<N; i++ )
		while ( ee[p][i] ) {
			ee[p][i]--;
			dfs1(i);
		}
	s1[n1++]=p;
}
void dfs2( int p ) {
	for ( int i=N-1; i>=0; i-- )
		while ( ee[p][i] ) {
			ee[p][i]--;
			dfs2(i);
		}
	s2[n2++]=p;
}
void predo() {
	for ( int i=0; i<N; i++ )
		for ( int j=0; j<N; j++ )
			ee[i][j]=e[i][j];
}
bool spcas() {
	int ci=0,co=0,st=0,ed=0;
	for ( int i=0; i<N; i++ )
		if ( in[i]>out[i] ) ci++,ed=i;
		else if ( out[i]>in[i] ) co++,st=i;
	if ( ci>1 || co>1 ) return 0;
	ee[st][ed]+=out[st]-in[st]-1;
	predo(); n1=0; dfs1(st); s1[n1]=0;
	predo(); n2=0; dfs2(st); s2[n2]=0;
	reverse(s1,s1+n1); reverse(s2,s2+n2);
	if ( strcmp(s1,str) || strcmp(s2,str) ) return 0;
	return 1;
}
void solve() {
	if ( len<=2 ) {
		puts("No Results");
		return;
	}
	int diff=calc();
	if ( diff==0 ) {
		printf("%d\n",m+1);
		return;
	}
	if ( m+diff==len ) {
		if ( spcas() ) printf("%d\n",len+1);
		else printf("%d\n",len);
		return;
	}
	printf("%d\n",m+diff);
}
int main()
{
	for ( int i=0; i<8; i++ ) tbl[(int)from[i]]=to[i];
	int t,cs=0;
	scanf("%d",&t);
	while ( t-- ) {
		printf("Case #%d: ",++cs);
		input();
		build();
		solve();
	}
	return 0;
}
