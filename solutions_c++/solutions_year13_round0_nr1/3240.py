//By Lin
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<cctype>
#include<cmath>

#define eps 1e-9
#define N 100010
#define sqr(x) ((x)*(x))
#define Rep(i,n) for(int i = 0; i<n; i++)
#define foreach(i,n) for( __typeof(n.begin()) i = n.begin(); i!=n.end(); i++)
#define X first
#define Y second
#define mp(x,y) make_pair(x,y)

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

char	s[10][10];
bool	pan( char ch){
	Rep(i,4){
		bool f1 = 1, f2 = 1;
		Rep(j,4){
			if ( s[i][j] != ch && s[i][j] != 'T' ) f1 = false;
			if ( s[j][i] != ch && s[j][i] != 'T' ) f2 = false;
		}
		if ( f1 || f2 ) return true;
	}
	
	bool f1 = 1, f2 = 1;
	Rep(i,4){
		if ( s[i][i] != ch && s[i][i] != 'T' ) f1 = false;
		if ( s[i][3-i] != ch && s[i][3-i] != 'T' ) f2 = false;
	}
	if ( f1 || f2 ) return true;
	return false;
}
bool	exist( char ch){
	Rep(i,4){
		Rep(j,4){
			if ( s[i][j] == ch ) return true;
		}
	}
	return false;
}
int		main(){
	int cas , tt = 0;
	scanf("%d", &cas );
	while ( cas -- ) {
		Rep(i,4) scanf("%s", s[i] );
		printf("Case #%d: ", ++tt );
		if ( pan('X') ) printf("X won\n");
		else if ( pan('O') ) printf("O won\n");
		else if ( exist('.') ) printf("Game has not completed\n");
		else printf("Draw\n");
	}
	return 0;
}
