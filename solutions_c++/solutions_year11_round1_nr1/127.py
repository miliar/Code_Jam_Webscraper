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
          int n, pd, pg;
          fin >> n >> pd >> pg;
          bool ans = false;
          if (pg == 0 || pg == 100) {
            if (pd != pg) {
              ans = false;
            } else {
              ans = true;
            }
          } else {
            int i = 1;
            while (i <= n) {
              if (i * pd % 100 == 0) {
                ans = true;
                break;
              }
              ++i;
            }
          }

          fout << "Case #" << tind << ": "
               << (ans ? "Possible" : "Broken") << endl;
	}
	return 0;
}
