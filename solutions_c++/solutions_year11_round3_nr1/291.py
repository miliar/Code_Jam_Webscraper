#include <iostream>
#include <string>
#include <fstream>

using namespace std;

ifstream fin("A.in");
ofstream fout("A.out");

#define cin fin
#define cout fout

int r, c;
char mat[60][60];

int main(){
	int T, test = 0;
	for(cin >> T; T--; ){
		cin >> r >> c;
		for(int i = 0; i < r; i++)
			for(int j = 0; j < c; j++)
				cin >> mat[i][j];
		bool fl = true;
		cout << "Case #" << ++test << ":" << endl;
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(mat[i][j] == '#'){
					if(i == r - 1 || j == c - 1 || mat[i][j+1] != '#' || mat[i+1][j] != '#' || mat[i+1][j+1] != '#')
						fl = false;
					else{
						mat[i][j] = '/';
						mat[i][j+1] = '\\';
						mat[i+1][j] = '\\';
						mat[i+1][j+1] = '/';
					}
				}
			}
		}
		if(fl){
			for(int i = 0; i < r; i++){
				for(int j = 0; j < c; j++)
					cout << mat[i][j];
				cout << endl;
			}
		}
		else cout << "Impossible" << endl;
	}
	return 0;
}
