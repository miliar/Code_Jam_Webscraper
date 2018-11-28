#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <list>

using namespace std;

struct stats
{
  set<int> beat;
  set<int> lost;
  double wp, owp, oowp;
};

struct stats stats[100];

bool has(set<int> &s, int i)
{
  return s.find(i)!=s.end();
}

int main()
{
  int _T;
  cin >> _T;

  int N;
  cout.precision(20);
  for (int _t=1; _t<=_T; _t++)
    {
      cout << "Case #" << _t << ": ";

      cin >> N;
      for (int i=0; i<N; i++)
        {
          stats[i].beat.clear();
          stats[i].lost.clear();
          string l;
          cin >> l;
          for (int j=0; j<N; j++)
            {
              if (l[j]=='1')
                {
                  stats[i].beat.insert(j);
                }
              else if (l[j]=='0')
                {
                  stats[i].lost.insert(j);
                }
            }
          stats[i].wp = (double)stats[i].beat.size()/((double)stats[i].beat.size()+stats[i].lost.size());
          //          cout << stats[i].wp << endl;
        }

      for (int i=0; i<N; i++)
        {
          stats[i].owp=0;
          for (int j=0; j<N; j++)
            {
              if (has(stats[i].beat,j))
                stats[i].owp += (double)stats[j].beat.size()/((double)stats[j].beat.size()+stats[j].lost.size()-1);
              else if (has(stats[i].lost,j))
                stats[i].owp += ((double)stats[j].beat.size()-1)/((double)stats[j].beat.size()+stats[j].lost.size()-1);
            }
          stats[i].owp /= (double)stats[i].beat.size()+stats[i].lost.size();
          //         cout << stats[i].owp << endl;
        }

      for (int i=0; i<N; i++)
        {
          stats[i].oowp=0;
          for (int j=0; j<N; j++)
            {
              if (has(stats[i].beat,j))
                stats[i].oowp += stats[j].owp;
              else if (has(stats[i].lost,j))
                stats[i].oowp += stats[j].owp;
            }
          stats[i].oowp /= (double)stats[i].beat.size()+stats[i].lost.size();
          //cout << stats[i].oowp << endl;

                cout << endl << 0.25 * stats[i].wp + 0.50 * stats[i].owp + 0.25 * stats[i].oowp;
        }
      cout << endl;
    }

  return 0;
}
