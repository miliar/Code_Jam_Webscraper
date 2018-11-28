#include <iostream>
#include <list>
using namespace std;

int t, tt, n, i;
list<long long> l1, l2;
list<long long>::iterator it1, it2, et;
long long res;

int main()
{
    cin >> t;
    for(tt = 1; tt <= t; ++tt)
    {
        l1.clear();
        l2.clear();
        cin >> n;
        for(i = 0; i < n; ++i)
        {
            cin >> res;
            l1.push_back(res);
        }
        for(i = 0; i < n; ++i)
        {
            cin >> res;
            l2.push_back(res);
        }

        res = 0;
        l1.sort();
        l2.sort();
        l2.reverse();
        et = l1.end();
        for(it1 = l1.begin(), it2 = l2.begin(); it1 != et; ++it1, ++it2)
            res += (*it1) * (*it2);
        cout << "Case #" << tt << ": " << res << endl;
    }
    return 0;
}
