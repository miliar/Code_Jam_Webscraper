#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int TESTCASE;
    int n;
    long long k;
    cin >> TESTCASE;
    for (int CASE = 1 ; CASE <= TESTCASE ; CASE++) {
        cin >> n >> k;
        cout << "Case #" << CASE << ": ";
        k++;
        //cout << "pow" << (int)pow(2.,n) << endl;
        if (k % (int)pow(2., n) == 0) cout << "ON" << endl;
        else cout << "OFF" << endl;
    }
}
