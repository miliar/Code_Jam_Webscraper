#include <iostream>

using namespace std;

int main(){
	int cases;
	
	cin >> cases;
	
	for(int T=1;T<=cases;T++){
		
		int row;
		int col;

		cin >> row;
		cin >> col;

		int in[row][col];

		char scan;

		for(int i=0;i<row;i++){
			for(int j=0;j<col;j++){
				cin >> scan;
				// cout << scan;
				if(scan == '.'){
					in[i][j]=0;
				}
				else if(scan == '#'){
					in[i][j]=1;
				}
			}
			// cout << endl;
		}
		
		int ok = 1;
		for(int i=0;i<row;i++){
			for(int j=0;j<col;j++){
				if(in[i][j] == 1 && ok == 1){
					if(	in[i+1][j] == 1 &&
						in[i][j+1] == 1 &&
						in[i+1][j+1] == 1){
							in[i][j] = 2;
							in[i+1][j] = 3;
							in[i][j+1] = 4;
							in[i+1][j+1] = 5;
					}
					else{
						cout << "Case #" << T << ":" << endl << "Impossible" << endl;
						ok = 0;
						break;
					}
				}
				else if(ok==0){
					break;
				}
			}
		}
		
		if(ok == 1){
			cout << "Case #" << T << ":" << endl;
			for(int i=0;i<row;i++){
				for(int j=0;j<col;j++){
					if(in[i][j] == 0){
						cout << ".";
					}
					else if(in[i][j] == 2){
						cout << "/";
					}
					else if(in[i][j] == 3){
						cout << "\\";
					}
					else if(in[i][j] == 4){
						cout << "\\";
					}
					else if(in[i][j] == 5){
						cout << "/";
					}
				}
				cout << endl;
			}
			
		}
	}

	
}

// Input 
//  	
// Output 
//  
// 3
// 2 3
// ###
// ###
// 1 1
// .
// 4 5
// .##..
// .####
// .####
// .##..	 Case #1:
// Impossible
// Case #2:
// .
// Case #3:
// ./\..
// .\//\
// ./\\/
// .\/.. 
