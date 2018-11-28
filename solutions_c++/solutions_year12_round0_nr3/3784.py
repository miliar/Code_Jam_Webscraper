/* 
 * File:   C.cpp
 * Author: Ants
 *
 * Created on April 14, 2012, 12:20 PM
 */

#include <cstdlib>
#include <iostream>
#include <cstring>

using namespace std;

typedef long long i64;

int len(int x) {
    int l = 0;
    while (x != 0) {
        l++;
        x /= 10;
    }
    return l;
}
int pow10(int x) {
    int res = 1;
    while (x != 0) {
        res *= 10;
        x--;
    }
    return res;
}

int rotate(int x) {
    int l = len(x);
    int l10 = pow10(l);
    do {
        x *= 10;
        x += x/l10;
        x %= l10;
    } while (len(x) != l);
    return x;
}

/*
 * 
 */
int main(int argc, char** argv) {
    int T;
    cin >> T;
    
    bool * checked = new bool[10000000];
    
    for (int t = 1; t <= T; t++) {
        memset(checked, 0, 10000000*sizeof(bool));
        
        int A, B;
        cin >> A >> B;
        
        
        i64 result = 0;
        for (int i = A; i <= B; i++) {
            if (checked[i]) continue;
            int l = len(i);
            int rots = 0;
            int k = i;
            do {
                checked[k] = true;
                if (k >= A && k <= B) rots++;
                k = rotate(k);
            } while (k != i);
            result += rots*(rots-1)/2;
        }
        cout << "Case #" << t << ": " << result << endl;
    }
    
    return 0;
}

