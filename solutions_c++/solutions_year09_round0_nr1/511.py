#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <list>
#include <vector>
#include <string>
#include <set>
using namespace std;

string getword() {
    char buf[1000];
    scanf("%s", buf);
    return buf;
}

int main(int argc, char* argv[]) {
    if (argc == 3) {
        freopen(argv[1], "r", stdin);
        freopen(argv[2], "w", stdout);
    }
    int l, d, n;
    scanf("%d%d%d", &l, &d, &n);
    vector<const string> sl;
    for (int i = d; i != 0; --i) {
        sl.push_back(getword());
    }
    for (int i = 1; i <= n; i++) {
        list<int> ml;
        for (vector<const string>::const_iterator it = sl.begin(); it != sl.end(); it++) {
            ml.push_back(it - sl.begin());
        }
        string str(getword());
        int pos = 0;
        for (int j = 0; j < l; j++) {
            set<char> poss;
            if (pos == str.length()) {
                ml.clear();
                break;
            }
            if (str[pos] == '(') {
                ++pos;
                for (char ch; ')' != (ch = str[pos++]);)
                    poss.insert(ch);
            } else
            {
                poss.insert(str[pos++]);
            }
            for (list<int>::iterator it = ml.begin(); it != ml.end();) {
                if (poss.find(sl[*it][j]) == poss.end()) {
                    ml.erase(it++);
                } else
                    ++it;
            }
        }
        printf("Case #%d: %d\n", i, ml.size());
    }
    if (argc == 3) {
        fclose(stdin);
        fclose(stdout);
    }
    return 0;
}
