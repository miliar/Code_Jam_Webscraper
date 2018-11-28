#include <iostream>

using namespace std;

int gcd(int a, int b)
{
    if ( b == 0 )
        return a;
    return gcd(b, a%b);
}

int main()
{
    int t, pd, pg;
    long long n;
    cin >> t;
    for (int ca = 1; ca <= t; ++ca)
    {
        cout << "Case #" << ca << ": ";
        cin >> n >> pd >> pg;
        if ( pg == 0 )
        {
            if ( pd == 0 )
                cout << "Possible" << endl;
            else
                cout << "Broken" << endl;
            continue;
        }
        if ( pd == 0 )
        {
            if ( pg < 100 )
                cout << "Possible" << endl;
            if ( pg == 100 )
                cout << "Broken" << endl;
            continue;
        }
        pd = 100/gcd(pd, 100);
        pg = 100/gcd(pg, 100);
        if ( pg == 1 && pd != 1 )
        {
            cout << "Broken" << endl;
            continue;
        }
        if ( pd <= n )
            cout << "Possible" << endl;
        else
            cout << "Broken" << endl;
    }
    return 0;
}
