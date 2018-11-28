#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <string.h>

using namespace std;

#define MAX 505
#define LEN 19
#define MOD 10000

char temp[MAX];

int len(int x) {
    if (x == 0) return 1;
    int res = 0;
    while(x != 0) {
        res++;
        x/=10;
    }
    return res;
}

int main() {
    freopen("c.in","r", stdin);
    freopen("c.out","w", stdout);

    string s = "welcome to code jam";

    int tests;
    cin >> tests;
    cin.getline(temp, MAX);

    int a[MAX][LEN];
    for (int q = 1; q <= tests; q++) {
        cin.getline(temp, MAX);
        int n = strlen(temp);

        memset(a,0,MAX*LEN*sizeof(int));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < s.length(); j++) {
                if (temp[i] == s[j]) {
                    if (j == 0) a[i][j] = 1;
                    else {
                        for (int k = 0; k < i; k++) {
                            a[i][j] += a[k][j-1];
                            a[i][j] %= MOD;
                        }
                    }
                }
            }
        }
        int res = 0;
        for (int i = 0; i < n; i++) {
            res += a[i][LEN-1];
            res %= MOD;
        }

        cout << "Case #" << q << ": ";

        int reslen = len(res);
        for (int i = 0; i < 4-reslen; i++) cout << "0";
        cout << res << endl;
    }

    return 0;
}
