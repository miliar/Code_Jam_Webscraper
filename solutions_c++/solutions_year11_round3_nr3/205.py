#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

int main()
{
    int nCase;
    cin >> nCase;

    for (int iCase = 1; iCase <= nCase; ++iCase) {

        unsigned N, L, H;
        cin >> N >> L >> H;
        vector<unsigned> v;
        for (size_t i = 0; i < N; ++i) {
            unsigned n;
            cin >> n;
            v.push_back(n);
        }

        unsigned ans = 0;
        for (size_t c = L; c <= H; ++c) {
            bool f = true;
            for (size_t i = 0; i < v.size(); ++i) {
                if ((v[i] % c) && (c % v[i])) {
                    f = false;
                    break;
                }
            }
            if (f) {
                ans = c;
                break;
            }
        }

        cout << "Case #" << iCase << ": ";
        if (ans)
            cout << ans << endl;
        else
            cout << "NO" << endl;
    }
}

