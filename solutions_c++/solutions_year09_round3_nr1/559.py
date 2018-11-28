#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <ios>
#include <map>
#include <algorithm>
#include <iomanip>
#include <limits>

using namespace std;

int main(int argc, char* argv[])
{
	int N;
	cin >> N;

    for (int i = 1; i <= N; ++i) {
        string s;
        cin >> s;

        map<char, long long> m;
        m[s[0]] = 1ll;
        long long ind = 0ll;
        for (int j = 0; j < s.size(); ++j) {
            char c = s[j];
            if (m.find(c) == m.end()) {
                m[c] = ind;
                ++ind;
                if (ind == 1ll) ++ind;
            }
        }
        int base = m.size();
        if (base == 1) ++base;

        long long result = 0ll;
        long long fact = 1ll;
        for (int j = s.size() - 1; j >= 0; --j) {
            long long d = m[s[j]];
            //cout << d << " ";
            result += d * fact;
            fact *= base;
        }
        //cout << endl;

        cout << "Case #" << i << ": " << result << endl;
    }

	return 0;
}
