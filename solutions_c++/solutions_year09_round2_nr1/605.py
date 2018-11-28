#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <map>
#include <set>
#include <string>
using namespace std;

int cases, cas = 1;
int n, m;
char buf[1024];
string text, line, name;
set<string> features;

string removeParentheses(const string& s) {
    int head, tail;
    for (unsigned i = 0; i < s.size(); ++i) if (s[i] == '(') {
        head = i + 1; break;
    }
    for (int i = (int) s.size() - 1; i >= 0; --i) if (s[i] == ')') {
        tail = i - 1; break;
    }
    return s.substr(head, tail - head + 1);
}

void leftAndRight(const string& s, string& left, string& right) {
    left = ""; right = "";
    int first = -1, second = -1, pos;
    for (pos = 0; pos < (int) s.size(); ++pos) if (s[pos] == '(') {
        first = pos; break;
    }
    if (first >= 0) {
        left += s[first]; int cnt = 1;
        for (pos = first + 1; pos < (int) s.size(); ++pos) {
            left += s[pos];
            if (s[pos] == '(') {
                cnt++;
            } else if (s[pos] == ')') {
                cnt--;
            }
            if (cnt == 0) {
                break;
            }
        }
        for (; pos < (int) s.size(); ++pos) if (s[pos] == '(') {
            second = pos; break;
        }
        if (second >= 0) {
            right += s[second]; cnt = 1;
            for (pos = second + 1; pos < (int) s.size(); ++pos) {
                right += s[pos];
                if (s[pos] == '(') {
                    cnt++;
                } else if (s[pos] == ')') {
                    cnt--;
                }
                if (cnt == 0) {
                    break;
                }
            }
        }
    }
}

struct Tree {
    Tree* left;
    Tree* right;
    string feature;
    double prob;
    Tree() : left(0), right(0), feature(""), prob(0.0) {
    }
    Tree(const string& feature, double prob) : left(0), right(0), feature(feature), prob(prob) {
    }
    ~Tree() {
        delete left;
        delete right;
    }
    void parse(const string& text) {
        string s = removeParentheses(text);
        sscanf(s.c_str(), "%lf%s", &prob, buf);
        feature = buf;
        string lf, rt;
        leftAndRight(s, lf, rt);
        if (lf != "") {
            left = new Tree();
            left->parse(lf);
        }
        if (rt != "") {
            right = new Tree();
            right->parse(rt);
        }
    }
    double calc(double p) {
        p *= prob;
        if (left == 0) {
            return p;
        }
        if (features.find(feature) != features.end()) {
            return left->calc(p);
        } else {
            return right->calc(p);
        }
    }
};

int main() {
    for (scanf("%d", &cases); cases--; ) {
        scanf("%d", &n);
        getline(cin, line);
        text = "";
        for (int i = 0; i < n; ++i) {
            getline(cin, line);
            text += line;
        }
        Tree tree;
        tree.parse(text);

        cin >> n;
        printf("Case #%d:\n", cas++);
        for (int loop = 0; loop < n; ++loop) {
            cin >> name >> m;
            features.clear();
            for (int i = 0; i < m; ++i) {
                cin >> name;
                features.insert(name);
            }
            double ans = tree.calc(1.0);
            printf("%.10lf\n", ans);
        }
    }
    return 0;
}
