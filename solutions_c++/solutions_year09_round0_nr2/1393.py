#include<iostream>
#include<cstdio>
using namespace std;
int H , W ; 
int mas[ 102][102] ; 
char map[102][102] ;
int X[] = {  -1 , 0 , 0, 1 };
int Y[] = {  0 , -1 ,  1 ,0 } ;
int staK[10200][2] , sSize =0 ; 
bool shig( int x, int y ){
	return x >= 0 && x < H && y >=0 && y < W ; 
}

int main(){
	freopen("B-large.in","r", stdin);
	freopen("B-large.out","w", stdout);
	int T , j, i ; 
	cin >> T ;
	for ( int t= 1; t <= T ; t++){
		cin >> H >> W ; 
		for ( i=0;i < H ; i++){
			for( j=0;j < W; j++){
				cin >> mas[i][j] ; 
				map[i][j] = '0' ;
		    }
		}
		char ind = 'a' ;
		for( i=0;i < H; i++){
			for( j=0; j< W; j++){
				if ( map[i][j] != '0' ) continue ; 
				char C = '0' ;
				sSize = 1;   staK[0][0] = i ; staK[0][1] = j;
				bool gadasvla = true; 
				while( gadasvla ){
					int qX = staK[sSize-1][0] , qY = staK[sSize-1][1] ;
					gadasvla = false; 
					int tmin = mas[ qX][qY] , tind = -1 ; 
					for( int k= 0;k  < 4; k++){
						if( !shig( X[k] + qX , Y[k] + qY  ) ) continue;
						if ( mas[ X[k] + qX ][ Y[k] + qY ] < tmin       ){
							if (  map[ X[k] + qX ][ Y[k] + qY ] != '0'  ){ C = map[ X[k] + qX ][ Y[k] + qY ];   tind=k; tmin= mas[ X[k] + qX ][ Y[k] + qY ]; gadasvla = false;  }
							else {    gadasvla = true;            
							          C = '0' ;
									  tind=k; tmin= mas[ X[k] + qX ][ Y[k] + qY ];
							}
						}
					}
					if( C != '0' ) break ;
					if(!gadasvla ) break;
					staK[ sSize  ][0] = qX + X[tind]; staK[sSize++][1] = qY + Y[tind] ; 
				}
				if( C == '0') { C = ind; ind++; }
				for( int k= sSize-1; k >=0 ; k-- )
					map[ staK[k][0] ][ staK[k][1] ] = C ; 
			}
		}
		cout  << "Case #" << t << ":\n" ;
		for(i=0;i < H;i++){
			for(j=0;j < W;j++){
				cout << map[i][j];
				if( j < W-1) cout <<  " " ;
			}
			cout << "\n" ;
		}


	}

	return 0;
}