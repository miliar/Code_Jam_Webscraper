#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef unsigned long long ullong;

int main() {
    ifstream input("A-small.in");
    ofstream output("A-small.out");
    ullong t, l, p, c;
    input>>t;
    for (ullong i = 0; i < t; i++) {
        ullong result = 0;
        input>>l>>p>>c;
        while (l * c < p) {
            ullong x1 = l, x2 = p;
            int counter = 0;
            while (x1 < x2) {
                x1 *= c;
                ullong x2_tmp = x2;
                x2_tmp /= c;
                if (x2_tmp * c == x2) {
                    x2 = x2_tmp;
                } else {
                    x2 = x2_tmp + 1;
                }
                counter++;
            }
            p = x1;
            result++;
        }
        output<<"Case #"<<i + 1<<": "<<result<<endl;
    }
}
