#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <utility>
#include <string>
#include <cstring>
using namespace std;

/*
 * if the input is 123456789011
 *
 * int a;
 * cin >> a;
 * a will we 2^31 - 1;
 *
 */
int r, c, d;
vector<string> weight;

vector<vector<int> > totalRow;
vector<vector<int> > totalCol;

bool ok(int r0, int c0, int n)
{
	int i, j;

	int totalr = 0;

	if (c0 == 0) {
	for (i=0,j=n-1; i<j; ++i,--j) {
		int a = totalRow[r0+i][c0+n-1];
		totalr += (j*2+1-n) * (totalRow[r0+j][c0+n-1] - a);
	}
	} else {
	for (i=0,j=n-1; i<j; ++i,--j) {
		int a = totalRow[r0+i][c0+n-1] - totalRow[r0+i][c0-1];
		totalr += (j*2+1-n) * (totalRow[r0+j][c0+n-1] - totalRow[r0+j][c0-1] - a);
	}
	}

	totalr -= (0*2+1-n) * (weight[r0+0][c0+0]);
	totalr -= (0*2+1-n) * (weight[r0+0][c0+n-1]);
	totalr -= ((n-1)*2+1-n) * (weight[r0+n-1][c0+0]);
	totalr -= ((n-1)*2+1-n) * (weight[r0+n-1][c0+n-1]);

	if (totalr != 0) return false;

	int totalc = 0;
	if (r0 == 0) {
	for (i=0,j=n-1; i<j; ++i,--j) {
		int a = totalCol[c0+i][r0+n-1];
		totalc += (j*2+1-n) * (totalCol[c0+j][r0+n-1] - a);
	}
	} else {
	for (i=0,j=n-1; i<j; ++i,--j) {
		int a = (totalCol[c0+i][r0+n-1] - totalCol[c0+i][r0-1]);
		totalc += (j*2+1-n) * (totalCol[c0+j][r0+n-1] - totalCol[c0+j][r0-1] - a);
	}
	}

	totalc -= (0*2+1-n) * (weight[r0+0][c0+0]);
	totalc -= ((n-1)*2+1-n) * (weight[r0+0][c0+n-1]);
	totalc -= (0*2+1-n) * (weight[r0+n-1][c0+0]);
	totalc -= ((n-1)*2+1-n) * (weight[r0+n-1][c0+n-1]);

	return totalc == 0;

	/*
	for (i=0; i<n; ++i) for (j=0; j<n; ++j) {
		int r = r0+i;
		int c = c0+j;
		
		//if (r==0&&c==0) continue;
		//if (r==0&&c==n-1) continue;
		//if (r==n-1&&c==0) continue;
		//if (r==n-1&&c==n-1) continue;

		//totalr += (i*2+1-n) * (weight[r][c]);
		//totalc += (j*2+1-n) * (weight[r][c]);
	}
	*/

	/*
	if (r0==1 && c0==1 && n==5) {
		cerr << totalr << ' ' << totalc << endl;
	}

	return totalr==0 && totalc==0;
	*/
}

bool ok(int n)
{
	int i, j;
	//cerr << n << endl;
	for (i=0; i+n<=r; ++i) for (j=0; j+n<=c; ++j) {
		if (ok(i, j, n)) {
			//cerr << i << ' ' << j << ' ' << n << endl;
			return true;
		}
	}

	return false;
}

string calc()
{
	stringstream S;
	int i, j;

	cin >> r >> c >> d;

	weight.resize(r);
	for (i=0; i<r; ++i) {
		cin >> weight[i];
	}

	for (i=0; i<r; ++i) for (j=0; j<c; ++j) {
		weight[i][j] -= '0';
	}

	totalRow.resize(r);
	for (i=0; i<r; ++i) {
		totalRow[i].resize(c);
		totalRow[i][0] = weight[i][0];
		for (j=1; j<c; ++j) {
			totalRow[i][j] = weight[i][j] + totalRow[i][j-1];
		}
	}

	totalCol.resize(c);
	for (i=0; i<c; ++i) {
		totalCol[i].resize(r);
		totalCol[i][0] = weight[0][i];

		for (j=1; j<r; ++j) {
			totalCol[i][j] = weight[j][i] + totalCol[i][j-1];
		}
	}


	int m = min(r, c);
	for (; m>=3; --m) {
		if (ok(m)) break;
	}

	if (m >= 3) {
		S << m;
	} else {
		S << "IMPOSSIBLE";
	}

	return S.str();
}

int main(void)
{
	int caseNum;
	cin >> caseNum;
	//string line;
	//getline(cin, line);
	for (int c=1; c<=caseNum; ++c) {
		cout << "Case #" << c << ": " << calc() << endl;
	}

	return 0;
}

