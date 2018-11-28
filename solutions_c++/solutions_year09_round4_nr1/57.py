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

int main()
{
	int tcase = 0;
	ifstream fin("z.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
		string s;
		int n, i;
		int a[50];
		fin >> n;
		for (i = 0; i < n; ++i) {
			fin >> s;
			a[i] = 0;
			for (int j = 0; j < n; ++j) {
				if (s[j] == '1') a[i] = j;
			}
		}

		int ans = 0;
		for (int i = 0; i < n; ++i) {
			if (a[i] <= i) continue;
			int j = i+1;
			while (j < n && a[j] > i) ++j;
			for (int k = j; k > i; k--) {
				swap(a[k], a[k-1]);
				ans++;
			}
		}
		fout << "Case #" << tind << ": " << ans << endl;
	}
	return 0;
}
