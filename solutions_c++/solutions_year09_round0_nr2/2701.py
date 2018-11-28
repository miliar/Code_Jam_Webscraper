#include <string>
#include <iostream>
#include <vector>

using namespace std;

bool dbg=false;

vector<vector<int> > search_sink(vector<vector<int> > matrix,int row, int col){
	vector<vector<int> > field;
	
	for(int i=0;i<row;i++){
		vector<int> temp;
		for(int j=0;j<col;j++){
			int min=100;
			int min_direct=0;
			int now = matrix[i][j];
			if(i != 0 && matrix[i-1][j] < now && matrix[i-1][j] < min){
				min = matrix[i-1][j];
				min_direct = 1;
			}
			if(j != 0 && matrix[i][j-1] < now && matrix[i][j-1] < min){
				min = matrix[i][j-1];
				min_direct = 2;
			}
			if(j < col-1 && matrix[i][j+1] < now && matrix[i][j+1] < min){
				min = matrix[i][j+1];
				min_direct = 3;
			}
			if(i < row-1 && matrix[i+1][j] < now && matrix[i+1][j] < min){
				min = matrix[i+1][j];
				min_direct = 4;
			}
			temp.push_back(min_direct);
		}
		field.push_back(temp);
	}
	
	return field;
}

// row is tate
// col is yoko
void calc(int z){
	int row,col;
	cin >> row >> col;
	
	vector<vector<int> > matrix(row, vector<int>(col) );
	for(int i=0;i<row;i++){
		for(int j=0;j<col;j++){
			cin >> matrix[i][j];
		}
	}
	
	vector<vector<int> > mat2(row, vector<int>(col) );
	mat2 = search_sink(matrix,row,col);
	
if(dbg){
	for(int i=0;i<row;i++){
		for(int j=0;j<col;j++){
			if(j != 0) cout << " ";
			cout << mat2[i][j];
		}
		cout << endl;
	}
}
	
	vector<vector<char> > mat_char(row, vector<char>(col) );
	unsigned int sum=row*col;
	string chars = "0bcdefghijklmnopqrstuvwxyz";
	int chars_num = 0; bool change = false;
	
while(sum > 0){
	for(int i=0;i<row;i++){
		for(int j=0;j<col;j++){
			if(mat2[i][j] < 0) continue;
			switch(mat2[i][j]){
				case 0:
					mat_char[i][j] = chars[chars_num++];
					mat2[i][j] = -1; sum--;
					break;
				case 1:
					if(mat2[i-1][j] == -1){
						mat_char[i][j] = mat_char[i-1][j];
						mat2[i][j] = -1; sum--;
					}
					break;
				case 2:
					if(mat2[i][j-1] == -1){
						mat_char[i][j] = mat_char[i][j-1];
						mat2[i][j] = -1; sum--;
					}
					break;
				case 3:
					if(mat2[i][j+1] == -1){
						mat_char[i][j] = mat_char[i][j+1];
						mat2[i][j] = -1; sum--;
					}
					break;
				case 4:
					if(mat2[i+1][j] == -1){
						mat_char[i][j] = mat_char[i+1][j];
						mat2[i][j] = -1; sum--;
					}
					break;
			}
		}
	}
}
	
	char change_target = mat_char[0][0];
	for(int i=0;i<row;i++){
		for(int j=0;j<col;j++){
			if(mat_char[i][j] == change_target) mat_char[i][j] = 'a';
			if(mat_char[i][j] == '0') mat_char[i][j] = change_target;
		}
	}
	
	
	
	cout << "Case #" << z+1 << ":" << endl;
	for(int i=0;i<row;i++){
		for(int j=0;j<col;j++){
			if(j != 0) cout << " ";
			cout << mat_char[i][j] ;
		}
		cout << endl;
	}
}

int main(){
	int all;
	cin >> all;
	
	for(int z=0;z<all;z++){
		calc(z);
	}
	
	return 1;
}
