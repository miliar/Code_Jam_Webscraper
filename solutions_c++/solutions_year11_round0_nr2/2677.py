#include <algorithm>
#include <cstdio>
#include <iostream>
#include <list>
#include <map>
#include <vector>
using namespace std;
#define For(i,x) for (int i=0; i<(int)(x); i++)
#define mp make_pair

typedef vector<int> vi;

bool isClear(vi& v, map<pair<char, char>, int> & opposedMap) {
    for (int i = 0; i < (int)v.size(); i++) {
        for (int j = i+1; j < (int)v.size(); j++) {
            char a = v[i];
            char b = v[j];
            if (opposedMap[mp(min(a, b), max(a, b))])
                return true;
        }
    }
    return false;
}

void calc(map<pair<char, char>, char>& combineMap,
          map<pair<char, char>, int> & opposedMap,
          vi& cs) {
    vi v;
    For(i, cs.size()) {
        v.push_back(cs[i]);

        if (v.size() >= 2) {
            char a = v[v.size()-1];
            char b = v[v.size()-2];
            char c = combineMap[mp(min(a, b), max(a, b))];
            if (c > 0) {
                v.pop_back();
                v.pop_back();
                v.push_back(c);
            }
            else if (isClear(v, opposedMap))
                v.clear();
        }
    }

    printf("[");
    For(i, v.size()) {
        if (i > 0) printf(", ");
        putchar(v[i]);
    }
    puts("]");

}

int main() {
    int ncases;
    scanf("%d", &ncases);
    For(cc, ncases) {
        map<pair<char, char>, char> combineMap;
        map<pair<char, char>, int> opposedMap;

        char s[1000];
        int n;
        scanf("%d", &n);
        For(i, n) {
            scanf("%s", s);
            char a = min(s[0], s[1]);
            char b = max(s[0], s[1]);
            combineMap[mp(a, b)] = s[2];
        }
        scanf("%d", &n);
        For(i, n) {
            scanf("%s", s);
            char a = min(s[0], s[1]);
            char b = max(s[0], s[1]);
            opposedMap[mp(a, b)] = 1;
        }

        scanf("%d %s", &n, s);
        vi cs;
        for (int i = 0; s[i] != '\0'; i++)
            cs.push_back(s[i]);

        printf("Case #%d: ", cc+1);
        calc(combineMap, opposedMap, cs);
    }
}
