#include<iostream>
#include<string>

using namespace std;

int R, C;
char pic[50][50];
int tiles;

int main() {
	int T;
	cin >> T;
	for (int testCase = 0; T--; testCase++) {
		cin >> R >> C;
		tiles = 0;
		for (int i = 0; i < R; i++) {
			string line; cin >> line;
			for(int j = 0; j < C; j++) {
				pic[i][j] = line[j];
				if (line[j] == '#') tiles++;
			}
		}		
		for (int i = 0; i < R - 1; i++) {			
			for (int j = 0; j < C - 1; j++) {
				if (pic[i][j] == '#' && pic[i][j] == pic[i][j+1] && pic[i][j] == pic[i+1][j] && pic[i][j] == pic[i+1][j+1]) {
					pic[i][j] = '/';
					pic[i][j+1] = '\\';
					pic[i+1][j] = '\\';
					pic[i+1][j+1] = '/';
					tiles -= 4;
				}
			}
		}
		cout << "Case #" << (testCase + 1) << ":" << endl;
		if (tiles) 
			cout << "Impossible" << endl;
		else 
			for (int i = 0; i < R; i++) {
				for (int j = 0; j < C; j++) cout << pic[i][j]; 
				cout << endl;
			}	
	}
	return 0;
}