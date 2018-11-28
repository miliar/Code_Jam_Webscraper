#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <vector>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int k = 1; k <= T; ++k)
    {
        typedef pair<char, char> CharPair;
        map<CharPair, char> combos;
        set<CharPair> oposes;

        int c;
        cin >> c;

        for (int i = 0; i < c; ++i)
        {
            string s;
            cin >> s;
            combos[make_pair(s[0], s[1])] = s[2];
            combos[make_pair(s[1], s[0])] = s[2];
        }

        int d;
        cin >> d;

        for (int i = 0; i < d; ++i)
        {
            string s;
            cin >> s;
            oposes.insert(make_pair(s[0], s[1]));
            oposes.insert(make_pair(s[1], s[0]));
        }

        int n;
        cin >> n;

        string spell;
        cin >> spell;

        vector<char> result;
        result.reserve(n);

        for (int i = 0; i < n; ++i)
        {
            result.push_back(spell[i]);
            while ((result.size() > 1) &&
                   (combos.count(make_pair(*(result.end() - 1),
                                           *(result.end() - 2))) == 1))
            {
                char c1 = result.back();
                result.pop_back();

                char c2 = result.back();
                result.pop_back();

                result.push_back(combos[make_pair(c1, c2)]);
            }

            for (int j = 0; j < result.size() - 1; ++j)
            {
                if (oposes.count(make_pair(result.back(), result[j])) == 1) {
                    result.clear();
                    break;
                }
            }
        }

        cout << "Case #" << k << ": " << "[";

        for (size_t i = 0; i < result.size(); ++i)
        {
            if (i != 0)
                cout << ", ";
            cout << result[i];
        }

        cout << "]\n";


    }

    return 0;
}
