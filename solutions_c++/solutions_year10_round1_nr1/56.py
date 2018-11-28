// by shik
#include <iostream>
using namespace std;
char tbl[100][100];
int n,m;
int c1( int x, int y ) {
	if ( y+m>n ) return 0;
	int a=0,b=0,i;
	for ( i=0; i<m; i++ )
		if ( tbl[x][y+i]=='R' ) a++;
		else if ( tbl[x][y+i]=='B' ) b++;
	if ( a==m ) return 1;
	if ( b==m ) return 2;
	return 0;
}
int c2( int x, int y ) {
	if ( x+m>n ) return 0;
	int a=0,b=0,i;
	for ( i=0; i<m; i++ )
		if ( tbl[x+i][y]=='R' ) a++;
		else if ( tbl[x+i][y]=='B' ) b++;
	if ( a==m ) return 1;
	if ( b==m ) return 2;
	return 0;
}
int c3( int x, int y ) {
	if ( x+m>n || y+m>n ) return 0;
	int a=0,b=0,i;
	for ( i=0; i<m; i++ )
		if ( tbl[x+i][y+i]=='R' ) a++;
		else if ( tbl[x+i][y+i]=='B' ) b++;
	if ( a==m ) return 1;
	if ( b==m ) return 2;
	return 0;
}
int c4( int x, int y ) {
	if ( x-m+1<0 || y+m>n ) return 0;
	int a=0,b=0,i;
	for ( i=0; i<m; i++ )
		if ( tbl[x-i][y+i]=='R' ) a++;
		else if ( tbl[x-i][y+i]=='B' ) b++;
	if ( a==m ) return 1;
	if ( b==m ) return 2;
	return 0;
}
int check() {
	int r=0,i,j;
	for ( i=0; i<n; i++ )
		for ( j=0; j<n; j++ )
			r|=c1(i,j)|c2(i,j)|c3(i,j)|c4(i,j);
	return r;
}
void rotate() {
	int i,j,k,x; char s[100]={};
	for ( i=0; i<n; i++ ) {
		for ( j=k=0; j<n; j++ )
			if ( tbl[i][j]!='.' ) s[k++]=tbl[i][j];
		for ( j=0; j<n-k; j++ ) tbl[i][j]='.';
		for ( j=n-k,x=0; j<n; j++ ) tbl[i][j]=s[x++];
	}
	//for ( i=0; i<n; i++ ) puts(tbl[i]);
}
int main()
{
	int t,T,i,f;
	scanf("%d",&T);
	for ( t=1; t<=T; t++ ) {
		scanf("%d%d",&n,&m);
		while(getchar()!='\n');
		for ( i=0; i<n; i++ ) gets(tbl[i]);
		rotate();
		f=check();
		if ( f==0 ) printf("Case #%d: Neither\n",t);
		else if ( f==1 ) printf("Case #%d: Red\n",t);
		else if ( f==2 ) printf("Case #%d: Blue\n",t);
		else if ( f==3 ) printf("Case #%d: Both\n",t);
	}
	return 0;
}
