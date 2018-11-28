#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <string>
#include <conio.h>
using namespace std;
#define FOR(i, a, b) for(int i=a; i<=b; i++)
#define DOW(i, a, b) for(int i=a; i>=b; i--)
#define FOREACH(it, c) for(typeof(c.begin()) it=c.begin(); it!=c.end(); it++)
#define RESET(c, val) memset(c, val, sizeof(c))

int test, a, b, key=0;
int fr[2000007], mu[10];

void solve(int a, int b) {
    int s=0, t=a;
    long long res=0;
    while (t!=0) s++, t/=10;
    FOR(n, a, b) {
        key++;
        FOR(i, 1, s) {
            int sta=n/mu[s-i+1];
            int fin=n%mu[s-i+1];
            int m  =fin*mu[i-1]+sta;
            if (n<m && m<=b && fr[m]<key) res++, fr[m]=key;
        }
    }
    cout << res;
}
int main() {
    freopen("CC.in", "r", stdin);
    freopen("test.out", "w", stdout);
    mu[0]=1;
    FOR(i, 1, 8) mu[i]=mu[i-1]*10;
    cin >> test;
    FOR(t, 1, test) {
        scanf("%d%d", &a, &b);
        cout << "Case #" << t << ": ";
        solve(a, b);
        if (t<test) cout << endl;
    }
    //getch();
    return 0;
}
