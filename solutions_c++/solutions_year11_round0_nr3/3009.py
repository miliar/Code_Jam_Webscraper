#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>

using namespace std;

unsigned int candies[1000];

void split(unsigned int candies[], int *max, int sum, int rem, int index, unsigned int sean, unsigned int patrick) {
    index--;

    if (index < 0) {
        if (sean == patrick && rem > 0 && sum > *max) {
            *max = sum;
        }
        return;
    }

    unsigned int c = candies[index];
    split(candies, max, sum + c, rem, index, sean ^ c, patrick); 
    split(candies, max, sum, rem + c, index, sean, patrick ^ c); 
}

void solve() {
    memset(candies, 0, sizeof(candies));

    unsigned int n;
    cin >> n;

    for (unsigned int i = 0; i < n; ++i) {
        cin >> candies[i];
    }

    int max = 0;
    split(candies, &max, 0, 0, n, 0, 0);

    if (max) {
        cout << max;
    } else {
        cout << "NO";
    }
}

int main() {
    int nTest;
    cin >> nTest;
    
    for (int i = 1; i <= nTest; ++i) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
}
