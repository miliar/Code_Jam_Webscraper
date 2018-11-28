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
    ullong t, n;
    input>>t;
    for (ullong i = 0; i < t; i++) {
        ullong result = 0;
        input>>n;
        int a[n];
        int b[n];
        for (int j = 0; j < n; j++) {
            input>>a[j];
            input>>b[j];
            for (int m = 0; m < j; m++) {
                if ((a[j] < a[m] && b[j] > b[m]) || (a[j] > a[m] && b[j] < b[m]))
                    result++;
            }
        }
        output<<"Case #"<<i + 1<<": "<<result<<endl;
    }
}
