#include <cstdio>
#include <iostream>

using namespace std;


int T;
int g[100][100];
char res[100][100];
int H,W;
char newTag;

int d[4][2] = { { -1 , 0 } , { 0 , -1 } , { 0 , 1 } , { 1 , 0 } };


bool inArea( int x , int y ){ return x >= 0 && x < H && y >= 0 && y < W; }

char dfs( int x , int y ){

	if( res[x][y] != ' ' )
		return res[x][y];

	int smallestV = 20000;
	int smallestD = -1;

	int nextx,nexty;
	for( int i = 0 ; i < 4 ; i ++ ){
		nextx = x + d[i][0];
		nexty = y + d[i][1];
		if( inArea( nextx , nexty ) && g[nextx][nexty] < g[x][y] && g[nextx][nexty] < smallestV ){
			smallestV = g[nextx][nexty];
			smallestD = i;
		}
	}

	if( smallestD == -1 ){
		res[x][y] = newTag;
		newTag += 1;
	}
	else
		res[x][y] = dfs( x + d[smallestD][0] , y + d[smallestD][1] );
		
	return res[x][y];
}

void solve( void ){

	for( int i = 0 ; i < H ; i ++ )
		for( int j = 0 ; j < W ; j ++ )
			if( res[i][j] == ' ' )
				dfs( i , j );

	return;
}

void init( void ){

	for( int i = 0 ; i < H ; i ++ )
		for( int j = 0 ; j < W ; j ++ )
			res[i][j] = ' ';

	newTag = 'a';

	return;
}

int main( void ){

	//FILE *fin = freopen( "B-test.in" , "r" , stdin );
	//FILE *fout = freopen( "B-testout.out" , "w" , stdout );

	//FILE *fin = freopen( "B-small-attempt0.in" , "r" , stdin );
	//FILE *fout = freopen( "B-smallout.out" , "w" , stdout );

	FILE *fin = freopen( "B-large.in" , "r" , stdin );
	FILE *fout = freopen( "B-largeout.out" , "w" , stdout );

	cin>>T;

	for( int cases = 1 ; cases <= T ; cases ++ ){

		cin>>H>>W;
		for( int i = 0 ; i < H ; i ++ )
			for( int j = 0 ; j < W ; j ++ )
				cin >> g[i][j];

		init();
		solve();

		cout<<"Case #"<<cases<<": "<<endl;
		for( int i = 0 ; i < H ; i ++ ){
			for( int j = 0 ; j < W ; j ++ )
				cout<<res[i][j]<<" ";
			cout<<endl;
		}
	}

	return 0;
}