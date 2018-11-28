#include <cassert>
#include <cctype>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

int main()
{
    string line;
    getline(cin, line);
    int const n = atoi(line.c_str());
    vector<string> gs(n);
    for (int i = 0; i < n && getline(cin, gs[i]); ++i);
    vector<string> es(n);
    for (int i = 0; i < n && getline(cin, es[i]); ++i);

    map<char, char> m;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < gs[i].size(); ++j)
            if (islower(gs[i][j]))
                m[gs[i][j]] = es[i][j];

    m['q'] = 'z';
    set<char> no_in_gs;
    for (char c = 'a'; c <= 'z'; ++c)
        no_in_gs.insert(c);
    set<char> no_in_es = no_in_gs;
    for (auto p: m) {
        no_in_gs.erase(p.first);
        no_in_es.erase(p.second);
    }
    assert(no_in_gs.size() == 1 && no_in_es.size() == 1);
    m[*no_in_gs.begin()] = *no_in_es.begin();

    for (auto p: m)
        cout << p.second << '\n';
}
