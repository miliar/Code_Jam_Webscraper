#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <bitset>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>

#include <ext/numeric>
#include <ext/functional>

using namespace std;
using namespace __gnu_cxx;

char combiner[256][256];
int deleter[256][256];

int killers[256];

stack<char> table;

void push(char c){
    //cout << "pushing " << c << endl;
    table.push(c);
    for (int i = 0; i < 256; ++i)
        killers[i] += deleter[(int)c][i];
}

void pop(){
    char c = table.top();
    //cout << "popping " << c << endl;
    table.pop();
    for (int i = 0; i < 256; ++i)
        killers[i] -= deleter[(int)c][i];
}

void clear() {
    //cout << "clearing" << endl;
    while(!table.empty()) table.pop();
    memset(killers, 0, sizeof(killers));
}

void add(char c) {
    if (table.empty()) { 
        push(c);
        return;
    }
    char p = table.top();
    
    if (combiner[(int)c][(int)p]) {
        char t = combiner[(int)c][(int)p];
        pop();
        add(t);
        return;
    }

    if (killers[(int)c]) {
        clear();
        return;
    }
    push(c);
}

int main() {
    int ts;
    cin >> ts;
    for (int tc = 1; tc <= ts; ++tc) {
        memset(combiner, 0, sizeof(combiner));
        memset(deleter, 0, sizeof(deleter));
        memset(killers, 0, sizeof(killers));
        string elements;
        int c, d, n;
        cin >> c;
        for (int i = 0; i < c; ++i) {
            string a;
            cin >> a;
            combiner[(int)a[0]][(int)a[1]] = a[2];
            combiner[(int)a[1]][(int)a[0]] = a[2];
        }
        cin >> d;
        for (int i = 0; i < d; ++i) {
            string a;
            cin >> a;
            deleter[(int)a[0]][(int)a[1]]++;
            deleter[(int)a[1]][(int)a[0]]++;
        }
        cin >> n;
        cin >> elements;
        for (int i = 0; i < (int)elements.size(); ++i) {
            add(elements[i]);
        }
        vector<char> r;
        while(!table.empty()) {r.push_back(table.top()); table.pop();}
        reverse(r.begin(), r.end());
        cout << "Case #" << tc << ": [";
        if (r.size()) {
            cout << r[0];
            for (int i = 1; i < (int)r.size(); ++i)
                cout << ", " << r[i];
        }
        cout << "]" << endl;
    }
    return 0;
}