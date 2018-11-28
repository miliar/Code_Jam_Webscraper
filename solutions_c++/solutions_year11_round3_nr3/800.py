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
    for (int tt =0 ; tt < t; tt++)
    {
        int n, l, r;
        fin >> n >> l >> r;
        vector<int> a(n);
        for (int i = 0; i < n; i++)
            fin >> a[i];
        int ans = 0;
        for (int i = l; i <= r; i++)
        {
            bool ok = true;
            for (int j = 0; j < n; j++)
                if (!(a[j] % i == 0 || i % a[j] == 0))
                   ok = false;
            if (ok && ans == 0)
            {
               ans = i;
               break;
            }
        }
        fout << "Case #" << 1 + tt << ": ";
        if (ans == 0)
           fout << "NO";
        else
            fout << ans;
        fout << endl;
    }
    //system("pause");
    return 0;
}
