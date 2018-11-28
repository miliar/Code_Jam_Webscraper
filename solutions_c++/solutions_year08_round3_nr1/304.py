// Problem A
// Problem's source: Google Code Jam - Round 1C
// Program by Plamen Petrov (C) 2008
// http://digitalphysics.org/~ppetrov

#include <iostream>
#include <vector>
#include <map>
#include <deque>
#include <algorithm>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);

    int test, tests, p, k, l, i, j;
    int p2, k2;
    long long res;
    int f[1024];

    cin >> tests;
    for(test=1; test<=tests; test++)
    {
        res=0;
        cin >> p >> k >> l;

        for(i=0; i<l; i++) { cin >> f[i]; }
        
        sort(f, f+l, greater<int>());
        
        p2=1; k2=1;
        for(i=0; i<l; i++) 
        {
            res+=((long long)f[i]*(long long)p2);
            k2++;
            if(k2>k) { p2++; k2=1; }
        }

        cout << "Case #" << test << ": " << res << endl;

    }

    return 0;
}
