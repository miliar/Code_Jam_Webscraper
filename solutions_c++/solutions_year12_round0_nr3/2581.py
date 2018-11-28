#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int const max_ = 10000000;
bool a[max_+1];

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int A, B;
        cin >> A >> B;
        fill(a, a+A, false);
        fill(a+A, a+B+1, true);
        fill(a+B+1, a+max_+1, false);
        int res = 0;
        for (int j = A; j <= B; ++j) {
            if (a[j]) {
                a[j] = false;
                string s = to_string(j);
                int n = 1;
                for (int i = 0; i < s.size()-1; ++i) {
                    rotate(s.begin(), s.begin()+1, s.end());
                    int const val = atoi(s.c_str());
                    if (a[val] && s[0] != '0')
                        ++n;
                    a[val] = false;
                }
                res += n * (n-1) / 2;
            }
        }
        cout << "Case #" << i+1 << ": " << res << '\n';
    }
}
