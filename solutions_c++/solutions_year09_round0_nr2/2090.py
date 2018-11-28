#include <iostream>
#include <vector>
#include <string.h>
using namespace std;

typedef struct structure {
	int i;
	int j;
}st;

int main()
{
	
	int t;
	cin >> t;
	int z = 1;
	while (z <= t) {
		int m, n;
		cin >> m >> n;
		int a[m+2][n+2];
		for (int i = 1 ; i <= m ; ++i) {
			for (int j = 1 ; j <= n ; ++j) {
				cin >> a[i][j];
			}
		}
		for (int i = 0 ; i < m+2 ; ++i) {
			a[i][0] = a[i][n+1] = 20000;
		}
		for (int i = 0 ; i < n+2 ; ++i) {
			a[0][i] = a[m+1][i] = 20000;
		}


		vector<st> vst;
		
		char b[m+1][n+1];
		memset(b, '0', sizeof(b));
		
		char ch = 'a';
		int x, y;
		int p, q;
		for (int i = 1 ; i <= m ; ++i) {
			for (int j = 1 ; j <= n ; ++j) {
				p = i;
				q = j;
				while(true) {
					
						if (b[i][j] == '0')
							b[i][j] = ch;
						else break;
						st st1;
						st1.i = i;
						st1.j = j;
						vst.push_back(st1);
						
						x = i; y = j;
						if (a[x][y] > a[i-1][j])
							x = i-1, y = j;
						if (a[x][y] > a[i][j-1])
							x = i, y = j-1;
						if (a[x][y] > a[i][j+1])
							x = i, y = j+1;
						if (a[x][y] > a[i+1][j])
							x = i+1, y = j;
					
						if (x == i && y == j)
							break;
						i = x; j = y;
						
				}
				
				if (b[x][y] != b[p][q]) {
					for (int k = 0 ; k < vst.size() ; ++k) {
						b[vst[k].i][vst[k].j] = b[x][y];
					}
				}
				
				ch = b[p][q];
				ch++;
				vst.clear();
				i = p;
				j = q;
			}
		}
		
		cout << "Case #" << z << ":" << endl;
		for (int i = 1 ; i < m+1 ; ++i) {
			for (int j = 1 ; j < n+1 ; ++j) {
				cout << b[i][j] << " ";
			}
			cout << endl;
		}
	z++;
	}
	return 0;
}

