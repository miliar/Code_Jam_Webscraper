#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>

#include <iostream>
#include <algorithm>
#include <memory>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>

#define TASK "a"
#define PB(x) push_back(x)
#define MP(x, y) make_pair(x, y)
#define CLR(x) memset(x, 0, sizeof(x))        
#define forn(i, n) for (int i = 0; i < n; i++)

using namespace std;

typedef long long int64;
typedef long double ldouble;
typedef pair<int, int> pii;
typedef vector<int> vi;

const int INF = 0x3f3f3f3f;
const int64 INF64 = (int64)INF * (int64)INF;

map<string, int> hash_code;
int hash(string str) {
    if (hash_code.count(str) == 0) hash_code[str] = hash_code.size();
    return hash_code[str];
}

vector<string> parse(string str) {
    vector<string> result;
    string cur = "";
    forn(i, str.length()) {
        if (str[i] == '/') {
            if (cur.length() > 0) result.PB(cur);
            cur = "";
        } else {
            cur += str[i];
        }
    }
    if (cur.length() > 0) result.PB(cur);
    return result;
}

string read_line() {
    char ch;
    string result;
    while (scanf("%c", &ch) != 0 && ch != '\n')
        result += ch;
    return result;
}

int n, m;

vector< map<int, int> > tree;

int add_new_vertex() {
    map<int, int> vertex;
    tree.PB(vertex);
    return tree.size() - 1;
}

bool add(int &start, string str) {
    bool result = false;
    int code = hash(str);
    if (tree[start].count(code) == 0) {
        result = true;
        tree[start][code] = add_new_vertex();
    }
    start = tree[start][code];
    return result;
}


int main() {
    freopen(TASK ".in", "rt", stdin);
    freopen(TASK ".out", "wt", stdout);
    int T;
    scanf("%d\n", &T);
    forn(i, T) {
        scanf("%d%d\n", &n, &m);
        tree.clear();
        hash_code.clear();
        int root = add_new_vertex();

        forn(j, n) {
            vector<string> words = parse(read_line());
            int start = root;            
            forn(k, words.size()) {
                add(start, words[k]);
            }
        }                

        int answer = 0;
        forn(j, m) {
            vector<string> words = parse(read_line());
            int start = root;            
            forn(k, words.size()) {
                answer += add(start, words[k]);
            }
        }

        printf("Case #%d: %d\n", i + 1, answer);   
    }


    return 0;
}
