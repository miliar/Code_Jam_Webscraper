// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
#define N 6010
#define SZ(x) ((int)(x).size())
#define FOR(it,c) for ( __typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )
using namespace std;
struct Q {
	int dat[2*N*N],fr,bk;
	void clear() { fr=bk=0; }
	void push( int x ) { dat[bk++]=x; }
	int pop() { return dat[fr++]; }
	bool empty() { return fr==bk; }
} q;
const char tmt[3][10]={"bridge","fork","ring"};
const int dx[]={-1,-1,0,0,1,1},dy[]={-1,0,-1,1,0,1};
inline int bit( int x, int i ) { return (x>>i)&1; }
int n,m,l;
char v[N][N];
inline bool out( int x, int y ) { return x<1 || x>l || y<1 || y>l || x-y>=n || y-x>=n; }
inline bool is_cor( int x, int y ) {
	if ( x==1 && y==1 ) return 1;
	if ( x==1 && y==n ) return 1;
	if ( x==n && y==1 ) return 1;
	if ( x==l && y==n ) return 1;
	if ( x==n && y==l ) return 1;
	if ( x==l && y==l ) return 1;
	return 0;
}
inline int is_edg( int x, int y ) {
	if ( x==1 ) return 1;
	if ( y==1 ) return 2;
	if ( x==l ) return 4;
	if ( y==l ) return 8;
	if ( x-y==n-1 ) return 16;
	if ( y-x==n-1 ) return 32;
	return 0;
}
int BFS( int x, int y ) {
	int cor=0,edg=0,ret=0;
	q.clear(); q.push(x); q.push(y); v[x][y]=2;
	while ( !q.empty() ) {
		x=q.pop(); y=q.pop();
		if ( is_cor(x,y) ) cor++;
		else edg|=is_edg(x,y);
		for ( int i=0; i<6; i++ ) {
			int nx=x+dx[i],ny=y+dy[i];
			if ( out(nx,ny) || v[nx][ny]!=1 ) continue;
			q.push(nx); q.push(ny); v[nx][ny]=2;
		}
	}
	if ( __builtin_popcount(edg)>=3 ) ret|=2;
	if ( cor>=2 ) ret|=1;
	return ret;
}
void BFS2( int x, int y ) {
	q.clear(); q.push(x); q.push(y); v[x][y]=3;
	while ( !q.empty() ) {
		x=q.pop(); y=q.pop();
		for ( int i=0; i<6; i++ ) {
			int nx=x+dx[i],ny=y+dy[i];
			if ( out(nx,ny) || v[nx][ny]!=0 ) continue;
			q.push(nx); q.push(ny); v[nx][ny]=3;
		}
	}
}
int x[10010],y[10010];
int chk( int M ) {
	int ret=0;
	memset(v,0,sizeof(v));
	for ( int i=0; i<=M; i++ ) v[x[i]][y[i]]=1;
	for ( int i=0; i<=M; i++ ) if ( v[x[i]][y[i]]==1 ) ret|=BFS(x[i],y[i]);
	for ( int i=1; i<=l; i++ ) for ( int j=1; j<=l; j++ ) if ( !out(i,j) && is_edg(i,j) && v[i][j]==0 ) BFS2(i,j);
	for ( int i=1; i<=l&&!bit(ret,2); i++ ) for ( int j=1; j<=l; j++ ) if ( !out(i,j) && v[i][j]==0 ) ret|=4;
	for ( int i=M; i>=0; i-- ) {
		v[x[i]][y[i]]=3;
		int flg=1;
		for ( int j=0; j<6&&flg; j++ ) {
			int nx=x[i]+dx[j],ny=y[i]+dy[j];
			if ( out(nx,ny) || v[nx][ny]!=2 ) flg=0;
		}
		if ( flg ) ret|=4;
	}
	return ret;
}
int main()
{
	int t,cs=0;
	scanf("%d",&t);
	while ( t-- ) {
		scanf("%d%d",&n,&m); l=2*n-1;
		for ( int i=0; i<m; i++ ) scanf("%d%d",x+i,y+i);
		int L=0,R=m;
		while ( L!=R ) {
			int M=(L+R)/2;
			if ( chk(M) ) R=M;
			else L=M+1;
		}
		printf("Case #%d:",++cs);
		if ( L==m ) puts(" none");
		else {
			int ans=chk(L),flg=0;
			for ( int i=0; i<3; i++ ) if ( bit(ans,i) ) {
				printf("%c%s",flg?'-':' ',tmt[i]);
				flg=1;
			}
			printf(" in move %d\n",L+1);
		}
	}
	return 0;
}
