#include <iostream>
using namespace std;

inline void readAndSolve()
{
    int sum=0, xsum=0, mini=(1 << 20), n;
    cin >> n;
    for (int i=0; i < n; ++i)
    {
        int cur;
        cin >> cur;
        sum += cur;
        xsum ^= cur;
        if (cur < mini)
            mini = cur;
    }
    if (!xsum) cout << sum-mini << endl;
    else cout << "NO\n";
}

int main()
{
    int brt, testNo = 0;
    cin >> brt;

    while (brt --)
    {
        cout << "Case #" << ++testNo << ": ";
        readAndSolve();
    }
    return 0;
}
