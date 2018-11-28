#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
using namespace std;

void solve(int CASE)
{
    long long int n, x, y, s = 0;
    cin >> n;

    long long int unsplittable = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> x;
        unsplittable ^= x;
        y = (i == 0 ? x : min(y, x));
        s += x;
    }

    if (unsplittable) {
        printf("Case #%d: NO\n", CASE);
    } else {
        printf("Case #%d: %lld\n", CASE, s - y);
    }

}

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++)
        solve(i);

    return 0;
}
