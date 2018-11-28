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
#define maxn 100050
int L, R;

bool check(int a, int b) {
    string aa, bb;
    int alen = 0, blen = 0, tmp;
    int sa[maxn], pa = 0;
    int sb[maxn], pb = 0;
    tmp = a;
    while(tmp) {
        alen++; 
        sa[pa++] = tmp % 10;
        tmp /= 10;
    }
    tmp = b;
    while(tmp) {
        blen++; 
        sb[pb++] = tmp % 10;
        tmp /= 10;
    }
    if(alen != blen) return false;
    for(int i = 0; i < 2 * pa; i++) aa += (sa[i % pa] + '0');
    for(int i = 0; i < pb; i++) bb += (sb[i] + '0');
    if(aa.find(bb) != string::npos) return true;
    return false;
}

bool checklen(int a, int b) {
    int alen = 0, blen = 0, tmp;
    tmp = a;
    while(tmp) {
        alen++; 
        tmp /= 10;
    }
    tmp = b;
    while(tmp) {
        blen++; 
        tmp /= 10;
    }
    return alen == blen;
}
int main() {
    freopen("C-small-attempt2.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, Case = 1;
    cin >> T;
    while(T--) {
        cin >> L >> R;
        int ans = 0;
        for(int i = L; i <= R; i++) {
            for(int j = i + 1; j <= R; j++) {
                if(!checklen(i, j)) break; 
                if(check(i, j)) ans++;
            }
        }
        printf("Case #%d: %d\n", Case++, ans);
    }
    return 0;
}
