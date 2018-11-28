#include <cstdio>
#include <iostream>

using namespace std;

bool is_square(long long a) {
    long long lo = 0, hi = 1LL<<31;
    while(lo < hi) {
        long long mid = (lo+hi)/2;
        if(mid*mid < a)
            lo = mid+1;
        else
            hi = mid;
    }

    return lo*lo == a;
}

string input;
string cur, ans;

void backtrack(int pos, long long num) {
    if(pos == (int)input.size()) {
        if(is_square(num))
            ans = cur;
        return;
    }

    if(input[pos] == '0' || input[pos] == '?') {
        cur[pos] = '0';
        backtrack(pos+1, 2*num);
    }

    if(input[pos] == '1' || input[pos] == '?') {
        cur[pos] = '1';
        backtrack(pos+1, 2*num+1);
    }
}

int main() {
    int t;
    cin >> t;

    for(int z = 1; z <= t; z++) {
        cin >> input;
        cur = input;
        backtrack(0, 0);

        cout << "Case #" << z << ": " << ans << endl;
    }
}
