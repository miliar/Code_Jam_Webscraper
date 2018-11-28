#include <iostream>
#include <vector>
#include <sstream>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

// shift all the colour values to the extreme right
void rightShift(vector<vector<char> > &v){
	int size = int(v.size());
	for(int i = 0; i < size ; i++){
		int vacancy = 0;
		for(int j = size - 1; j >= 0; j--){
			if(v[i][j] == 'R' || v[i][j] == 'B'){
				v[i][size - vacancy - 1] = v[i][j];
				if(size - vacancy - 1 != j){
					v[i][j] = '.';
				}
				vacancy++;				
			}
		}
	}
}

vector<vector<char> > rotateBy90(vector<vector<char> > v){
	vector<vector<char> > t(int(v.size()), vector<char> (int(v.size()), '\0'));
	for(int col = 0, i = 0; col < int(v.size()); col++, i++){
		for(int row = int(v.size()) - 1, j = 0; row >= 0 ; row--, j++){
			t[i][j] = v[row][col];
		}
	}
	return t;
}

bool horizontal(vector<vector<char> > v, int k, char which){
	int size = int(v.size());
	for(int i = 0; i < size; i++){
		for(int j = 0; j < size; j++){			
			if(v[i][j] == which){
				int row = i, col = j, counter = 0;
				while(col < size){
					if(v[i][col] == which){
						counter++, col++;
						continue;
					}
					else	break;
				}
				if(counter == k)	return true;
			}
		}
	}
	return false;
}

bool vertical(vector<vector<char> > v, int k, char which){
	int size = int(v.size());
	for(int i = 0; i < size; i++){
		for(int j = 0; j < size; j++){
			if(v[i][j] == which){
				int row = i, col = j, counter = 0;
				while(row < size){
					if(v[row][j] == which){
						counter++, row++;
						continue;
					}
					else break;
				}
				if(counter == k)	return true;
			}
		}
	}
	return false;
}

bool leftDiagonal(vector<vector<char> > v,int k, char which){
	int size = int(v.size());
	for(int i = 0; i < size; i++){
		for(int j = 0; j < size; j++){
			if(v[i][j] == which){
				// moving along left diagonal, row increases and column decreases
				int row = i, col = j, counter = 0;
				while(row < size && col >= 0){
					if(v[row][col] == which){
						row++, col--, counter++;
						continue;
					}
					else	break;
				}
				if(counter == k)	return true;
			}
		}
	}
	return false;
}

bool rightDiagonal(vector<vector<char> > v, int k, char which){
	int size = int(v.size());
	for(int i = 0; i < size; i++){
		for(int j = 0; j < size; j++){
			if(v[i][j] == which){
				// moving along the right diagonal, row and column both increase
				int row = i, col = j, counter = 0;
				while(row < size && col < size){
					if(v[row][col] == which){
						row++, col++, counter++;
						continue;
					}
					else	break;
				}
				if(counter == k)		return true;
			}
		}
	}
	return false;
}

void print2D(vector<vector<char> > v){
	int size = int(v.size());
	for(int i = 0; i < size; i++){
		for(int j = 0; j < size; j++){
			cout<<v[i][j]<<" ";
		}
		cout<<endl;
	}
}

int main(){
	int cases = 0;
	cin>>cases;
	for(int c = 0; c < cases; c++){
		int N = 0, K = 0;
		cin>>N>>K;
		vector<vector<char> > v(N, vector<char>(N, 0));
		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				cin>>v[i][j];
			}
		}

		// gravity to the right
		rightShift(v);
		//print2D(v);
		// rotate by 90
		v = rotateBy90(v);

		// check horizontal
		bool redHorizontal = horizontal(v, K, 'R');
		bool blueHorizontal = horizontal(v, K, 'B');

		// check vertical
		bool redVertical = vertical(v, K, 'R');
		bool blueVertical = vertical(v, K, 'B');

		// check left diagonal
		bool redLeftDiagonal = leftDiagonal(v, K, 'R');
		bool blueLeftDiagonal = leftDiagonal(v, K, 'B');

		// check right diagonal
		bool redRightDiagonal = rightDiagonal(v, K, 'R');
		bool blueRightDiagonal = rightDiagonal(v, K, 'B');

		bool RED = redHorizontal || redVertical || redLeftDiagonal || redRightDiagonal;
		bool BLUE = blueHorizontal || blueVertical || blueLeftDiagonal || blueRightDiagonal;

		if(RED && BLUE){
			cout<<"Case #"<<c + 1<<": "<<"Both"<<endl;
		}
		else if(RED){
			cout<<"Case #"<<c + 1<<": "<<"Red"<<endl;
		}
		else if(BLUE){
			cout<<"Case #"<<c + 1<<": "<<"Blue"<<endl;
		}
		else	cout<<"Case #"<<c + 1<<": "<<"Neither"<<endl;
	}
	return 0;
}
