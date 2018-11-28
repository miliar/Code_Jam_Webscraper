#include <cstdlib>
#include <climits>
#include <sstream>
#include <string>
#include <iostream>
#include <cstdio>

// STL
#include <algorithm>
#include <vector>
#include <map> // contains multimap
#include <set> // contains multiset
#include <queue> // contains priority_queue
#include <deque>
#include <bitset>
#include <list>
#include <stack>


using namespace std;

void add(bitset<32>& b, long val) {
    bitset<32> dd((unsigned long)val);
    for (int i = 0; i < 32; ++i) {
        b[i] = dd[i] == b[i] ? 0 : 1;
    }
}


long split(stack<long> sean, stack<long> pat, long* candy, int len) {
    int t, l;

    if (len == 0) {
        if (sean.empty() || pat.empty()) return -1;

        bitset<32> s(0ul), p(0ul);
        long val = 0;

        while (! sean.empty() ) {
            add(s, sean.top());
            val += sean.top();
            sean.pop();
        }
        while (! pat.empty() ) {
            add(p, pat.top());
            pat.pop();
        }

        if (s.to_ulong() == p.to_ulong()) {
            return val;
        } else {
            return -1;
        }
    }

    sean.push(*candy);
    t = split(sean, pat, candy + 1, len - 1);
    sean.pop();

    pat.push(*candy);
    l = split(sean, pat, candy + 1, len - 1);
    pat.pop();

    return max(t,l);
}

long solve(int k) {
    long *candy = new long[k];
    stack<long> pat, sean;
    
    for (int i = 0; i < k; ++i) {
        cin >> candy[i];
    }

    return split(sean, pat, candy, k);
}


int main() {
    int numcase, k, val;

    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small.out", "w", stdout);

    cin >> numcase;
    for (int i = 0; i < numcase; ++i) {
        cin >> k;
        cout << "Case #" << i + 1 << ": ";
        val = solve(k);
        if (val < 0) cout << "NO" << endl;
        else cout << val << endl;
    }

    return 0;
}
