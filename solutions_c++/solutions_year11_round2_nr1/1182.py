#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <utility>
#include <deque>
#include <iomanip>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for(int tt = 0; tt < T; tt++)
  {
    int N;
    cin >> N;
    char *table = new char[N*N];
    int *games = new int[N];
    int *wins = new int[N];
    double *wp = new double[N];
    double *owp = new double[N];
    double *oowp = new double[N];
    
    for(int i = 0; i < N; i++)
    {
      games[i] = 0;
      wins[i] = 0;
    }

    for(int i = 0; i < N; i++)
    {
      for(int j = 0; j < N; j++)
      {
        cin >> table[i*N + j];
        if(table[i*N + j] == '1')
        {
          games[i]++;
          wins[i]++;
        }
        else if(table[i*N + j] == '0')
        {
          games[i]++;
        }
      }
    }

    for(int i = 0; i < N; i++)
    {
      wp[i] = (double) wins[i] / (double) games[i];
    }
    
    for(int i = 0; i < N; i++)
    {
      int opponents_number = 0;
      owp[i] = 0.;
      for(int j = 0; j < N; j++)
      {
        if(table[i*N + j] == '1')
        {
          owp[i] += (double) wins[j] / (double) (games[j] - 1);
          opponents_number++;
        }
        else if(table[i*N + j] == '0')
        {
          owp[i] += (double) (wins[j] - 1) / (double) (games[j] - 1);
          opponents_number++;
        }
      }
      owp[i] /= opponents_number;
    }

    for(int i = 0; i < N; i++)
    {
      int opponents_number = 0;
      oowp[i] = 0;
      for(int j = 0; j < N; j++)
      {
        if(table[i*N + j] != '.')
        {
          oowp[i] += owp[j];
          opponents_number++;
        }
      }
      oowp[i] /= (double) opponents_number;
    }

    cout << "Case #" << (tt+1) << ":" << endl;
    cout << setprecision(10);
    for(int i = 0; i < N; i++)
    {
//      cout << games[i] << '\t' << wins[i] << '\t' << wp[i] << '\t' << owp[i] << '\t' << oowp[i] << endl;
      cout << 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << endl;
    }


    delete [] table;
    delete [] games;
    delete [] wins;
    delete [] wp;
    delete [] owp;
    delete [] oowp;
  }
  return 0;
}

