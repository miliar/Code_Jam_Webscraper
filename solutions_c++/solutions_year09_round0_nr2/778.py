#include <iostream> 
using namespace std;
#define MAX 0x7ffffff
int m, n;
char map[110][110], cur;
int ati[110][110], dir[4][2]= {-1,0,0,-1,0,1,1,0};
bool flg[110][110];
int Flowto( int i, int j ){
	int min= MAX, k, a, b, t;
	if( ati[i][j]==MAX )	return -1;
	for( k= 0; k< 4; k++ ){
		a= i+ dir[k][0], b= j+ dir[k][1];
		if( ati[a][b]< min )
			min= ati[a][b], t= k;
	}
	if( min>= ati[i][j] )	return -1;
	return t;
}
void DFS( int i, int j ){
	if( !flg[i][j] )	return;
	map[i][j]= cur;
	int t= Flowto(i,j), k, a, b;
	flg[i][j]= false;
	if( t>= 0 )	DFS(i+dir[t][0],j+dir[t][1]);		//flow to
	for( k= 0; k< 4; k++ ){
		a= i+dir[k][0], b= j+dir[k][1];
		t= Flowto(a,b);
		if( t>= 0 && a+dir[t][0]==i && b+dir[t][1]==j )
			DFS(a,b);	//flow from
	}
}
int main(){
	int i, j, t, k;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	for( i= 0; i< 110; i++ )
		ati[i][0]= ati[0][i]= MAX;
	for( k= 1; k<= t; k++ ){
		scanf("%d%d",&m,&n);
		cur= 'a';
		for( i= 1; i<= m; i++ )
			for( j= 1; j<= n; j++ ){
				scanf("%d",&ati[i][j]);
				flg[i][j]= true;
			}
		for( i= 1; i<= n; i++ )	ati[m+1][i]= MAX;
		for( i= 1; i<= m+1; i++ )	ati[i][n+1]= MAX;
		for( i= 1; i<= m; i++ )
			for( j= 1; j<= n; j++ )
				if( flg[i][j] ){
					DFS(i,j);
					cur++;
				}
		printf("Case #%d:\n",k);
		for( i= 1; i<= m; i++ ){
			for( j= 1; j< n; j++ )
				printf("%c ",map[i][j]);
			printf("%c\n",map[i][j]);
		}
	}
	return 0;
}