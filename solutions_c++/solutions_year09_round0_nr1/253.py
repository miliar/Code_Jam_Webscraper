#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

struct Trie {
    map< char, Trie > entries;
    void Insert(string::iterator s, string::iterator end);
    size_t Count(vector< string >::iterator begin,
                 vector< string >::iterator end);
};

void Trie::Insert(string::iterator s, string::iterator end)
{
    if (s != end) {
        entries.insert(make_pair(*s, Trie()));
        entries[*s].Insert(s + 1, end);
    }
}

size_t Trie::Count(vector< string >::iterator begin,
                   vector< string >::iterator end)
{
    if (begin == end) {
        return 1;
    } else {
        size_t total = 0;
        for (string::iterator it = begin->begin(); it != begin->end(); ++it) {
            map< char, Trie >::iterator child = entries.find(*it);
            if (child != entries.end()) {
                total += child->second.Count(begin + 1, end);
            }
        }
        return total;
    }
}

int main()
{
    size_t L, D, N;
    cin >> L >> D >> N;

    Trie trie;
    for (size_t i = 0; i < D; ++i) {
        string word;
        cin >> word;
        trie.Insert(word.begin(), word.end());
    }

    for (size_t i = 0; i < N; ++i) {
        string wild;
        cin >> wild;
        vector< string > parsed;
        for (string::iterator it = wild.begin(); it != wild.end(); ++it) {
            if (*it == '(') {
                string::iterator close = find(it + 1, wild.end(), ')');
                parsed.push_back(string(it + 1, close));
                it = close;
            } else {
                parsed.push_back(string(it, it + 1));
            }
        }
        cout << "Case #" << i + 1 << ": "
             << trie.Count(parsed.begin(), parsed.end()) << "\n";
    }
}

