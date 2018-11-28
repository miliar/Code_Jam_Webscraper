#include <iostream>

using namespace std;

int gcd(long long a, long long b)
{
    if (a < b)
       return gcd(b, a);
    if (b == 0)
       return a;
    return gcd(b, a%b);
}

int main()
{
    long long T, t, N, Pd, Pg;
    cin >> T;
    for (t = 0; t < T; ++t)
    {
        cin >> N >> Pd >> Pg;
        long long g = gcd(100, Pd);
        // cout << g << endl;
        int newPd = 100 / g;
        cout << "Case #" << t+1 << ": ";
        if ((N == 0) && (Pd == 0) && (Pg == 0))
        {
               cout << "Possible" << endl;
               continue;
        }
        if ((newPd > N) || ((Pg == 100) && (Pd != 100)) || ((Pg == 0) && (Pd > 0)))
        {
               cout << "Broken" << endl;
               continue;
        }
        cout << "Possible" << endl;
    }
    return 0;
}
