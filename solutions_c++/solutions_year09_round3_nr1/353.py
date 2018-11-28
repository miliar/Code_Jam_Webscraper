#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>

using namespace std;

void doCase(int caseNum) {
    string num;

    cin >> num;

    map<char, int> counts;

    string::const_iterator sit;
    for (sit = num.begin(); sit != num.end(); sit++) {
        const char& c = *sit;

        counts[c]++;
    }

    int base = counts.size();
    if (base < 2) base = 2;
    
    map<char, int> vals;
    vector<int> digits;
    digits.reserve(num.size());

    // Starts with a 1
    vals[num[0]] = 1;

    int curVal = 0;
    for (sit = num.begin(); sit != num.end(); sit++) {
        const char& c = *sit;

        if (vals.count(c) == 0) {
            vals[c] = curVal;
            if (curVal == 0) {
                curVal = 2;
            } else {
                curVal++;
            }
        }
        int myVal = vals[c];

        digits.push_back(myVal);
    }

    long long currMult = 1;
    long long value = 0;
    vector<int>::reverse_iterator vit;
    for (vit = digits.rbegin(); vit != digits.rend(); vit++) {
        value += *vit * currMult;
        currMult *= base;
    }

    cout << "Case #" << caseNum << ": " << value << endl;
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        doCase(i+1);
    }
}
