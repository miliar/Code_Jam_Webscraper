#include <iostream>
#include <set>
#include <map>
#include <vector>
using namespace std;

int res = 0;

void rec(int n, int l, set<string>& buena, vector<vector<char> >& posible, string s) {
    if (n == l) {
        ++res;
        return;
    }
    for (int i = 0; i < posible[n].size(); ++i) {
        string aux = s;
        aux += posible[n][i];
        if (buena.count(aux)) rec(n + 1, l, buena, posible, aux);
    }
}

int main() {
    int l, d, n;
    cin >> l >> d >> n;
    int caso = 1;
    set<string> buena;
    for (int i = 0; i < d; ++i) {
        string aux;
        cin >> aux;
        string s;
        for (int i = 0; i < aux.size(); ++i) {
            s += aux[i];
            buena.insert(s);
        }
    }
    while (n--) {
        string s;
        cin >> s;
        vector<vector<char> > posible(l);
        int act = 0, pos = 0;
        while (act < l) {
            if (isalpha(s[pos])) {
                posible[act].push_back(s[pos]);
                ++pos;
            }
            else if (s[pos] == '(') {
                ++pos;
                while (s[pos] != ')') {
                    if (isalpha(s[pos])) posible[act].push_back(s[pos]);
                    ++pos;
                }
                ++pos;
            }
            ++act;
        }
        res = 0;
        rec(0,l,buena,posible,"");
        cout << "Case #" << caso++ << ": " << res << endl;
    }
}
