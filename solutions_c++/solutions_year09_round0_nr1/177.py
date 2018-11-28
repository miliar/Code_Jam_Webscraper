#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

inline void get_data(const size_t &L, vector< set<char> > &parsed_data) {
    string raw_data;
    cin >> raw_data;
    bool in_parenthesis = false;
    size_t cursor = 0;
    for (size_t i = 0; i < raw_data.size(); ++i) {
        if (raw_data[i] == '(') {
            in_parenthesis = true;
        } else if (raw_data[i] == ')') {
            in_parenthesis = false;
            ++cursor;
        } else if (in_parenthesis) {
            parsed_data[cursor].insert(raw_data[i]);
        } else {
            parsed_data[cursor].insert(raw_data[i]);
            ++cursor;
        }
    }
    assert(cursor == L);
}

inline bool match_data(const string &str, const vector< set<char> > &parsed_data) {
    for (size_t i = 0; i < parsed_data.size(); ++i) {
        if (parsed_data[i].find(str[i]) == parsed_data[i].end())
            return false;
    }
    return true;
}

int main() {
    size_t L, D, N;
    cin >> L >> D >> N;
    vector<string> dictory(D);
    for (size_t i = 0; i < D; ++i) {
        cin >> dictory[i];
    }
    for (size_t cases = 1; cases <= N; ++cases) {
        vector< set<char> > parsed_data(L);
        get_data(L, parsed_data);
        size_t count = 0;
        for (size_t i = 0; i < dictory.size(); ++i) {
            if (match_data(dictory[i], parsed_data))
                ++count;
        }
        cout << "Case #" << cases << ": " << count << endl;
    }
}
