#include<iostream>
 
using namespace std;
 
int main(){
	int n;
	bool flag;
	char arr[4][4];
	cin >> n;
	
	for(int q = 0; q < n; q++){
		
		// initializing and input
		cout << "Case #" << q + 1 << ": ";
		flag = false;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> arr[i][j];
			}
		}
		
		// horizantal and vertical
		for(int i = 0; i < 4; i++){
			if(arr[i][0] != '.' && (arr[i][0] == arr[i][1] || arr[i][1] == 'T') && (arr[i][1] == arr[i][2] || arr[i][2] == 'T') && (arr[i][2] == arr[i][3] || arr[i][3] == 'T')){
				cout << arr[i][0] << " won" << endl;
				flag = true;
			}
			else if(arr[0][i] != '.' && (arr[0][i] == arr[1][i] || arr[1][i] == 'T') && (arr[1][i] == arr[2][i] || arr[2][i] == 'T') && (arr[2][i] == arr[3][i] || arr[3][i] == 'T')){
				cout << arr[0][i] << " won" << endl;
				flag = true;
			}
		}
		
		// diagnoal
		if(!flag){
			if(arr[0][0] != '.' && (arr[0][0] == arr[1][1] || arr[1][1] == 'T') && (arr[1][1] == arr[2][2] || arr[2][3] == 'T') && (arr[2][2] == arr[3][3]  || arr[3][3] == 'T')){
				cout << arr[0][0] << " won" << endl;
				flag = true;
			}
			else if(arr[0][3] != '.' && (arr[0][3] == arr[1][2]  || arr[1][2] == 'T') && (arr[1][2] == arr[2][1] || arr[2][1] == 'T') && (arr[2][1] == arr[3][0] || arr[3][0] == 'T')){
				cout << arr[0][3] << " won" << endl;
				flag = true;
			}
		}
		
		// no one's won, check for a draw
		if(!flag){
			bool full = true;;
			for(int i = 0; i < 4; i++){
				for(int j = 0; j < 4; j++){
					if(arr[i][j] == '.'){
						full = false;
					}
				}
			}
			if(full){
				cout << "Draw" << endl;	
				flag = true;
			}
		}
		
		// Game not completed
		if(!flag){
			cout << "Game has not completed" << endl;
		}
			
	}
	return 0;
 
}
