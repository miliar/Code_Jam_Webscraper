#include <cstdio>
#include <algorithm>
#include <vector>
#include <sstream>
#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int cs = 1; cs <= T; cs++) {
        string s;
        cin >> s;

        if (!next_permutation(s.begin(), s.end())) {
            sort(s.begin(), s.end());
            int n = 0;
            while (s[n] == '0') n++;
            s = s.substr(n);
            s = string(1, s[0]) + string(n+1, '0') + s.substr(1);
        }

        cout << "Case #" << cs << ": " << s << endl;


    }
}
