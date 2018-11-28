#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <stack>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define DPRINT printf
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define MP(a,b) make_pair(a,b)


int main (void) {
    map<char, char> m;
    m.insert(MP(' ', ' '));
    m.insert(MP('\n', '\n'));
    m.insert(MP('a', 'y'));
    m.insert(MP('b', 'h'));
    m.insert(MP('c', 'e'));
    m.insert(MP('d', 's'));
    m.insert(MP('e', 'o'));
    m.insert(MP('f', 'c'));
    m.insert(MP('g', 'v'));
    m.insert(MP('h', 'x'));
    m.insert(MP('i', 'd'));
    m.insert(MP('j', 'u'));
    m.insert(MP('k', 'i'));
    m.insert(MP('l', 'g'));
    m.insert(MP('m', 'l'));
    m.insert(MP('n', 'b'));
    m.insert(MP('o', 'k'));
    m.insert(MP('p', 'r'));
    m.insert(MP('q', 'z'));
    m.insert(MP('r', 't'));
    m.insert(MP('s', 'n'));
    m.insert(MP('t', 'w'));
    m.insert(MP('u', 'j'));
    m.insert(MP('v', 'p'));
    m.insert(MP('w', 'f'));
    m.insert(MP('x', 'm'));
    m.insert(MP('y', 'a'));
    m.insert(MP('z', 'q'));

    int T;
    cin >> T;
    getchar(); // discard '\n'.
    REP(i, T) {
        cout << "Case #" << (i + 1) << ": ";
        char c;
        while ((c = getchar()), c != '\n' && c != EOF) {
            putchar(m[c]);
        }
        cout << endl;
    }
    return 0;
}


