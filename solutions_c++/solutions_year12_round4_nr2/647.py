# include <fstream>
# include <iostream>
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
double dist(double a, double b, double c, double d)
{
       return sqrt((a - c) * (a - c) + (b - d) * (b - d));
}
int main()
{
    //ios_base::sync_with_stdio(false);
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");
    int t;
    cin >> t;
    int test = 0;
    while (t--)
    {
          test++;
          double mult = 1000;
          long long n;
          cin >> n;
          double a, b;
          cin >> a >> b;
          a *= mult;
          b *= mult;
          double eps = 1e-1;
          vector<pair<double, int> > r(n);
          for (long long i = 0; i < n; i++)
              cin >> r[i].first, r[i].first *= mult, r[i].second = i;
          sort(r.begin(), r.end());
          reverse(r.begin(), r.end());
          vector<pair<double, double> > f;
          f.push_back(make_pair(eps * mult, eps * mult));
          for (long long i = 1; i < n; i++)
          {
              srand(time(0));
              double q = abs((long long)(rand() << 45 + rand() * 100) % ((long long)a));
              double w = abs((long long)(rand() << 45 + rand() * 100) % ((long long)b));
              while (true)
              {
                    bool ok = true;
                    for (long long j = 0; j < f.size(); j++)
                        if (dist(q, w, f[j].first, f[j].second) < r[i].first + r[j].first + eps)
                           ok = false;
                    if (ok && !(q + eps > a || w + eps > b))
                    {
                           f.push_back(make_pair(q, w));
                           break;
                    }
                    else
                    {
                        q = abs((rand() << 45 + rand() * 100) % ((long long)a));
                        w = abs((rand() << 45 + rand() * 100) % ((long long)b));
                    }
              }
          }
          cout << "Case #" << test << ": ";
          cout.precision(5);
          vector<pair<double, double> > ans(n);
          for (int i = 0; i < n; i++)
              ans[r[i].second] = make_pair(f[i].first, f[i].second);
          for (long long i = 0; i < n; i++)
              cout << fixed << ans[i].first / mult << " " << ans[i].second / mult << " ";
              
          cout << endl;
    }
    //system("pause");
    return 0;
}
