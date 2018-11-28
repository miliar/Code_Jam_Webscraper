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
#include <cstdio>
#include <cstdlib>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

const int n = 19;
const int mm = 10000;
const char str[] = "welcome to code jam";
int a[20][510];

int main()
{
        int tcase = 0;
        ifstream fin("z.in");
        //ofstream fout("z.out");
		FILE * f = fopen("z.out", "w+");
        fin >> tcase >> ws;
        for (int tind = 1; tind <= tcase; tind++)
        {
			string line;
			getline(fin, line);
			int l = line.length();
			mset(a, 0);
			for (int i = 0; i <= l; ++i) a[0][i] = 1;
			for (int j = 1; j <= n; ++j) {
				for (int i = 1; i <= l; ++i) {
					a[j][i] = a[j][i-1];
					if (line[i-1] == str[j-1]) a[j][i] = (a[j][i]+a[j-1][i-1])%mm;
				}
			}
			fprintf(f, "Case #%d: %04d\n", tind, a[n][l]);
          //fout << "Case #" << tind << ": " << ans << endl;
        }
			fclose(f);
        return 0;
}
