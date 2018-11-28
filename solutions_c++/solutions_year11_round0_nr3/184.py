#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <algorithm>
#include <string>
#include <cmath>

#define D(x) x

using namespace std;

template<typename T>
ostream& operator <<(ostream& os, vector<T> v) {
    os << "[";
    for (int i = 0; i < v.size(); i++) {
        if (i > 0) os << ", ";
        os << v[i];
    }
    os << "]";
    return os;
}

int main() {
    int T;

    cin >> T;
    for (int testCase = 1; testCase <= T; testCase++) {
        int N;
        cin >> N;

        int total = 0, smallest = 10000000, xorsum = 0;
        for (int i = 0; i < N; i++) {
            int Ci;
            cin >> Ci;

            total += Ci;
            smallest = min(smallest, Ci);
            xorsum ^= Ci;
        }

        cout << "Case #" << testCase << ": ";
        if (xorsum) {
            cout << "NO" << endl;
        } else {
            cout << (total-smallest) << endl;
        }
    }
}

