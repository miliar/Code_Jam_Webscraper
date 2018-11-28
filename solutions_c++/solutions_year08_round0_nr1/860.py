#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

const int maxq=1000, maxs=100, INFI =0x3fffffff;

map<string, int> mmap;
int que[maxq+10], f[maxq+5][maxs+5];
int num, s, q;

void read(){
	int  i;
	char str[110];
	mmap.clear();
	memset( que, 0, sizeof(que));
	scanf("%d", &s);
	getchar();
	for( i=1; i<=s; i++){
		gets(str);
		mmap.insert( make_pair(str, i) );
	}
	scanf("%d", &q);
	getchar();
	for( i=1; i<=q; i++){
		gets(str);
		que[i]=mmap.find(str)->second;
	}
}

void solve(){
	if( q==0 ) {
		printf("0\n"); return;
	}
	int i, j, k, tmini;
	memset( f, 0, sizeof(f) );
	for( i=1; i<=s; i++){
		if( que[1]==i ) f[1][i]=INFI;
		else f[1][i]=1;
	}
	for( i=2; i<=q; i++){
		tmini = *min_element( &f[i-1][1], &f[i-1][s+1] );
		for( j=1; j<=s; j++){
			if( que[i]==j ) { f[i][j]=INFI; continue; }
			if( f[i-1][j]==INFI ) f[i][j]=tmini+1;
			else f[i][j]=f[i-1][j];
		}
	}
	printf("%d\n", *min_element( &f[q][1], &f[q][s+1])-1 );
}

int main(){
	freopen("D:\\in.txt", "r", stdin);
	freopen("D:\\a.out", "w", stdout);
	int tc, i;
	scanf("%d", &tc);
	for( i=1; i<=tc; i++){
		printf("Case #%d: ", i);
		read();
		solve();
	}
	return 0;
}