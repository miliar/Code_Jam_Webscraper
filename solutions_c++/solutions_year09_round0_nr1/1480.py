#include <iostream>
#include <string>
#include <vector>
using namespace std;

typedef vector<string> VS;

int matches(string s, const VS &V) {
    VS ant = V, act;
    for (int j = 0, k = 0; j < s.size(); ++j) {
        string pat = "";
        if (s[j] == '(') {
            ++j;
            while (s[j] != ')')
                pat += s[j++];
        }
        else pat += s[j];
        for (int i = 0; i < ant.size(); ++i) {
            if (pat.find_first_of(ant[i][k]) != string::npos) {
                act.push_back(ant[i]);
            }
        }
        ant = act;
        act.clear();
        ++k;
        if (ant.size() == 0) return 0;
    }
    return ant.size();
}

int main() {
    int L, D, N, cases = 0;
    scanf("%d %d %d", &L, &D, &N);
    VS dict(D);
    for (int i = 0; i < D; ++i)
        cin >> dict[i];

    string s;
    while (N--) {
        cin >> s;
        int res = matches(s, dict);
        printf("Case #%d: %d\n", ++cases, res);
    }
}

