//
//  RecycledNumbers.cpp
//  Programs
//
//  Created by Shivendra Dayal on 14/04/12.
//  Copyright (c) 2012 sdayal@gmail.com. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <set>

using namespace std;

long flag[2000000];


long breakNum(long num, int position, int numsize) {
    long first, second;
    first = num/(long) pow((double)10,numsize-position);
    second = num % (long)pow((double)10,numsize-position);
    second *= (long)pow((double)10,position);
    return first+second;
}

int main() {
    int T;
    cin>>T;
    long A,B;
    
    for (int t=1; t<=T; t++) {
        int cases = 0;
        cin >> A >> B;
        int numsize = 1;
        long temp=A;
        while (temp/=10) numsize++;
        set<pair<long, long> > s;
        for (long n=A; n < B; n++) {
            s.clear();
            for (int i=1; i<numsize; i++) {
                long m = breakNum(n, i, numsize);
                if (n < m  && m <= B) {
                    s.insert(make_pair(n,m));
                }
            }
            cases+= s.size();
        }
        cout << "Case #" << t << ": " << cases << endl;
    }    
}