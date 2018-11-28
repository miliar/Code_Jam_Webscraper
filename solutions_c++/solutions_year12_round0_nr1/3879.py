#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <bitset>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <algorithm>
#include <complex>
#include <functional>
#include <limits>
#include <memory>
#include <numeric>
#include <utility>

using namespace std;
typedef long long Int;

map<char, char> mapping = {
    {' ', ' '},
    {'a', 'y'}, {'b', 'h'}, {'c', 'e'}, {'d', 's'}, {'e', 'o'},
    {'f', 'c'}, {'g', 'v'}, {'h', 'x'}, {'i', 'd'}, {'j', 'u'},
    {'k', 'i'}, {'l', 'g'}, {'m', 'l'}, {'n', 'b'}, {'o', 'k'},
    {'p', 'r'}, {'q', 'z'}, {'r', 't'}, {'s', 'n'}, {'t', 'w'},
    {'u', 'j'}, {'v', 'p'}, {'w', 'f'}, {'x', 'm'}, {'y', 'a'},
    {'z', 'q'}
};

int main() {
    int t; cin >> t; ws(cin);
    for(int x = 1; x <= t; ++x) {
        string s;
        getline(cin, s);
        ostringstream y;
        for(int i = 0; i < s.size(); ++i) {
            y << mapping[s[i]];
        }
        cout << "Case #" << x <<": " << y.str() << endl;
    }
}
