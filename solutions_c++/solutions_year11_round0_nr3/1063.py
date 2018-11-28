#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

void solve(int i) {
    int count = 0;
    cin >> count;
    vector<int> v;
    int xor_all = 0;
    while(count--) {
        int value;
        cin >> value;
        xor_all = xor_all ^ value;
        v.push_back(value);
    }
    if(xor_all != 0) {
        cout << "Case #" << i << ": " << "NO" << endl;
    } else {
        int sum = accumulate(v.begin(), v.end(), 0);
        cout << "Case #" << i << ": " << sum - *min_element(v.begin(), v.end()) << endl;
    }
}

int main(int argc, void **argv) {
    int N;
    cin >> N;
    for(int i=0;i<N;i++) {
        solve(i+1);
    }
}

