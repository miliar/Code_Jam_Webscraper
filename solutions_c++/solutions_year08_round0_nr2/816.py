#include <iostream>
#include <vector>
#include <utility>
#include <cstdio>
#include <cassert>
#include <algorithm>
#include <queue>

using namespace std;

#define ISDIGIT(x) assert((x) >= '0' && (x) <= '9')
#define D(x) ((int) ((x) - '0'))

int convert(string s)
{
    assert(s.length() == 5);
    assert(s[2] == ':');
    ISDIGIT(s[0]);
    ISDIGIT(s[1]);
    ISDIGIT(s[3]);
    ISDIGIT(s[4]);

    return (D(s[0]) * 10 + D(s[1])) * 60
        + D(s[3]) * 10 + D(s[4]);
}

int main()
{
    int n;
    cin >> n;
    for (int c = 1; c <= n; c++)
    {
        int t, na, nb;
        cin >> t >> na >> nb >> ws;
        vector<int> la, lb, aa, ab;
        for (int i = 0; i < na; i++)
        {
            string start, end;
            cin >> start >> end;
            la.push_back(convert(start));
            ab.push_back(convert(end) + t);
        }
        for (int i = 0; i < nb; i++)
        {
            string start, end;
            cin >> start >> end;
            lb.push_back(convert(start));
            aa.push_back(convert(end) + t);
        }

        sort(la.begin(), la.end());
        sort(lb.begin(), lb.end());
        sort(aa.begin(), aa.end());
        sort(ab.begin(), ab.end());

        int numA = 0, numB = 0;
        unsigned int ia = 0, ib = 0;
        for (unsigned int i = 0; i < la.size(); i++)
        {
            if (ia < aa.size() && aa[ia] <= la[i])
            {
                // a train has arrived in time!
                ia++;
            }
            else
            {
                // no train waiting, we need another
                numA++;
            }
        }
        for (unsigned int i = 0; i < lb.size(); i++)
        {
            if (ib < ab.size() && ab[ib] <= lb[i])
            {
                // a train has arrived in time!
                ib++;
            }
            else
            {
                // no train waiting, we need another
                numB++;
            }
        }

        cout << "Case #" << c << ": " << numA << " " << numB << endl;
    }
    return 0;
}
