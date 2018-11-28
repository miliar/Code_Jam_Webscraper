#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <vector>
#include <map>

using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define foru(i,a,b) for (int i=(a);i<=(b);i++)
#define ford(i,a,b) for (int i=(a);i>=(b);i--)

const string s = "welcome to code jam";
const int nl = 19, prime = 10000;

int cas, len, res0;
char res[10], str[1000];
int g[100][100];

void solve() {    
    memset(g, 0, sizeof(g));
    g[0][0] = 1;
    res0 = 0;
    for (int i = 0; i <= nl; i++) 
        for (int j = 0; j <= len; j++) if (g[i][j] > 0) {
            if (i == nl) res0 = (res0 + g[i][j]) % prime;
            for (int k = j + 1; k <= len; k++) 
                if (s[i] == str[k - 1]) g[i + 1][k] = (g[i + 1][k] + g[i][j]) % prime;                            
        }    
    memset(res, 0, sizeof(res));
    for (int i = 3; i >= 0; i--) {
        res[i] = '0' + res0 % 10;
        res0 /= 10;
    }    
    res[4] = 0;
}    

int main() {
    scanf("%d", &cas);

    gets(str);
    for (int i = 0; i < cas; i++) {
        gets(str);
        len = strlen(str);
        solve();
        cout << "Case #" << i + 1 << ": " << res << endl;        
    }    
}    
