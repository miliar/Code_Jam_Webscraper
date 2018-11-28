# include <fstream>
# include <string>
# include <vector>
# include <math.h>
# include <algorithm>
# include <string.h>
# include <stack>
# include <queue>
# include <sstream>
# include <set>
# include <map>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    ifstream fin ("input.txt");
    ofstream fout ("output.txt");
    int t;
    fin >> t;
    for (int tt = 0; tt < t; tt++)
    {
        int time = 0;
        queue<pair<int, int> > o, b;
        int n;
        fin >> n;
        for (int i = 0; i < n; i++)
        {
            char ch;
            fin >> ch;
            int q;
            fin >> q;
            pair<int, int> temp = make_pair(q, i);
            if (ch == 'O')
               o.push(temp);
            else
                b.push(temp);
        }
        int posO = 1, posB = 1;
        int inf = 999999999;
        while (!o.empty() || !b.empty())
        {
            time++;
            int needO = inf, needB = inf;
            if (!o.empty())
               needO = o.front().first;
            if (!b.empty())
               needB = b.front().first;
            int prO = inf;
            int prB = inf;
            if (!o.empty())
               prO = o.front().second;
            if (!b.empty())
               prB = b.front().second;
            bool popO = false, popB = false;
            if (needO == posO && prO < prB)
               popO = true;
            if (needB == posB && prB < prO)
               popB = true;
            if (posO < needO)
               posO++;
            else
                if (posO > needO)
                   posO--;
            if (posB < needB)
               posB++;
            else
                if (posB > needB)
                   posB--;
            if (popO)
               o.pop();
            if (popB)
               b.pop();
        }
        fout << "Case #" << tt + 1 << ": " << time << endl;
    }
    //system("pause");
    return 0;
}
