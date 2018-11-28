
//  Copyright(c) 2009-2011, all rights reserved.
//  written by ZHUMAZHANOV ADLET.

#include <iostream>
#include <iterator>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <bitset>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>

#define FILE_NAME       "a"
#define SZ(v)           static_cast<int>(v.size())

#define sqr(x)          ((x) * (x))
#define all(v)          v.begin(), v.end()

#define Assert(cond, msg) {\
    if (! (cond)) {\
        fprintf(stderr, "%s:%d: Error: %s", __FILE__, __LINE__, msg);\
        exit(EXIT_FAILURE);\
    }\
}

#define loop(i, a, b)   for (int i = static_cast<int>(a); i <= static_cast<int>(b); ++ i)
#define clr(a, b)       memset(a, (b), sizeof(a))

#define printx(x)       cerr << #x << " = " << x << "\n"
#define sign(a)         ((a) > 0 ? +1 : (a) < 0 ? -1 : 0)

#define forn(i, n)      loop(i, 0, n - 1)
#define forv(i, v)      forn(i, SZ(v))

typedef unsigned int uint;
typedef unsigned long long ui64;

typedef long long i64;

using namespace std;

int c;
int d;
int n;

int T;

map<pair<char, char>, char> set_c;
map<char, char> set_d;

vector<char> answer;

void print_answer(vector<char> &answer) {
    cout << "[";
    if (! answer.empty()) cout << answer[0];
    loop(i, 1, SZ(answer) - 1) cout << ", " << answer[i];
    cout << "]";
}

int main(int argc, char** argv)
{
    ios_base::sync_with_stdio(false);

    Assert (freopen(FILE_NAME".in", "r", stdin), "cannot creat input-file");
    Assert (freopen(FILE_NAME".out", "w", stdout), "cannot creat output-file");

    cin >> T;

    char u;
    char v;
    char w;

    loop(test, 1, T) {

        set_c.clear();
        set_d.clear();

        answer.clear();

        cin >> c;
        forn(i, c) {
            cin >> u >> v
                >> w;
            if (u > v) swap(u, v);
            set_c[make_pair(u, v)] = w;
            set_c[make_pair(v, u)] = w;
        }

        cin >> d;
        forn(i, d) {
            cin >> u >> v;
            if (u > v) swap(u, v);
            set_d[u] = v;
            set_d[v] = u;
        }

        cin >> n;

        forn(i, n) {
            cin >> w;
            answer.push_back(w);

            while (SZ(answer) > 1) {
                u = answer.back();
                answer.pop_back();
                v = answer.back();
                answer.pop_back();
                w = set_c[make_pair(u, v)];
                if (w > 0) {
                    if (find(all(answer), set_d[w]) != answer.end()) {
                        answer.clear();
                    } else {
                        answer.push_back(w);
                    }
                } else {
                    answer.push_back(v);
                    if (find(all(answer), set_d[u]) != answer.end()) {
                        answer.clear();
                    } else {
                        answer.push_back(u);
                        break;
                    }
                }
            }
        }

        cout << "Case #" << test << ": ";
        print_answer(answer);

        cout << "\n";
    }

    return EXIT_SUCCESS;
}
