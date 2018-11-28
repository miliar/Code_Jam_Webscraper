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

long long maxi[200000];

int main()
{
    //ios_base::sync_with_stdio(false);
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");
    long long t;
    cin >> t;
    long long test = 0;
    while (t--)
    {
          test++;
          long long n;
          cin >> n;
          vector<pair<long long, long long> > a(n);
          for (long long i = 0; i < n; i++)
              cin >> a[i].first >> a[i].second;
              
          long long d;
          cin >> d;
          
          memset(maxi, 0, sizeof(maxi));
          
          maxi[0] = a[0].first;
          for (long long i = 0; i < n; i++)
          {
              for (long long j = i + 1; j < n; j++)
                  if (a[i].first + maxi[i] >= a[j].first)
                     maxi[j] = max(maxi[j], min(a[j].first - a[i].first, a[j].second));
          }
          
          bool ok = false;
          
          for (long long i = 0; i < n; i++)
              if (a[i].first + maxi[i] >= d)
                 ok = true;
          cout << "Case #" << test << ": ";
          if (ok)
             cout << "YES";
          else
              cout << "NO";
          cout << endl;
          
    }
    //system("pause");
    return 0;
}
