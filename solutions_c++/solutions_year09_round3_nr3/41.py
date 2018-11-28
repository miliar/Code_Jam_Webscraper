#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int n;
int c[110];
int P;
int a[110][110];

int gao(int x, int y) {
    int &r = a[x][y];
    if (r != -1) return r;
    if (x > y) r = 0;
    else if (x == y) {
         r = c[x+1]-c[x-1]-2; 
    } else {
       for (int i = x; i<=y; ++i) {
          int r2 = gao(i+1, y)+ gao(x, i-1)+ c[y+1]-c[x-1]-2;
          if (r == -1 || r > r2) {
                r = r2;
          }
       }
    }
    return r;
}
void done() {
     memset(a, 0xff, sizeof(a));
     cout << gao(1, n-2) << endl;
}
int main() {
    int as;
    cin >> as;
    for (int kk=0; kk < as; ++kk) {
        cout << "Case #" << kk+1 << ": ";
        cin >> P >> n;
        c[0] = 0;
        c[n+1]=P+1;
        for (int i = 0; i < n; ++i)
            cin >> c[i+1];
        n += 2;
        done();
    }
    return 0;
}
