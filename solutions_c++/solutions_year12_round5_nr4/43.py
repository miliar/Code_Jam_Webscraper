#include <iostream>
#include <cstdio>
#include <vector>
#include <cassert>
#include <map>
#include <set>
#include <string>

using namespace std;

void make(map<char, char>& mp, vector<char>& v, char c) {
    v.push_back(c);
    if (mp.count(c)) 
        v.push_back(mp[c]);
}

void solve() {
    map<char, char> mp;
    set< pair<char, char> > was;

    mp['o'] = '0';
    mp['i'] = '1';
    mp['e'] = '3';
    mp['a'] = '4';
    mp['s'] = '5';
    mp['t'] = '7';
    mp['b'] = '8'; 
    mp['g'] = '9'; 

    int k;
    cin >> k;
    assert(k == 2);
    string s;
    cin >> s;

    vector<int> d(255);
    for (int i = 0; i + 1 < s.length(); i++) {
        vector<char> start;
        vector<char> end;
        make(mp, start, s[i]);
        make(mp, end, s[i+1]);
        
        for (int si = 0; si < start.size(); si++)
            for (int ei = 0; ei < end.size(); ei++) {
                if (was.count( make_pair(start[si], end[ei]) )) 
                    continue;
                was.insert( make_pair(start[si], end[ei]) );

                d[start[si]]++;
                d[end[ei]]--;
            }
    }

    int neg = 0;
    int pos = 0;

    for (int i = 0; i < 255; i++) if (d[i] != 0) {
        if (d[i] > 0) pos += d[i];
        else neg += -d[i];
    }

    assert(pos == neg);
    int mx = pos - 1;
    if (mx < 0) mx = 0;

    static int test;
    cout << "Case #" << ++test << ": ";
    cout << was.size() + 1 + mx << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--)
        solve();
    return 0;
}
