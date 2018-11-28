#include <iostream>
#include <vector>

using namespace std;


char picture[50][50];

int main(int argc, char *argv[])
{
	int i, j, k;
	int test_nb;
	int row_size, column_size;
	char c;
	bool possible;
	
	cin >> test_nb;
	for (i = 0; i < test_nb; i++) {
		possible = true;
		cin >> row_size >> column_size;
		for (j = 0; j < row_size; j++) {
			for (k = 0; k < column_size; k++) {
				cin >> c;
				picture[j][k] = c;
			}
		}
		
		j = 0;
		k = 0;
		while (possible & (j < row_size)) {
			k = 0;
			while (possible & (k < column_size)) {
				if (picture[j][k] == '#') {
					if (j == (row_size - 1)) possible = false;
					else if (k == (column_size - 1)) possible = false;
					else {
						possible = possible && (picture[j][k+1] == '#');
						possible = possible && (picture[j+1][k+1] == '#');
						possible = possible && (picture[j+1][k] == '#');
						if (possible) {
							picture[j][k] = '/';
							picture[j][k+1] = '\\';
							picture[j+1][k+1] = '/';
							picture[j+1][k] = '\\';
						}
					}
				}
				k++;
			}
			j++;
		}
		
		cout << "Case #" << i+1 << ":" << endl;
		if (!possible) cout << "Impossible" << endl;
		else {
			for (j = 0; j < row_size; j++) {
				for (k = 0; k < column_size; k++) cout << picture[j][k];
				cout << endl;
			}
		}
	}
	
	return 0;
}
