#include <iostream>
#include <string>


using namespace std;

char b[50][50];

int main()
{
	int T;
	cin >> T;
	for(int testCase = 1; testCase <= T; ++testCase) {
		int R, C;
		cin >> R;
		cin >> C;
		for(int i = 0; i < R; ++i)
			for(int j = 0; j < C; ++j)
				cin >> b[i][j];
		bool impossible = false;
		impossible = false;
		for(int i = 0; i < R && !impossible; ++i){
			for(int j = 0; j < C; ++j) {
				if(b[i][j] == '#') {
					if(i < R - 1 && j < C - 1 && b[i][j+1] == '#' && b[i+1][j] == '#' && b[i+1][j+1] == '#') {
						b[i][j] = '/';
						b[i][j+1] = '\\';
						b[i+1][j] = '\\';
						b[i+1][j+1] = '/';
					}
					else {
						impossible = true;
						break;
					}
				}
			}
		}
		cout << "Case #" << testCase << ":" << endl;
		if(impossible)
			cout << "Impossible" << endl;
		else {
			for(int i = 0; i < R; ++i) {
				for(int j = 0; j < C; ++j)
					cout << b[i][j];
				cout << endl;
			}
		}
	}
	return 0;
}
