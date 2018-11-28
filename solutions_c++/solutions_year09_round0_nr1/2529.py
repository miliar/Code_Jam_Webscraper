#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

vector<string> dicts;
vector<string> dicts_t;

int findNumOfMatch(string pattern, int dict_begin, int dict_end, int index)
{
    if (pattern == "#") return dict_end - dict_begin;

    int next = 0;
    vector<char> set;

    if (pattern[next++] != '(') {
        set.push_back(pattern[0]);
    }
    else {
        while (pattern[next] != ')') {
            set.push_back(pattern[next++]);
        }
        ++next;
    }

    int result = 0;
    vector<char>::iterator it;
    for (it = set.begin(); it < set.end(); ++it) {
        pair<string::iterator, string::iterator> bounds;
        bounds = equal_range(dicts_t[index].begin() + dict_begin, dicts_t[index].begin() + dict_end, *it);
        if (bounds.first == dicts_t[index].begin() + dict_end) continue;
        result += findNumOfMatch(pattern.substr(next),
                                 int(bounds.first - dicts_t[index].begin()),
                                 int(bounds.second - dicts_t[index].begin()),
                                 index + 1);
    }

    return result;
}

int main(int argc, char **argv)
{
    assert(argc > 1);
    ifstream fin(argv[1]);

    int L, D, N;
    fin >> L >> D >> N;

    dicts.resize(D);
    for (int i = 0; i < D; ++i) fin >> dicts[i];
    sort(dicts.begin(), dicts.end());

    dicts_t.resize(L);
    for (int i = 0; i < L; ++i) {
        for (int j = 0; j < D; ++j) {
            dicts_t[i].push_back(dicts[j][i]);
        }
    }

    for (int i = 0; i < N; ++i) {
        string pattern;
        fin >> pattern;
        cout << "Case #"
             << i + 1
             << ": "
             << findNumOfMatch(pattern + "#", 0, D, 0)
             << endl;
    }
    
    fin.close();

    return 0;
}
