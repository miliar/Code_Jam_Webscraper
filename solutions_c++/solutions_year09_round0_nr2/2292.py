#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main()
{
	map<int,int> MAP;

	int T, H, W;

	cin >> T;

	for (int i = 1; i <= T; i++ ) {
		cout << "Case #" << i << ":\n";
		cin >> H >> W;

		int M[H][W];
		int CC[H][W];
		

		for (int j = 0; j < H; j++ ) {
			for (int k = 0; k < W; k++ ) {
				cin >> M[j][k];
			}
		}
		int l = 0; 
		for (int j = 0; j < H; j++ ) {
			for (int k = 0; k < W; k++ ) {
				 CC[j][k] ='a' + l++;
				 //cout << CC[j][k] << " ";
			}
		//	cout << "\n";
		}

		//cout << "\n\n";
		int ch1, ch2;
		
		int minposj, minposk;
		int min;
		vector <int> Arr(H*W);

		for (int j = 0; j < H; j++ ) {
			for (int k= 0; k < W; k++ ) {
				minposj = j; minposk = k;
				min = M[j][k];
				if ( j > 0 && M[j-1][k] < min ) {
					min = M[j-1][k];
					minposj = j-1; minposk = k;
				}  
				if ( k > 0 && M[j][k-1] < min ) {
					min = M[j][k-1];
					minposj = j; minposk = k-1;
				}
				if ( k < W - 1 && M[j][k+1] < min) {
					min = M[j][k+1];
					minposj = j; minposk = k+1;
				}	
				if ( j < H - 1 && M[j+1][k] < min) {
					min = M[j+1][k];
					minposj = j+1; minposk = k;
				}
				
				if ( CC[minposj][minposk] > CC[j][k]) {
					ch1 = CC[minposj][minposk];
					ch2 = CC[j][k];
					int iii, jjj;
					for (iii = 0; iii <= j; iii++ ) {
						for ( jjj = 0; jjj < W; jjj++ ) {
							if( CC[iii][jjj] == ch1 ) {
								CC[iii][jjj] = ch2;
							}
						}
					}
					//for (int ii = 0; ii < j; ii++ ) {
						for ( jjj = 0; jjj <= k; jjj++ ) {
							if( CC[iii][jjj] == ch1 ) {
								CC[iii][jjj] = ch2;
							}
						}
					//}
										
					//CC[minposj][minposk] = CC[j][k];
				} else if (CC[j][k] > CC[minposj][minposk]) {
					ch2 = CC[minposj][minposk];
					ch1 = CC[j][k];
					int iii,jjj;
					for ( iii = 0; iii <= j; iii++ ) {
						for (int jjj = 0; jjj < W; jjj++ ) {
							if( CC[iii][jjj] == ch1 ) {
								CC[iii][jjj] = ch2;
							}
						}
					}
					for (jjj = 0; jjj <= k; jjj++ ) {
						if( CC[iii][jjj] == ch1 ) {
							CC[iii][jjj] = ch2;
						}
					}
					
					//CC[j][k] = CC[minposj][minposk];
				}		
			
			
			}
		}
		
		MAP.clear();

		l = 1;
		/*for (int j = 0; j < H*W; j++ ) {
			//for (int k = 0; k < W; k++ ) {
				MAP['a' + j] = 0;
		}*/

		for (int j = 0; j < H; j++ ) {
			for (int k= 0; k < W; k++ ) {
				if ( MAP[CC[j][k]] == 0) {
					//cout << "Hee";
					MAP[CC[j][k]] = l++;
				}
				cout << (char) ('a' - 1 + MAP[CC[j][k]]) << " ";
			}

			cout << endl;
		}
		/*
		for (int j = 0; j < H; j++ ) {
			for (int k= 0; k < W; k++ ) {
				//if ( MAP[CC[j][k]] == 0) {
				//	MAP[CC[j][k]] == l++;
				//}
				cout << (char) ('a' - 1 + MAP[CC[j][k]]) << " ";
			}

			cout << endl;
		}*/

		//cout << "\n****************\n\n";

				









	
	}

	return 0;
}
