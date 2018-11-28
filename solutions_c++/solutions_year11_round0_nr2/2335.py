#include <iostream>
#include <boost/unordered_map.hpp>
#include <utility>
#include <boost/foreach.hpp>
#include <string>
#include <vector>

using namespace std;

typedef boost::unordered_map<pair<char, char>, char> Rules;

int main(int argc, const char* argv[])
{
    size_t T;
    cin >> T;

    for (size_t test = 1; test <= T; ++test) {
        size_t C, D, N;
        Rules comb, opos;
        string input;
        cin >> C;
        for (size_t i = 0; i < C; ++i) {
            string tmp;
            cin >> tmp;
            comb[pair<char, char>(tmp[0], tmp[1])] = tmp[2];
            comb[pair<char, char>(tmp[1], tmp[0])] = tmp[2];
        }
        cin >> D;
        for (size_t i = 0; i < D; ++i) {
            string tmp;
            cin >> tmp;
            opos[pair<char, char>(tmp[0], tmp[1])] = 'x';
            opos[pair<char, char>(tmp[1], tmp[0])] = 'x';
        }
        cin >> N;
        cin >> input;

        // cout << input << endl;
        // BOOST_FOREACH(Rules::value_type& p, comb) {
        //     cout << p.first.first << " " << p.first.second << " : " << p.second << endl;
        // }
        // BOOST_FOREACH(Rules::value_type& p, opos) {
        //     cout << p.first.first << " " << p.first.second << " : " << p.second << endl;
        // }

        vector<char> ar;
        for (size_t i = 0; i < N; ++i) {
            ar.push_back(input[i]);
            if (ar.size() > 1) {
                Rules::iterator it = comb.find(pair<char, char>(ar.back(), ar[ar.size() - 2]));
                if (it != comb.end()) {
                    ar.pop_back();
                    ar.back() = it->second;
                }
            }
            if (ar.size() > 1) {
                for (size_t j = 0; j + 1 < ar.size(); ++j) {
                    Rules::iterator it = opos.find(pair<char, char>(ar.back(), ar[j]));
                    if (it != comb.end()) {
                        ar.clear();
                    }
                }
            }
        }

        cout << "Case #" << test << ": ";
        cout << "[";

        if (!ar.empty())
            cout << ar[0];
        for (size_t i = 1; i < ar.size(); ++i)
            cout << ", " << ar[i];
        cout << "]" <<  endl;
    }
    return 0;
}
