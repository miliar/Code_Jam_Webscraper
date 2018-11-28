#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int R;
int mat[110][110];
int n;

void print(){
	for( int i= 1; i<= n; ++i ){
		for( int j= 1; j<= n; ++j )
		printf("%d", mat[i][j] );
		puts("");
	}
	puts("");
}

int update(){
	int flag= 0;
	for( int i= 1; i<= 100; ++i )
	for( int j= 1; j<= 100; ++j )
	if( mat[i-1][j]== 1 && mat[i][j-1]== 1 && mat[i][j]== 0 ) {
		mat[i][j]= 2; flag= 1; }
	
	for( int i= 1; i<= 100; ++i )
	for( int j= 1; j<= 100; ++j )
	if( mat[i-1][j]== 0 && mat[i][j-1]== 0 && mat[i][j]== 1 ){
		mat[i][j]= -1; flag= 1; }
		
	for( int i= 1; i<= 100; ++i )
	for( int j= 1; j<= 100; ++j )
	if( mat[i][j]== 2 ) mat[i][j]= 1;
	else if( mat[i][j]== -1 ) mat[i][j]= 0;
	
	return flag;
}

int main(){
	int test;
	freopen("A.in", "r", stdin );
	freopen("b.txt", "w", stdout );
	
	scanf("%d",&test );
	for( int te= 1; te<= test; ++te ){
		scanf("%d",&R );
		
		for( int i= 0; i<= 100; ++i )
		for( int j= 0; j<= 100; ++j ) mat[i][j]= 0;
		
		for( int i= 0; i< R; ++i ){
			int x1, x2, y1, y2;
			
			scanf("%d%d%d%d", &y1, &x1, &y2, &x2 );
			
			for( int x= x1; x<= x2; ++x )
			for( int y= y1; y<= y2; ++y )
			mat[x][y]= 1;
		}
		
		n= 6;
//		print();
		
		int ans= 0;
		while( update() ) {
			ans++;
			
	//		print(); system("pause");
		}
		
		printf("Case #%d: %d\n", te, ans );
	}
	
	return 0;
}
