#include <iostream>
#include <iomanip> 
#include <string> 
#include <algorithm> 
#include <vector> 
#include <set> 
#include <map> 
#include <math.h> 
#include <cstdlib>
#include <queue>

using namespace std;

int main(void) {
	freopen("/Users/admin/Desktop/[Contests]/informatics/Cpl/be/a.in","r",stdin);
	freopen("/Users/admin/Desktop/[Contests]/informatics/Cpl/be/a.out","w",stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int r, c;
		char field[100][100];
		cin >> r >> c;
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				cin >> field[j][k];
			}
			scanf("\n");
		}
		bool flap = false;
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				if (field[j][k] == '#') {
					field[j][k] = '/';
					if (k+1 < c && field [j][k+1] == '#') {
						field[j][k+1] = '\\';
					} else {
						flap = true;
					}
					if (j+1 < r && field[j+1][k] == '#') {
						field[j+1][k] = '\\';
					} else {
						flap = true;
					}
					if (k+1 < c && j+1 < r && field[j+1][k+1] == '#') {
						field[j+1][k+1] = '/';
					} else {
						flap = true;
					}
				}
				
			}
			if (flap) break;
			
		}

		cout << "Case #" << i + 1<< ":\n";
		if (flap) {
			cout << "Impossible"<< endl;
		} else {
			for (int j = 0; j < r; j++) {
				for (int k = 0; k < c; k++) {
					cout << field[j][k];
				}
				cout << endl;
			}
		}
	}
		
		
	return 0;
}