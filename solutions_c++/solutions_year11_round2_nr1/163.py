#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


long double a[110][110];
int p[110];
int n;
long double wp[110], owp[110], oowp[110];

void Load()
{
	cin >> n;
	int i, j;
	char c;
	for (i = 0; i < n; i++) {
		wp[i] = owp[i] = oowp[i] = p[i] = 0;
		for (j = 0; j < n; j++) {
			cin >> c;
			if (c != '.') {
				p[i]++;
				a[i][j] = (int)c-(int)'0';
			} else a[i][j] = -1;
		}
	}

}

void Solve()
{
	int i, j;
	for (i = 0; i < n; i++) { 
		for (j = 0; j < n; j++) {
			if (a[i][j] > -0.5)
				wp[i] += a[i][j] / p[i];
		}
	}
	for (i = 0; i < n; i++) { 
		for (j = 0; j < n; j++) {
			if (a[i][j] > -0.5)
				owp[i] += (wp[j]*p[j] - (1-a[i][j])) / (p[j] - 1);
		}
		owp[i] /= p[i];
	}
	for (i = 0; i < n; i++) { 
		for (j = 0; j < n; j++) {
			if (a[i][j] > -0.5)
				oowp[i] += owp[j] / p[i];
		}
	}
	cout.setf(ios::fixed|ios::showpoint);
	cout.precision(12);
	for (i = 0; i < n; i++) {
		cout << 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] <<"\n";
	}


}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ":\n";
		Solve();
	}
	return 0;
}
