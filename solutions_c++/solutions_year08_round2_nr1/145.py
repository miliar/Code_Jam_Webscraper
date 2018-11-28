#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <assert.h>

using namespace std;

typedef long long resulttype;

void skipEOL() { string foo; getline(cin,foo); }
resulttype OneCase() {
	cerr << "ONE CASE" << endl;

	resulttype result;

	long long int n, A, B, C, D, x0, y0, M;

	cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

	long long stat[3][3];

	memset(stat,0,sizeof(stat));
	int x = x0, y=y0;
	for (int i=0; i<n; ++i) {
		stat[x % 3][y % 3]++;
		x = (A*x+B) % M;
		y = (C*y+D) % M;
	}

	long long all =0, AAB=0, AAA=0;
	for (int i=0; i<3; ++i) for (int j=0; j<3; ++j) {
		for (int k=0; k<3; ++k) for (int l=0; l<3; ++l) {
			int u= (9-i-k) % 3;
			int v = (9-j-l) %3;
			if ((i!=k||j!=l) && (i!=u||j!=v) && (k!=u||l!=v))
				all += stat[i][j] * stat[k][l] * stat[u][v];
		}
	}
	for (int i=0; i<3; ++i) for (int j=0; j<3; ++j) {
		int u = (9-i-i) % 3;
		int v = (9-j-j) %3;
		if (i!=u || j!=v)
			AAB += stat[i][j] * (stat[i][j] -1) * stat[u][v];
	}
	for (int i=0;i<3; ++i) for (int j=0; j<3; ++j) {
		AAA += stat[i][j] * (stat[i][j] -1) * (stat[i][j]-2);
	}

	assert(all % 6 == 0);
	assert(AAB % 2 == 0);
	assert(AAA % 6 == 0);

	result = all/6 + AAB/2 + AAA/6;
	return result;
}

int main() {
	int Anz;
	cin >> Anz;
	skipEOL();
	for (int run=1; run<=Anz; ++run) {
		resulttype result = OneCase();

		cout << "Case #" << run << ": " << result << endl;
	}
	return 0;
};
