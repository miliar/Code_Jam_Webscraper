#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

typedef long long ll;

ll ma = 2000000000;

int num[33][2];  //(a+b*sqrt(5)) ^ c

int main () {
    int i, j;
    num[0][0] = 1;
    num[0][1] = 0;
    num[1][0] = 3;
    num[1][1] = 1;
    for (i=2; i<33; i++) {
        int pa = num[i-1][0], pb = num[i-1][1];
        int a = pa*pa + 5*pb*pb;
        int b = 2*pa*pb;
        a %= 1000;
        b %= 1000;
        num[i][0] = a;
        num[i][1] = b;
    }
    int T, cse=0;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        int cnt = 1, a=1, b=0;
        while (n > 0) {
            if (n & 1) {
                int na, nb;
                na = a*num[cnt][0] + b*num[cnt][1]*5;
                nb = b*num[cnt][0] + a*num[cnt][1];
                a = na % 1000;
                b = nb % 1000;
            }
            cnt++;
            n >>= 1;
        }
        cout << "Case #" << ++cse << ": " << setfill('0') << setw(3) << (2*a-1)%1000 << endl;
    }
    return 0;
}
