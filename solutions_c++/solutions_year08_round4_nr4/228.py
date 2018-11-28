
#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

int p [32];

int main ()
{
    int tests;
    scanf ("%d", &tests);
    for (int t = 1; t <= tests; ++t)
    {
        int k;
        string s;
        cin >> k >> s;
        for (int j = 0; j < k; ++j)
            p [j] = j;
        
        int res = 1 << 30;
        do
        {
            string cur = "";
            for (int j = 0; j < (int) s.size () / k; ++j)
                for (int z = 0; z < k; ++z)
                    cur += s [j * k + p [z]];
            int ans = 0;
            for (int j = 0; j < (int) cur.size (); ++j)
            {
                while (j + 1 < (int) cur.size () && cur [j] == cur [j + 1])
                    ++j;
                ++ans;
            }
            res = min (res, ans);
        } while (next_permutation (p, p + k));
        printf ("Case #%d: %d\n", t, res);
    }
    return 0;
}
