 #include <iostream>
using namespace std;

#define MAX_SIZE 50

int main(int argc, char **args)
{
	int tA;
	cin >> tA;
	for(int c=0; c < tA; c++) {
		int n, k, w=0, a=0, bb=0;
		cin >> n >> k;
		char b[n][n], t;
		for(int x=0; x < n; x++)
			for(int y=0; y < n; y++) {
				cin >> t;
				b[x][y] = t;
		}
		//Apply gravity
		for(int y=0; y < n; y++) {
			for(int x=0; x < n-1; x++) {
				if(b[y][x+1] == '.' && b[y][x] != '.') {
					b[y][x+1] = b[y][x];
					b[y][x] = '.';
					x=-1;
				}
			}
		}

		//for(int i=0; i < n; i++) { for(int j=0; j < n; j++) { cout << b[i][j]; } cout << endl; } 
		//Solve vertically
		for(int x=0; x < n; x++) {
			for(int y=0; y < n; y++) {
				if(b[x][y] == 'R') {
					a++;
					bb=0;
				}
				else if(b[x][y] == 'B') {
					bb++;
					a=0;
				}
				else {
					bb=0;
					a=0;
				}
				if(a == k)
					w |= 1;
				if(bb == k)
					 w|= 2;
			}a=0;bb=0;
		} 
		//cout << "Vertical done." << endl;
		//Solve horizontal
		for(int y=0; y < n; y++) {
			for(int x=0; x < n; x++) {
				if(b[x][y] == 'R') {
					a++;
					bb=0;
				}
				else if(b[x][y] == 'B') {
					bb++;
					a=0;
				}
				else {
					bb=0;
					a=0;
				}
				if(a == k)
					w |= 1;
				if(bb == k)
					 w|= 2;
			}a=0;bb=0;
		}

		for(int y=n-1; y >= 0; y--) {
			for(int x=0; x < n; x++) {
				for(int q=0; y-q >= 0 && x+q < n; q++) {
					if(b[y-q][x+q]=='R') {
						a++;
						bb=0;
					} else if(b[y-q][x+q]=='B') {
						bb++;
						a=0;
					}
					else {
						bb=0;
						a=0;
					}
					if(a == k)
						w |= 1;
					if(bb == k)
						w|= 2;
				}a=0;bb=0;
			}
		}

		for(int y=0; y < n; y++) {
			for(int x=0; x < n; x++) {
				for(int q=0; q+x < n && y+q < n; q++) {
					if(b[x+q][y+q]=='R') {
						a++;
						bb=0;
					} else if(b[x+q][y+q]=='B') {
						bb++;
						a=0;
					}
					else {
						bb=0;
						a=0;
					}
					if(a == k)
						w |= 1;
					if(bb == k)
						w|= 2;
				}a=0;bb=0;
			}
		}
		cout << "Case #" << c+1 << ": ";
		if(w == 3)
			cout << "Both" << endl;
		else if(w == 2)
			cout << "Blue" << endl;
		else if(w == 1)
			cout << "Red" << endl;
		else
			cout << "Neither" << endl;
	}
}
