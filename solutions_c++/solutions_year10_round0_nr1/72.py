#include<iostream>
#include<cstdio>

using namespace std;

int main() {
    long long n, k, T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cin >> n >> k;
        long long mask = (1 << n) - 1;
        printf("Case #%d: %s\n", t, ((k & mask) == mask) ? "ON" : "OFF");
    }
}

