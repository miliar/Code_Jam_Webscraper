#include<iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    for(int i = 0; i < t; i++) {
        int n, k;
        cin >> n >> k;
        bool res = k != 0;
        for(int j = 0; j < n; j++) {
            res = res && k&(1<<j);
            if(!res) {
                break;
            }
        }
        cout << "Case #" << (i+1) << ": " << (res ? "ON" : "OFF") << endl;
    }
}
