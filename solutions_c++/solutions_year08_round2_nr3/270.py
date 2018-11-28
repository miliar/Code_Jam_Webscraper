#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int T, t, k, n, i, j, l;
int res[1000005];
vector<int> v;
vector<int>::iterator it, et;

int main()
{
    ifstream fin("in.txt");
    fin >> T;
    for(t = 1; t <= T; ++t)
    {
        fin >> k;
        v.clear();
        l = 0;
        for(i = 1; i <= k; ++i) v.push_back(i);
        for(i = 1; i <= k; ++i)
        {
            j = (l + i - 1) % static_cast<int>(v.size());
            et = v.end();
            for(it = v.begin(), l = 0; l < j; ++it, ++l);
            res[*it] = i;
            v.erase(it);
        }

        cout << "Case #" << t << ':';
        fin >> n;
        for(i = 0; i < n; ++i)
        {
            fin >> j;
            cout << ' ' << res[j];
        }
        cout << endl;
    }
    return 0;
}
