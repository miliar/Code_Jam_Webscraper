#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void readInput(vector<int>* prices) {
    int n;
    cin >> n;
    for(int i = 0; i < n; ++i) {
        int c;
        cin >> c;
        prices->push_back(c);
    }
}

void calc(const vector<int>& prices, int mask, int* sum, bool* ok) {
    *sum = 0;
    *ok = true;
    
    int xor1 = 0;
    int xor2 = 0;

    for(int i = 0; i < prices.size(); ++i) {
        if(mask & (1 << i)) {
            *sum += prices[i];
            xor1 ^= prices[i];
        } else {
            xor2 ^= prices[i];
        }
    }

    if(xor1 != xor2) {
        *ok = false;
    }
    cerr << "CALC MASK = " << mask << " " << *sum << " " << *ok << endl;
}


int solve(const vector<int>& prices) {
    int totalXor = 0;
    int minElement = 10000000;
    int total = 0;
    for(int i = 0; i < prices.size(); ++i) {
        totalXor ^= prices[i];
        minElement = min(minElement, prices[i]);
        total += prices[i];
    }
    if(totalXor) {
        return -1;
    } else {
        return total - minElement;
    }
}

void output(int caseNo, int answer) {
    cout << "Case #" << caseNo << ": ";
    if(answer > 0) {
        cout << answer;
    } else {
        cout << "NO";
    }
    cout << endl;
}

int main() {
    int n;
    cin >> n;
    for(int i = 0; i < n; ++i) {
        vector<int> prices;
        readInput(&prices);
        output(i + 1, solve(prices));
    }
    return 0;
}

