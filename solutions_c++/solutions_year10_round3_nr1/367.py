#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
struct Pairs {
    int a, b;
};

Pairs pairs[1001];

bool comp(const Pairs &p1, const Pairs &p2) {
        return p1.a < p2.a;
}

int main(void)
{
    int test, n;
    cin >> test;
    for (int ti=0; ti<test; ++ti) {
        cin >> n;
        for (int i=0; i<n; ++i)
            cin >> pairs[i].a >> pairs[i].b;
        sort(pairs, pairs + n, comp);
        int count = 0;
        for (int i=0; i<n; ++i)
            for (int j=i+1; j<n; ++j)
                if (pairs[i].b > pairs[j].b)
                    ++count;
        cout << "Case #" << ti+1 << ": " << count << endl;
    }

    return 0;
}
