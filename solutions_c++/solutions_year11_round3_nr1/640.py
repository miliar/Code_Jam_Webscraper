#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
	int i, j, k, n, r, c, t, p, a[60][60];
	char cc;
	
	cin >> t;
	for (k=0; k<t; k++) {
		cin >> r >> c;
		n=0;
		for (i=0; i<r; i++) {
			for (j=0; j<c; j++) {
				a[i][j]=0;
				cin >> cc;
					if (cc=='#') {
						n++;
						a[i][j]=1;
					}
			}
		}
		p=0;
		for (i=0; i<r; i++) {
			for (j=0; j<c; j++) {
				if (a[i][j]==1) {
					p=1;
					if (a[i][j+1]*a[i+1][j]*a[i+1][j+1]==1){
						p=0;
						n-=4;
						a[i][j]=2;
						a[i][j+1]=3;
						a[i+1][j]=3;
						a[i+1][j+1]=2;
					}
				}
			}
		}
		cout << "Case #" << k+1 << ":" << endl;
		if (p+n) cout << "Impossible" << endl;
		else {
		for (i=0; i<r; i++) {
			for (j=0; j<c; j++) {
				if (a[i][j]==0) cout << ".";
				if (a[i][j]==1) cout << "#";
				if (a[i][j]==2) cout << "/";
				if (a[i][j]==3) cout << "\\";
			}
			cout << endl;
		}
		}
	}
	return 0;
}
