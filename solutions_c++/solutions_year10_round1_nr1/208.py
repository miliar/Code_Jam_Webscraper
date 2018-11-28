#include <iostream>
#include <cmath>
using namespace std;

int test, n, kk;
char a[60][60];

int main() 
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	scanf("%i", &test);
	for (int tt = 1; tt <= test; tt++) {
		scanf("%i%i", &n, &kk);
			
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				cin >> a[i][j];

		for (int i = 0; i < n; i++)
			for (int j = n - 1; j >=0; j--) {
				int k = j - 1;
				while (a[i][j] == '.' && k >= 0) {
					swap(a[i][j],a[i][k]);
					k--;
				}
			}

		bool red = false, blue = false;
		for (int i = 0; i < n; i++) {
			int kR = 0, kB = 0, fR = 0, fB = 0;
			for (int j = 0; j < n; j++) {
				if (a[i][j] == 'R' && fR == 0) { kR = 1; fR = 1; fB = 0; }
				else if (a[i][j] == 'R' && fR == 1) kR++;
				else if (a[i][j] == 'B' && fB == 0) { kB = 1; fB = 1; fR = 0; }
				else if (a[i][j] == 'B' && fB == 1) kB++;
				else { fR = 0; fB = 0;}

				if (kR == kk) red = true;
				if (kB == kk) blue = true;
			}	
		}

		for (int j = 0; j < n; j++) {
			int kR = 0, kB = 0, fR = 0, fB = 0;
			for (int i = 0; i < n; i++) {
				if (a[i][j] == 'R' && fR == 0) { kR = 1; fR = 1; fB = 0; }
				else if (a[i][j] == 'R' && fR == 1) kR++;
				else if (a[i][j] == 'B' && fB == 0) { kB = 1; fB = 1; fR = 0; }
				else if (a[i][j] == 'B' && fB == 1) kB++;
				else { fR = 0; fB = 0;}

				if (kR == kk) red = true;
				if (kB == kk) blue = true;
			}	
		}

		for (int i = 0; i < n; i++) 
			for (int j = 0; j < n; j++) {
				int kR = 0, kB = 0, fR = 0, fB = 0, l = 0;
				while (i + l < n && j + l < n) {
					if (a[i + l][j + l] == 'R' && fR == 0) { kR = 1; fR = 1; fB = 0; }
					else if (a[i + l][j + l] == 'R' && fR == 1) kR++;
					else if (a[i + l][j + l] == 'B' && fB == 0) { kB = 1; fB = 1; fR = 0; }
					else if (a[i + l][j + l] == 'B' && fB == 1) kB++;
					else { fR = 0; fB = 0;}

					if (kR == kk) red = true;
					if (kB == kk) blue = true;
					l++;
				}	
			}

		for (int i = 0; i < n; i++) 
			for (int j = 0; j < n; j++) {
				int kR = 0, kB = 0, fR = 0, fB = 0, l = 0;
				while (i + l < n && j - l >= 0) {
					if (a[i + l][j - l] == 'R' && fR == 0) { kR = 1; fR = 1; fB = 0; }
					else if (a[i + l][j - l] == 'R' && fR == 1) kR++;
					else if (a[i + l][j - l] == 'B' && fB == 0) { kB = 1; fB = 1; fR = 0; }
					else if (a[i + l][j - l] == 'B' && fB == 1) kB++;
					else { fR = 0; fB = 0;}

					if (kR == kk) red = true;
					if (kB == kk) blue = true;
					l++;
				}	
			}

		cout << "Case #" << tt << ": ";
		if (red && blue)  cout << "Both\n";
		if (red && !blue)  cout << "Red\n";
		if (!red && blue)  cout << "Blue\n";
		if (!red && !blue)  cout << "Neither\n";
	}

	return 0;
}