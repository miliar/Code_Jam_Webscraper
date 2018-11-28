#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <ext/numeric>

using std::cin;
using std::cout;
using std::min;
using std::next_permutation;
using std::string;
using std::unique;
using std::vector;
using __gnu_cxx::iota;

int
main()
{
    int cases;
    cin >> cases;
    for (int i(0); i != cases; ++i) {
        int k;
        string s;
        cin >> k >> s;
        vector<int> perm(k);
        iota(perm.begin(), perm.end(), 0);
        ptrdiff_t least(50000);
        do {
            string test;
            for (string::iterator cur(s.begin()), end(s.end()); cur != end;
                    cur += k) {
                for (int j(0); j != k; ++j)
                    test.push_back(*(cur + perm[j]));
            }
            least = min(least, unique(test.begin(), test.end()) - test.begin());
        } while (next_permutation(perm.begin(), perm.end()));
        cout << "Case #" << (i + 1) << ": " << least << '\n';
    }
}
