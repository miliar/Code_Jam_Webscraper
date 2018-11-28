#include <iostream>
#include <set>
#include <cmath>
using namespace std;

int pow10(int exp) {
    if(exp == 0) {
        return 1;
    }
    int temp = pow10(exp/2);    
    if(exp%2 == 0) {
        return temp*temp;
    }
    
    return temp*temp*10;
}

int suffle(int a, int b, int c) {
    //cout << c << endl;
    set<int> temp;
    int base = 1;
    int count = 0;
    double l = log10(c);
    int t = int(l);
    //cout << "t l " << t << " " << l << endl;
    int len = pow10(t+1);
   // cout << len << endl;
    while(base < b) {
        base *= 10;
        int d = c/base, e = c%base, f = e*(len/base)+d;
        //cout << d << " " << e << " " << f << " " << c << endl;
        if(t == int(log10(f)) && f != c && f >= a && f <= b) {
            //cout << c << " " << f << endl;
            temp.insert(f);
        }
    }
    
   // cout << endl << endl;
    return temp.size();
}

int solve(int a, int b) {
    int result = 0;
    for(int i = a; i <= b; ++i) {
        result += suffle(a, b, i);
    }
    
    return result/2;
}

int main() {
    int test;
    cin >> test;
    
    for(int i = 1; i <= test; ++i) {
        int a, b;
        cin >> a >> b;
        
        cout << "Case #" << i << ": " << solve(a, b) << endl;
    }
}
