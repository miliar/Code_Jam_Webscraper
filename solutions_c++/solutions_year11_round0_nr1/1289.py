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
          int ans = 0;
          int lastpos[2] = {1,1};
          int waittime[2] = {0,0};
          fin >> n;
          int pos;
          char color;
          int robot;
          while (n--) {
            fin >> ws >> color >> pos;
            robot = (color == 'O') ? 0 : 1;
            int t = abs(pos - lastpos[robot]);
            if (waittime[robot] >= t) {
              t = 0;
            } else {
              t -= waittime[robot];
            }
            waittime[1-robot] += t + 1;
            ans += t + 1;
            waittime[robot] = 0;
            lastpos[robot] = pos;
          }
          fout << "Case #" << tind << ": " << ans << endl;
	}
	return 0;
}
