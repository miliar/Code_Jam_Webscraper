#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

struct Num
{
    char c[100];

    Num() {
        memset(c, 0, sizeof(c));
    }

    Num(const string& s) {
        int i, len;

        memset(c, 0, sizeof(c));
        len = s.size();
        for(i=0;i<len;i++) {
            c[i] = s[len-1-i] - '0';
        }
    }

    bool is_zero() const {
        int i;

        for(i=0;i<100;i++) {
            if (c[i] != 0) {
                return false;
            }
        }
        return true;
    }
    
    bool operator==(const struct Num& n) const {
        int i;
        for(i=99;i>=0;i--) {
            if (c[i] > n.c[i]) {
                return false;
            }
            if (c[i] < n.c[i]) {
                return false;
            }
        }
        return true;
    }

    bool operator<=(const struct Num& n) const {
        int i;
        for(i=99;i>=0;i--) {
            if (c[i] > n.c[i]) {
                return false;
            }
            if (c[i] < n.c[i]) {
                return true;
            }
        }
        return true;
    }

    bool operator<(const struct Num& n) const {
        int i;
        for(i=99;i>=0;i--) {
            if (c[i] > n.c[i]) {
                return false;
            }
            if (c[i] < n.c[i]) {
                return true;
            }
        }
        return false;
    }

    void lshift() {
        int i;
        for(i=99;i>0;i--) {
            c[i] = c[i-1];
        }
        c[0] = 0;
    }

    void rshift() {
        int i;
        for(i=0;i<99;i++) {
            c[i] = c[i+1];
        }
        c[99] = 0;
    }

    Num operator-(const struct Num& n) const {
        Num ret;
        int i, borrow;

        borrow = 0;
        for(i=0;i<100;i++) {
            if ((c[i]-borrow) < n.c[i]) {
                ret.c[i] = c[i] - borrow - n.c[i] + 10;
                borrow = 1;
            } else {
                ret.c[i] = c[i] - borrow - n.c[i];
                borrow = 0;
            }
        }

        return ret;
    }
};

void print(const Num& n) {
    int i;

    if (n.is_zero()) {
        cout << "0";
        return;
    }

    i = 99;
    while (n.c[i] == 0) {
        i--;
    }

    for(;i>=0;i--) {
        cout << (char)(n.c[i]+'0');
    }
}


Num MOD(Num n0, Num n1) {
    int i;
    int cnt;

//     cout << "MOD" << endl;
//     cout << "n0=";
//     print(n0);
//     cout << endl;
//     cout << "n1=";
//     print(n1);
//     cout << endl;
    cnt = 0;
    while (n1 < n0) {
        n1.lshift();
        cnt++;
//         cout << "n1=";
//         print(n1);
//         cout << endl;
    }
    n1.rshift();

//     cout << "n1=";
//     print(n1);
//     cout << endl;

    for(i=0;i<cnt;i++) {
//         cout << "i=" << i << endl;
        while (n1 <= n0) {
            n0 = n0 - n1;
        }
        n1.rshift();
//         cout << "n0=";
//         print(n0);
//         cout << endl;
//         cout << "n1=";
//         print(n1);
//         cout << endl;
    }
    return n0;
}

Num GCD(Num n0, Num n1) {

//     cout << "GCD" << endl;
    while (true) {
//         cout << "n0=";
//         print(n0);
//         cout << endl;
//         cout << "n1=";
//         print(n1);
//         cout << endl;
        
        if (n0.is_zero()) {
            return n1;
        }
        if (n1.is_zero()) {
            return n0;
        }
        if (n0 == n1) {
            return n0;
        }
        if (n0 < n1) {
            n1 = MOD(n1, n0);
        } else {
            n0 = MOD(n0, n1);
        }
        
    }

}

int
main(void)
{
    int C, N;
    int i, j;
    string s;
    Num num[1000];
    Num num2[1000];
    Num gcd;

    cin >> C;
    

    for(i=1;i<=C;i++) {
        cin >> N;
        for(j=0;j<N;j++) {
            cin >> s;
            num[j] = Num(s);
//             cout << "num[" << j << "]=";
//             print(num[j]);
//             cout << endl;
        }
        for(j=0;j<(N-1);j++) {
            if (num[j] < num[j+1]) {
                num2[j] = num[j+1] - num[j];
            } else {
                num2[j] = num[j] - num[j+1];
            }
//             cout << "num2[" << j << "]=";
//             print(num2[j]);
//             cout << endl;
        }
        gcd = num2[0];
        for(j=1;j<(N-1);j++) {
            gcd = GCD(gcd, num2[j]);
//             cout << "gcd[" << j << "]=";
//             print(gcd);
//             cout << endl;
        }

        Num ans;

        ans = MOD(num[0], gcd);
        if (!ans.is_zero()) {
            ans = gcd - ans;
        }

        cout << "Case #" << i << ": ";
        print(ans);
        cout << endl;
    }
    
    return 0;
}
