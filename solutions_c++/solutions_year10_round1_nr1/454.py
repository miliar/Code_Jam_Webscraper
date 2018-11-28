#include <algorithm>
#include <iostream>

using namespace std;

char input[50][50];
char rotated[50][50];

int main(){
	int T;
	cin >> T;
	for(int tell = 1; tell <= T; tell++){
		int N, K;
		cin >> N >> K;
		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				cin >> input[i][j];
				rotated[i][j] = '.';
			}
		}

		// Rotate
		for(int row = 0; row < N; row++){
			int curr = 0;
			int trow = N-1-row;
			for(int col = N-1; col >= 0; col--){
				if(input[trow][col] != '.'){
					rotated[N-curr-1][row] = input[trow][col];
					curr++;
				}
			}
		}

		bool red = false;
		bool blue = false;
		// Check for horisontal K in row
		for(int row = 0; row < N; row++){
			for(int col = 0; col <= N-K; col++){
				char first = rotated[row][col];
				int count = 1;
				for(int k = col+1; k < col+K; k++){
					if(rotated[row][k] == first){
				       		count++;
				 	}
					else{
						break;
					}
				}
				if(count >= K){
					if(first == 'B')blue=true;
					else if(first=='R')red=true;
				}
			}

		}
		
		// Check for vertical K in row
		for(int row = 0; row <= N-K; row++){
			for(int col = 0; col < N; col++){
				char first = rotated[row][col];
				int count = 1;
				for(int k = row+1; k < row+K; k++){
					if(rotated[k][col] == first){
				       		count++;
				 	}
					else{
						break;
					}
				}
				if(count >= K){
					if(first == 'B')blue=true;
					else if(first=='R')red=true;
				}
			}

		}

		// Check for diagonal K in row
		for(int row = 0; row <= N-K; row++){
			for(int col = 0; col <= N-K; col++){
				char first = rotated[row][col];
				int count = 1;
				for(int k = 1; k < K; k++){
					if(rotated[row+k][col+k] == first){
				       		count++;
				 	}
					else{
						break;
					}
				}
				if(count >= K){
					if(first == 'B')blue=true;
					else if(first=='R')red=true;
				}
			}

		}
		// Check for diagonal K in row
		for(int row = K-1; row < N; row++){
			for(int col = 0; col <= N-K; col++){
				char first = rotated[row][col];
				int count = 1;
				for(int k = 1; k < K; k++){
					if(rotated[row-k][col+k] == first){
				       		count++;
				 	}
					else{
						break;
					}
				}
				if(count >= K){
					if(first == 'B')blue=true;
					else if(first=='R')red=true;
				}
			}

		}
		cout << "Case #" << tell << ": ";
		if(blue == false && red == false){
			cout << "Neither" << endl;
		}
		else if(blue == true && red == false){
			cout << "Blue" << endl;
		}
		else if(blue == false && red == true){
			cout << "Red" << endl;
		}
		else{
			cout << "Both" << endl;
		}
	}

}
