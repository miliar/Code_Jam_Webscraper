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
        int n;
        fin >> n;
        vector<string> a(n);
        int ch[105][105];
        memset(ch, -1, sizeof(ch));
        for (int i = 0; i < n; i++)
        {
            fin >> a[i];
            for (int j = 0; j < n; j++)
                if (a[i][j] != '.')
                   ch[i][j] = a[i][j] - '0';
        }
        double ans = 0;
        vector<double> wp(n);
        for (int i = 0; i < n; i++)
        {
            int c = 0, d = 0;
            for (int j = 0; j < n; j++)
            {
                if (a[i][j] == '1')
                   c++;
                if (a[i][j] != '.')
                   d++;
            }
            if (d != 0)
               wp[i] = (double)c / (double)d;
            else
                wp[i] = 0;
        }
        vector<double> owp(n);
        for (int i = 0; i < n; i++)
        {
            int count = 0;
            double sum = 0;
            for (int j = 0; j < n; j++)
            {
                if (a[i][j] == '.')
                   continue;
                int op = j;
                int c = 0, d = 0;
                for (int we = 0; we < n; we++)
                {
                    if (a[op][we] == '.')
                       continue;
                    if (we == i)
                       continue;
                    if (a[op][we] == '1')
                       c++;
                    d++;
                }
                if (d != 0)
                   sum += (double)c / (double)d;
                count++;
            }
            sum /= (double)count;
            owp[i] = sum;
        }
        vector<double> oowp(n);
        for (int i = 0; i < n; i++)
        {
            int count = 0;
            double sum = 0;
            for (int j = 0; j < n; j++)
            {
                if (a[i][j] == '.')
                   continue;
                count++;
                sum += owp[j];
            }
            sum /= (double)count;
            oowp[i] = sum;
        }
        fout << "Case #" << 1 + tt << ":\n";
        for (int i = 0; i < n; i++)
        {
            double ans = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
            fout.precision(7);
            fout << fixed << ans << endl;
        }
    }
    //system("pause");
    return 0;
}
