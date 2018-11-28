#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

unsigned dpm[1024];
unsigned dpM[1024];


bool isp(unsigned n)
{
    if (n == 2 || n == 3)
        return true;
    for (unsigned t = 2; t <= n/2; ++t) {
        if ((n % t) == 0)
            return false;
    }
    return true;
}

map<unsigned, unsigned> f(unsigned a)
{
    map<unsigned, unsigned> m;
    unsigned n = a;
    for (unsigned t = 2; t <= a && n > 1; ++t)
    {
        if (isp(t) && (n % t) == 0) {
            while ((n % t) == 0) {
                m[t]++;
                n /= t;
            }
        }
    }

    return m;
}

unsigned m(unsigned i)
{
    if (dpm[i])
        return dpm[i];
    if (i == 1)
        return 1;
    if (i == 2)
        return 1;
    if (i == 3)
        return 2;

    unsigned s = m(i - 1);
    map<unsigned, unsigned> x = f(i);
    if (x.size() == 1 && x.begin()->second == 1)
        dpm[i] = s + 1;
    else
        dpm[i] = s;

    return dpm[i];
}

unsigned M(unsigned i)
{
    if (dpM[i])
        return dpM[i];
    if (i == 1)
        return 1;

    unsigned s = M(i - 1);
    map<unsigned, unsigned> x = f(i);
    if (x.size() == 1)
        dpM[i] = s + 1;
    else
        dpM[i] = s;

    return dpM[i];
}

int main()
{
    memset(dpm, 0, sizeof(dpm));
    memset(dpM, 0, sizeof(dpM));

    //cout << m(1) << " " << m(2) << " " << m(3) << endl;

    int nCase;
    cin >> nCase;

    for (int iCase = 1; iCase <= nCase; ++iCase) {

        unsigned n;
        cin >> n;

        unsigned d = M(n) - m(n);
        //cout << m(n) << " " << M(n) << endl;

        cout << "Case #" << iCase << ": " << d << endl;
    }
}

