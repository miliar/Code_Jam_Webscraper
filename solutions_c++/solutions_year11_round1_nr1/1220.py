#include <deque>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

template <typename T> T inp() {T input; cin >> input; return input;}

#define for_count(n) for(int _i = 0; _i < n; ++_i)
#define fori(a, b) for (long long a = 1; a < b; ++a)

void execute_case(int tc);

int main(int argc, char ** argv)
{
    int nt = inp<int>();
    for (int tc = 1; tc <= nt; ++tc) {
        execute_case(tc);
    }
    return 0;
}

void execute_case(int tc)
{
    cout << "Case #" << tc << ": ";

    long long n = inp<long long>();
    long long pd = inp<long long>();
    long long pg = inp<long long>();
    
    if (pd == 0 && pg != 100) {
        cout << "Possible" << endl;
        return;
    }
    if (pg == 0 && pd != 0) {
        cout << "Broken" << endl;
        return;
    }
    if (pg == 100) {
        if (pd == 100) {
            cout << "Possible" << endl;
        } else {
            cout << "Broken" << endl;
        }
        return;
    }
    fori(i, n) {
        if ((i * 100) % pd == 0 && (i * 100) / pd <= n) {
            cout << "Possible" << endl;
            return;
        }
    }
    cout << "Broken" << endl;
}
