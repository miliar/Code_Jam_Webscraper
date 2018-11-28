#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>

using namespace std;

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("in", "rt", stdin);
        freopen("out", "wt", stdout);
    #endif
    int n, t;
    cin >> t;
    for (int curTest = 1; curTest <= t; ++curTest)
    {
        cin >> n;
        vector<int> o, b, idi, idj;
        for (int i = 0; i < n; ++i)
        {
            char r;
            int id;
            cin >> r >> id;
            if (r == 'O')
            {
                o.push_back(id);
                idi.push_back(i);
            }
            else
            {
                b.push_back(id);
                idj.push_back(i);
            }
        }
        idi.push_back(n);
        idj.push_back(n);
        int time = 0;
        int i = 0, j = 0, posi = 1, posj = 1;
        while (i + j < (int)o.size() + (int)b.size())
        {
            ++time;
            bool iDone = false;
            bool jDone = false;
            if (i < o.size() && posi == o[i] && idi[i] < idj[j])
            {
                ++i;
                iDone = true;
            }
            else if (j < b.size() && posj == b[j] && idj[j] < idi[i])
            {
                ++j;
                jDone = true;
            }
            if (!iDone && i < o.size() && posi != o[i])
                posi += posi < o[i] ? 1 : -1;
            if (!jDone && j < b.size() && posj != b[j])
                posj += posj < b[j] ? 1 : -1;    
        }
        printf("Case #%d: %d\n", curTest, time);
    }
    return 0;
}
