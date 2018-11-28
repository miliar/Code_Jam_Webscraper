#include <iostream>
#include <cstddef>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <utility>
#include <boost/unordered_map.hpp>
#include <boost/foreach.hpp>

using namespace std;

typedef vector<unsigned long> Vector;

void proc(Vector& v, unsigned long L, unsigned long H)
{
    if (L == 1) {
        cout << "1" << endl;
        return;
    }
    if (v.size() == 0) {
        cout << "NO" << endl;
        return;
    }
    if (v.size() == 1) {
        if (v[0] >= L && v[0] <= H)
            cout << v[0] << endl;
        else
            cout << "NO" << endl;
        return;
    }

    for (unsigned long i = L; i <= H; ++i) {
        bool good = true;
        for (size_t j = 0; j < v.size(); ++j) {
            if (v[j] % i != 0 && i % v[j] != 0) {
                good = false;
                break;
            }
        }
        if (good) {
            cout << i << endl;
            return;
        }
    }
    cout << "NO" << endl;
    return;
}

int main(int argc, const char* argv[])
{
    size_t T;
    cin >> T;
    for (size_t test = 1; test <= T; ++test) {
        unsigned long N, L, H;
        cin >> N >> L >> H;
        Vector all;
        all.reserve(N);
        for (size_t i = 0; i < N; ++i) {
            unsigned long tmp;
            cin >> tmp;
            if (tmp != 1)
                all.push_back(tmp);
        }

        cout << "Case #" << test << ": ";
        proc(all, L, H);
    }
    return 0;
}
