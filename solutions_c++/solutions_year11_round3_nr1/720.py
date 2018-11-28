#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int caseNum = 1; caseNum <= T; ++caseNum){
		int R, C;
		cin >> R >> C;
		vector<string> picture(R);
		for(int i = 0; i < R; ++i){ cin >> picture[i]; }
		for(int i = 0; i < R - 1; ++i){
			for(int j = 0; j < C - 1; ++j){
				if(
					picture[i][j] == '#' &&
					picture[i][j + 1] == '#' &&
					picture[i + 1][j] == '#' &&
					picture[i + 1][j + 1] == '#'
				){
					picture[i][j] = picture[i + 1][j + 1] = '/';
					picture[i][j + 1] = picture[i + 1][j] = '\\';
				}
			}
		}
		bool possible = true;
		for(int i = 0; i < R && possible; ++i){
			for(int j = 0; j < C && possible; ++j){
				if(picture[i][j] == '#'){ possible = false; }
			}
		}
		cout << "Case #" << caseNum << ":" << endl;
		if(possible){
			for(int i = 0; i < R; ++i){ cout << picture[i] << endl; }
		}else{
			cout << "Impossible" << endl;
		}
	}
	return 0;
}
