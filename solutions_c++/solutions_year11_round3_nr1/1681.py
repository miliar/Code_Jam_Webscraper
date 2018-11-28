#include <iostream>

using namespace std;

int main(){
	int t;
	int r,c;
	char data[51][51];
	int imp;
	int count;
	
	cin >> t;
	
	for (int i = 0; i < t; i++) {
		cin >> r >> c;
		count = 0;
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				cin >> data[j][k];
				if (data[j][k] == '#')
					count++;
			}
			data[j][c] = '.';
		}
		for (int j = 0; j < c; j++)
			data[r][j] = '.';
		
		if (count % 4 != 0) {
			cout << "Case #" << (i + 1) << ":" << endl;
			cout << "Impossible" << endl;
			continue;
		}
		
		imp = 0;
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				if (data[j][k] == '#') {
					if (data[j+1][k] != '#' ||
					    data[j][k+1] != '#' ||
					    data[j+1][k+1] != '#') {
						imp = 1;
						break;
					}
					data[j][k] = '/';
					data[j+1][k] = '\\';
					data[j][k+1] = '\\';
					data[j+1][k+1] = '/';
				}
			}
			if (imp)
				break;
		}
		
		if (imp) {
			cout << "Case #" << (i + 1) << ":" << endl;
			cout << "Impossible" << endl;
			continue;
		} else {
			cout << "Case #" << (i + 1) << ":" << endl;
			for (int j = 0; j < r; j++) {
				for (int k = 0; k < c; k++) {
					cout << data[j][k];
				}
				cout << endl;
			}
		}
	}
	
	return 0;
}