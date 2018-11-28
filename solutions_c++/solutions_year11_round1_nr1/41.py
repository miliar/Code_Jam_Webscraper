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

long long gcd(long long x, long long y) {
    while (y != 0) {
        long long t = y;
        y = x%y;
        x = t;
    }
    return x;
}


int main() {
    int T;

    cin >> T;
    for (int testCase = 1; testCase <= T; testCase++) {
        long long N;
        int PD, PG;
        cin >> N >> PD >> PG;

        bool result = true;

        long long g = gcd(PD, 100);

        if ((100/g) > N) result = false;

        if (PG == 0 && PD != 0) result = false;
        if (PG == 100 && PD != 100) result = false;

        cout << "Case #" << testCase << ": " << (result ? "Possible" : "Broken") << endl;
    }
}

