/*
  GCJ2010: Snapper Chain
*/
#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>

#define print(x) cout << #x" = " << x << endl

using namespace std;

long long N, K;

int main(void) {
    int t = 1, n;

    cin >> n;

    while(n--) {
        cin >> N >> K;

        while (N > 0 && (K % 2)) {
            K = K / 2;
            N--;
        }

        cout << "Case #" << t++ << ": ";

        if (N == 0) {
            cout << "ON";
        } else {
            cout << "OFF";
        }
        cout << endl;
    }

    return 0;
}
