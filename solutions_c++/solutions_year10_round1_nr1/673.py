#include <cstdio>
#include <iostream>
#include <string>

#define MAXN 55

using namespace std;

string board[ MAXN ];
int N, K, T;
int mov[][2] = { {-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1} };

int count(int i, int j, char cosa, int k){
	//printf("(%d,%d) ", i, j);
	if ( i<0 || i>=N || j<0 || j>=N ) return 0;
	if ( board[i][j] != cosa ) return 0;
	return 1 + count( i+mov[k][0], j+mov[k][1], cosa, k );
}

int main(){
	
	cin >> T;
	
	for (int tt=1; tt<=T; tt++){
		cin >> N >> K;
		cin.ignore();
		
		for (int i=0; i<N; i++){
			getline( cin, board[i] );
			//cout << board[i] << endl;
		}
		
		for (int i=0; i<N; i++){
			int j = N - 1;
			
			for (int k=N-1; k>=0; k--)
				if ( board[i][k]=='R' || board[i][k]=='B' ){
					board[i][j--] = board[i][k];
					if ( j+1 == k ){
						continue;
					}
					board[i][k] = '.';
				}
		}
		
		//for (int i=0; i<N; i++)
			//cout << board[i] << endl;
		
		//cout << "***********" << endl;
		//continue;
		
		bool RWin = false;
		bool BWin = false;
		
		for (int i=0; i<N; i++)
			for (int j=0; j<N; j++)
				if ( board[i][j] != '.' )
					for (int k=0; k<8; k++){
						//cout << i << " " << j << " " << k;
						int cosa;
						if ( board[i][j] == 'R' )
							RWin = RWin || ((cosa=count( i, j, board[i][j], k )) >= K);
						else
							BWin = BWin || ((cosa=count( i, j, board[i][j], k )) >= K);
						//cout << " " << cosa << " "<< board[i][j] << endl;
					}
		
		printf("Case #%d: ", tt);
		
		//cout << RWin << " " << BWin << endl;
		
		if ( RWin && BWin ) puts( "Both" );
		else if ( !(RWin || BWin) ) puts( "Neither" );
		else if ( RWin ) puts( "Red" );
		else puts("Blue");
	}
	

	return 0;
}
