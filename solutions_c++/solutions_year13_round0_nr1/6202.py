#include <iostream>
#include <string>
#include <vector>
#include <cstdio>

using namespace std;

int check( int myA[4][4] ){
	if( ( myA[0][0] + myA[0][1] + myA[0][2] + myA[0][3] ) == 4 ){ return 1;	}
	if( ( myA[1][0] + myA[1][1] + myA[1][2] + myA[1][3] ) == 4 ){ return 1;	}
	if( ( myA[2][0] + myA[2][1] + myA[2][2] + myA[2][3] ) == 4 ){ return 1;	}
	if( ( myA[3][0] + myA[3][1] + myA[3][2] + myA[3][3] ) == 4 ){ return 1;	}

	if( ( myA[0][0] + myA[1][0] + myA[2][0] + myA[3][0] ) == 4 ){ return 1;	}
	if( ( myA[0][1] + myA[1][1] + myA[2][1] + myA[3][1] ) == 4 ){ return 1;	}
	if( ( myA[0][2] + myA[1][2] + myA[2][2] + myA[3][2] ) == 4 ){ return 1;	}
	if( ( myA[0][3] + myA[1][3] + myA[2][3] + myA[3][3] ) == 4 ){ return 1;	}

	if( ( myA[0][0] + myA[1][1] + myA[2][2] + myA[3][3] ) == 4 ){ return 1;	}
	if( ( myA[3][0] + myA[2][1] + myA[1][2] + myA[0][3] ) == 4 ){ return 1;	}

	return 0;
}

int main(){
	int T; cin >> T;
	int myX[4][4];
	int myO[4][4];
	int used;

	for( int t=1; t<=T; t++ ){
		used = 0;

		for( int i=0; i<4; i++ ){
			for( int j=0; j<4; j++ ){
				char myChar; cin >> myChar;

				switch( myChar ){
					case 'X':
						myX[i][j] = 1;
						myO[i][j] = 0;
						++used;
						break;
					case 'O':
						myX[i][j] = 0;
						myO[i][j] = 1;
						++used;
						break;
					case 'T':
						myX[i][j] = 1;
						myO[i][j] = 1;
						++used;
						break;
					case '.':
						myX[i][j] = 0;
						myO[i][j] = 0;
						break;
				}
			}
		}

		int myXcheck = check( myX );
		int myOcheck = check( myO );

		if( ( myXcheck == 1 && myOcheck == 1 ) || ( myXcheck == 0 && myOcheck == 0 && used == 16 ) ){
			cout << "Case #" << t << ": Draw" << endl;
		} else if( myXcheck == 1 ){
			cout << "Case #" << t << ": X won" << endl;
		} else if( myOcheck == 1 ){
			cout << "Case #" << t << ": O won" << endl;
		} else {
			cout << "Case #" << t << ": Game has not completed" << endl;
		}
	}
}