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
bool ok(vector<string> a)
{
     bool ret = true;
     for (int i = 0; i < a.size(); i++)
         for (int j = 0; j < a[0].length(); j++)
             if (a[i][j] == '#')
                ret = false;
     return ret;
}
vector<string> go(vector<string> a)
{
               int n = a.size();
               int m = a[0].length();
               for (int i = 0; i < n - 1; i++)
                   for (int j = 0; j < m - 1; j++)
                   {
                       if (a[i][j] == '#' && a[i][j + 1] == '#' && a[i + 1][j] == '#' && a[i + 1][j + 1] == '#')
                       {
                                   a[i][j] = '/';
                                   a[i][j + 1] = '\\';
                                   a[i + 1][j] = '\\';
                                   a[i + 1][j + 1] = '/';
                                   return a;
                       }
                   }
               return a;
}
int main()
{
    ios_base::sync_with_stdio(false);
    ifstream fin ("input.txt");
    ofstream fout ("output.txt");
    int t;
    fin >> t;
    for (int tt =0 ; tt < t; tt++)
    {
        int n, m;
        fin >> n >> m;
        vector<string> a(n);
        for (int i = 0; i < n; i++)
            fin >> a[i];
        bool oki = true;
        while (!ok(a))
        {
              vector<string> b = a;
              a = go(a);
              if (a == b)
              {
                    oki = false;
                    break;
              }
        }
        fout << "Case #" << 1 + tt << ":" << endl;
        if (oki)
           for (int i = 0; i < n; i++)
               fout << a[i] << endl;
        else
            fout << "Impossible" << endl;
    }
    //system("pause");
    return 0;
}
