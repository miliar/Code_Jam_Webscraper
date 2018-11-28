
#include <iostream>
#include <cmath>

using namespace std;

unsigned int faculty(unsigned int n) {
    unsigned int value = 1;
    for (unsigned int i = 2; i <= n; ++i) {
        value *= i;
    }
    return value;
}

unsigned int derangements(unsigned int n) {
    double value = 0;
    for (unsigned int i = 0; i <= n; ++i) {
        value += (double) ((i % 2 == 1) ? -1 : 1) / faculty(i);
    }
    return (unsigned int) (value * faculty(n));
}

unsigned int nOverK(unsigned int n, unsigned int k) {
    return faculty(n) / faculty(k) / faculty(n - k);
}

double results[1001];

double calcFor(unsigned int n) {
    if (results[n] <= 0) {
        unsigned int xSide = faculty(n) - derangements(n);
        unsigned int otherSide = 1;
        for (unsigned int i = 2; i < n; ++i) {
            otherSide += derangements(i) * nOverK(n, i) * (calcFor(i) + 1);
        }
        otherSide += derangements(n);

        results[n] = (double) otherSide / xSide;
    }
    return results[n];
}

void init() {
    results[0] = results[1] = 0;
    results[2] = 2;
    for (unsigned int i = 3; i < 1001; ++i) {
        results[i] = 0;
    }
}

double doTestcase() {
    unsigned int n, value, atCorrectPlace = 0;
    cin >> n;
    for (unsigned int i = 0; i < n; ++i) {
        cin >> value;
        if (value == i + 1) {
            ++atCorrectPlace;
        }
    }

    if (atCorrectPlace >= n) {
        return 0;
    }
    return calcFor(n - atCorrectPlace);
}

int main(int argc, char *argv[]) {
    init();
    unsigned int t;
    cin >> t;
    for (unsigned int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": " << doTestcase() << endl;
    }
    return 0;
}

