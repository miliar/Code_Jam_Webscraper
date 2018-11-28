//
//  main.c
//  codejam2012
//
//  Created by Петро Бойчук on 4/14/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <fstream>

using namespace std;

set<pair<long long, int> > sss;

vector<long long> toV(long long x) {
    vector<long long> r;
    while (x > 0) {
        r.push_back(x % 10);
        x /= 10;
    }
    return r;
}

vector<long long> shft(vector<long long> &v, long long k) {
    vector<long long> r;
    for (long long i=0; i<v.size(); i++) {
        r.push_back( v[(i+k) % v.size()]);
    }
    return r;
}

long long toI(vector<long long> &v) {
    long long r = 0;
    for (long long i=v.size()-1; i>=0; i--) {
        r *= 10;
        r += v[i];
    }
    return r;
}

void calc(vector<long long> &v, long long a, long long b, long long x){
    for (long long i=1; i<v.size(); i++) {
        vector<long long> s = shft(v, i);
        if(s[s.size() -1] != 0) {
            long long k = toI(s);
            if(k > x && k >=a && k <= b) {
                sss.insert(make_pair(x, k));
            }
        }
    }
}

void solve() {
    sss.clear();
    long long a,b;
    cin >> a >> b;
    long long result = 0;
    for (long long i=a; i<=b; i++) {
        vector<long long> v = toV(i);
        calc(v, a, b, i);
    }
    cout << sss.size();
    
    
}

int main(int argc, const char * argv[])
{
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    
    long long t;
    cin >> t;
    
    for (long long test = 1; test <= t; test++) {
        cout << "Case #" << test << ": ";
        cerr << "Case #" << test << endl;
        solve();
        cout << endl;
    }
    
    return 0;
}

