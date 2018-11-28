#include <cstdio>
#include <cstdlib>
#include <cmath>

#include <iostream>
using namespace std;
typedef long long int64;

#define for0(i,n) for(int i=0; i<n; i++)

int main()
{
//	freopen("test.in","r",stdin); freopen("test.out","w",stdout);
	freopen("A-small-attempt0.in","r",stdin); freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin); freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);

//	freopen("test.in","r",stdin); freopen("test.out","w",stdout);
//	freopen("A-small-practice.in","r",stdin); freopen("A-small-practice.out","w",stdout);
//	freopen("A-large-practice.in","r",stdin); freopen("A-large-practice.out","w",stdout);

	int totalCases;
	cin >> totalCases;

	for (int caseNo = 1; caseNo <= totalCases; caseNo++) {
		
		int imax, jmax;
		cin >> imax >> jmax;

		char c[50][50] = {0};
		int blue = 0;

		for0(i,imax) {
			for0(j,jmax) {
				cin >> c[i][j];
				if (c[i][j] == '#')
					blue++;
			}
		}

		bool possible = true;
		if (blue % 4 != 0)
			possible = false;
		else
		for0(i,imax)
			for0(j,jmax)
				if (c[i][j] == '#') {
					c[i][j] = '/';
					
					if (j+1 < jmax && c[i][j+1] == '#')
						c[i][j+1] = '\\';
					else {
						possible = false;
						break;
					}
					
					if (i+1 < imax && c[i+1][j] == '#')
						c[i+1][j] = '\\';
					else {
						possible = false;
						break;
					}

					if (i+1 < imax && j+1 < jmax && c[i+1][j+1] == '#')
						c[i+1][j+1] = '/';
					else {
						possible = false;
						break;
					}
				}


		cout << "Case #" << caseNo << ": " << endl;
		if (!possible)
			cout << "Impossible" << endl;
		else {
			for0(i,imax) {
				for0(j,jmax)
					cout << c[i][j];
				cout << endl;
			}
		}
	}

	return 0;
}
