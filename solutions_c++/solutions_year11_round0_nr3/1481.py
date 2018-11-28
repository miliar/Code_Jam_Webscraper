#include <iostream>
#include <string>
#include <cmath>
#include <cstring>
#include <cassert>
#include <vector>
#include <set>
#include <map>

using namespace std;


void doCase(int caseNum) {
    int N;

    cin >> N;

    int smallest = 0;
    long sum = 0;
    int xored = 0;
    for (int i = 0; i < N; i++) {
        int ci;
        cin >> ci;
        if (smallest == 0 || ci < smallest) smallest = ci;
        sum += ci;
        xored ^= ci;
    }

    if (xored != 0) {
        cout << "Case #" << caseNum << ": NO" << endl;
    } else {
        cout << "Case #" << caseNum << ": " << sum - smallest << endl;
    }
}

int main() {
    int T;

    cin >> T;

    for (int i = 0; i < T; i++) {
        doCase(i+1);
    }
}
