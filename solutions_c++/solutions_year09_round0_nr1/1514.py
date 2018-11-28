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

string nm[20000], str;
int nl, res, L, D, N, chk[10000], a[10000];
char ns[1000000];
map<string,int> maps;

void solve() {
    int len = str.size(), now, tot = 0;
    nl = 0;
  //  cout << str << endl;
    for (int i = 0; i < len;) {
        if (str[i] == '(') {
            ns[nl++] = '(';
            i++;
            now = 0;
            while (str[i] != ')') {
                now |= (1 << (str[i] - 'a'));
                ns[nl++] = str[i];
                i++;
            }
            ns[nl++] = ')';
            a[tot] = now;
        } else {
            ns[nl++] = '(';
            ns[nl++] = str[i];
            ns[nl++] = ')';
            a[tot] = (1 << (str[i] - 'a'));
        }    
        tot++;        
        i++;
    }    
    ns[nl] = 0;
//    cout << ns << endl;
    tot = 0;
    for (int i = 0; i < D; i++) {        
        int ok = 1;
        for (int j = 0; j < L; j++) {
            if (a[j] & (1 << (nm[i][j] - 'a'))) continue;
            ok = 0;
        }    
        if (ok) tot++;
    }    
    res = tot;
}

int main() {
    cin >> L >> D >> N;
    for (int i = 0; i < D; i++) cin >> nm[i];    
    
    for (int cas = 0; cas < N; cas++) {
        cin >> str;
        solve();
        cout << "Case #" << cas + 1 << ": " << res << endl;
    }    
}    
