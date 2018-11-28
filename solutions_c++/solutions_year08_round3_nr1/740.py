#include <stdio.h>
#include <assert.h>

#include <string>
#include <algorithm>
#include <functional>
#include <iostream>
#include <vector>
using namespace std;

typedef unsigned int uint;
typedef vector<int> VI;
typedef vector<VI> VII;


int P=0, K=0, L=0;

int get_next_pos(VI& kbrd) {
    if (kbrd.size() == 0) {
        return -1;
    }

    VI::iterator next = min_element(kbrd.begin(), kbrd.end());
    if (*next > P) {
        return -1;
    }
    int pos = *next;
    ++*next;
    return pos;
    //// get next key. if no more keys left - fall back to the first.
    //// get pos at the key. if no more pos - get next key.
    //// if no more keys - finita
    //for (int i=curr_key; i<K; i++) {
    //    if (kbrd[i]<P) {
    //        int pos = kbrd[i];
    //        kbrd[i]++;
    //        return pos;
    //    }
    //}
    //return -1;
}

void solve(VI& abc) {
    VI kbrd(K);
    // take the most frequent
    // place to the rightmost pos
    sort(abc.begin(), abc.end(), greater<int>());
    int result = 0;
    for (VI::iterator i=abc.begin(); i!=abc.end(); i++) {
        int f = *i;
        int pos = get_next_pos(kbrd);
        if (pos == -1) {
            cout << "Impossible" << endl;
            return;
        }
        result += (pos+1)*f;
    }
    cout << result << endl;
}


void main(int argc, char** argv) {

    string str;
    int CASES = 0;
    cin >> CASES;   getline(cin, str);

    for (int i=0; i<CASES; i++) {
        cin >> P;
        cin >> K;
        cin >> L;
        getline(cin, str);
        VI abc;
        for (int j=0; j<L; j++) {
            int f;
            cin >> f;
            abc.push_back(f);
        }
        getline(cin, str);
        printf("Case #%i: ", i+1);
        solve(abc);
    }
    return;
}

