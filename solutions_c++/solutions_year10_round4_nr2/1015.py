#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

typedef unsigned long long ulong;

ulong power(ulong base, ulong pwr) {
    ulong ret = 1;
    for (ulong i = 0; i < pwr; i++) {
        ret *= base;
    }
    return ret;
}


int main() {
    ifstream input("B-input.in");
    ofstream output("B-output.out");
    ulong t;
    input>>t;
    for (ulong i = 0; i < t; i++) {
        ulong p;
        input>>p;
        vector<int> miss;
        vector<vector<int> > price;
        for (ulong j = 0; j < power(2, p); j++) {
            int inp;
            input>>inp;
            miss.push_back(inp);
        }
        for (ulong j = 1; j < p + 1; j++) {
            vector<int> temp;
            for (ulong m = 0; m < power(2, p - j); m++) {
                int inp;
                input>>inp;
                temp.push_back(inp);
            }
            price.push_back(temp);
        }
        ulong answer = 0;
        for (ulong j = 0; j < p+1; j++) {
            for (ulong m = 0; m < miss.size(); m++) {
                if (miss[m] == j) {
                    int missable = j;
                    while (missable > 0) {
                        ulong maxprice = 0;
                        ulong pos = -1;
                        for (ulong g = p; g > 0; g--) {
                            if (price[g-1][m / power(2, g)] > maxprice) {
                                maxprice = price[g-1][m / power(2, g)];
                                pos = g;
                            }
                        }
                        if(pos != -1) {
                            price[pos-1][m/power(2, pos)] = 0;
                        }
                        missable--;
                    }
                    for (ulong g = p; g > 0; g--) {
                        answer += price[g - 1][m / power(2, g)];
                        price[g - 1][m / power(2, g)] = 0;
                    }
                }
            }
        }
        /*ulong answer = 0;
        
        for (ulong j = 0; j < price.size(); j++) {
            for (ulong m = 0; m < price[j].size(); m++) {
                answer+=price[j][m];
            }
        } */
        output<<"Case #"<<i + 1<<": "<<answer<<endl;
    }
}
