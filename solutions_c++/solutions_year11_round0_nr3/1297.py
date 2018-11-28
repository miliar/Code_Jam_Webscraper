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
          int n;
          int s = 0;
          int sum = 0;
          int minv = 100000000;
          fin >> n;
          while (n-- > 0) {
            int i;
            fin >> i;
            s ^= i;
            if (i < minv) minv = i;
            sum += i;
          }
          if (s == 0) {
		fout << "Case #" << tind << ": " << sum-minv << endl;
          } else {
		fout << "Case #" << tind << ": NO" << endl;
          }
	}
	return 0;
}
