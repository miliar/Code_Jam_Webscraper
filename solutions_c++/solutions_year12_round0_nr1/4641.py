#include "iostream"
#include "cstdio"
#include "cstring"
#include "algorithm"
#include "vector"
#include "queue"
#include "cmath"
#include "string"
#include "cctype"
#include "map"
#include "iomanip"
using namespace std;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define lc(x) (x << 1)
#define rc(x) (x << 1 | 1)
#define lowbit(x) (x & (-x))
#define ll long long

int match[300];
void init(string a, string b) {
    for(int i = 0; i < a.length(); i++) {
        if(islower(a[i])) {
            match[a[i]] = b[i];
        }
    }
}

int main() {
    memset(match, -1, sizeof(match));
    string a, b;
    a = "ejp mysljylc kd kxveddknmc re jsicpdrysi",  b = "our language is impossible to understand";
    init(a, b);
    a = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",  b = "there are twenty six factorial possibilities";
    init(a, b);
    a = "de kr kd eoya kw aej tysr re ujdr lkgc jv",  b = "so it is okay if you want to just give up";
    init(a, b);
    match['q'] = 'z';
    match['z'] = 'q';
    string s;
    int T, Case = 1;
    freopen("A-small-attempt0.in", "r", stdin);
    cin >> T;
    getchar();
    while(T--) {
        getline(cin, s);
        printf("Case #%d: ", Case++);
        for(int i = 0; i < s.length(); i++) 
            if(islower(s[i])) putchar(match[s[i]]);
            else putchar(s[i]);
        cout << endl;
    }
    return 0;
}
