#include <iostream>
#include <algorithm>

using namespace std;

void doCase(int caseNum) {
    int N, S, p;

    cin >> N >> S >> p;

    int mean;
    mean = max(0, p - 1);
    int minreg = mean * 3 + (p - mean);
    mean = max(0, p - 2);
    int minsurp = mean * 3 + (p - mean);

    int numreg = 0, numsurp = 0;

    for (int i = 0; i < N; i++) {
        int ti;
        cin >> ti;
        if (ti >= minsurp) numsurp++;
        if (ti >= minreg) numreg++;
    }

    int result = numreg + min(numsurp - numreg, S);

    cout << "Case #" << caseNum << ": " << result << endl;
}

int main() {
    int T;

    cin >> T;

    for (int i = 0; i < T; i++) {
        doCase(i+1);
    }
}
