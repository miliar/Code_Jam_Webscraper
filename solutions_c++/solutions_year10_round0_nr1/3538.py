#include<iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++) {
        int n, k;
        cin >> n >> k;

        bool isOn = (((k & ((1 << n) - 1)) == ((1 << n) - 1)) ? true : false);
        
        cout << "Case #" << i << ": " << (isOn ? "ON" : "OFF") << endl;
    }
    return 0;
}
