#include <string>
#include <iostream>
using namespace std;

int ts, l, i, j;
string s, p = "welcome to code jam";
int f[1000][30], M = 10000;

main() {
       freopen("c1.in", "r", stdin);
       freopen("3.out", "w", stdout);
       
       for (scanf("%d\n", &ts); ++l <= ts; ) {
           cout << "Case #" << l << ": ";
           getline(cin, s);
           for (i=0; i<s.size(); i++) {
               f[i][0] = f[i-1][0] + (s[i] == p[0]);
               if (i) for (j=1; j<19; j++)
                   f[i][j] = (f[i-1][j] + f[i-1][j-1] * (s[i] == p[j])) % M;
           }
           i = f[s.size()-1][18];
           cout << i / 1000 << i % 1000 / 100 << i % 100 / 10 << i % 10 << endl;
       }
}
