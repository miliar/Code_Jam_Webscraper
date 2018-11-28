#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
//#include <map>
//#include <queue>
#include <iomanip>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

string s[4];

bool wins(char ch) {
  int i, j;
  for (i = 0; i < 4; i++) {
    j = 0;
    while (j < 4 && (s[i][j] == 'T' || s[i][j] == ch)) j++;
    if (j >= 4) return true;

    j = 0;
    while (j < 4 && (s[j][i] == 'T' || s[j][i] == ch)) j++;
    if (j >= 4) return true;
  }

  j = 0;
  while (j < 4 && (s[j][j] == 'T' || s[j][j] == ch)) j++;
  if (j >= 4) return true;

  j = 0;
  while (j < 4 && (s[j][3-j] == 'T' || s[j][3-j] == ch)) j++;
  if (j >= 4) return true;

  return false;
}

bool full() {
  for (int i = 0; i < 4; ++i) {
    for (int j = 0; j < 4; ++j) if (s[i][j] == '.') return false;
  }
  return true;
}

int main()
{
	int tcase = 0;
	ifstream fin("z.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
		int i,j;
                for (i = 0; i < 4; ++i) {
                  fin >> s[i];
                }
                if (wins('X')) {
                  fout << "Case #" << tind << ": X won" << endl;
                } else if (wins('O')) {
                  fout << "Case #" << tind << ": O won" << endl;
                } else if (full()) {
                  fout << "Case #" << tind << ": Draw" << endl;
                } else {
                  fout << "Case #" << tind << ": Game has not completed"
                       << endl;
                }
	}
	return 0;
}
