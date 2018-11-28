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

        int mismatches=0;
        for (int i = 0; i < N; i++) {
            int v;
            cin >> v;
            if (v != i+1) mismatches++;
        }


        cout << "Case #" << testCase << ": " << mismatches << endl;
    }
}

