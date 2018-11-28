#include <iostream>

using namespace std;

int popcount(int v) {
    unsigned int c;
    for (c = 0; v; c++)
    {
      v &= v - 1;
    }
    return c;
}

int exists(int i, int pos) {
    pos --;
    if ((i >> (pos - 1)) & 1) {
        // Check how many before 
        int count = 0;
        for(int j = 0; j < (pos - 1); ++j) {
            if ((i >> j) & 1) {
                count++;
            }
        }
        return count + 1;
    }
    return -1;
}

bool check(int i, int n) {
    int pos = n;
    while (pos != 1) {
        pos = exists(i, pos);
        if (pos == -1) {
            return false;
        }
    }
    return true;
}

int solve(int n) {
    if (n == 2) {
       return 1;
    } 
    int count = 1;
    for(int i = 1; i < (1 << (n - 2)); ++i) {
        if(check(i, popcount(i) + 1)) {
            count ++;
        }
    }
    return count % 100003;
}

int main() {
    int n;
    cin >> n;
    for(int i = 0; i < n; ++i) {
        int val;
        cin >> val;
        cout << "Case #" << (i + 1) << ": " << solve(val) << endl;
    }
}
