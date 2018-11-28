#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

int main()
{
  cout << setprecision(10);
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++)
  {
    int N;
    cin >> N;
    int tab[N][N];
    for(int i = 0; i < N; i++)
    {
      for(int j = 0; j < N; j++)
      {
        tab[i][j] = -1;
      }
    }
    for(int i = 0; i < N; i++)
    {
      for(int j = 0; j < N; j++)
      {
        char g;
        cin >> g;
        if(g == '0')
        {
          tab[i][j] = 0;
        }
        else if(g == '1')
        {
          tab[i][j] = 1;
        }
      }
    }
    double wp[N];
    double owp[N];
    double oowp[N];
    for(int i = 0; i < N; i++)
    {
      wp[i] = 0;
      owp[i] = 0;
      oowp[i] = 0;
    }

    for(int i = 0; i < N; i++)
    {
      int played = 0;
      int won = 0;
      for(int j = 0; j < N; j++)
      {
        if(tab[i][j] >= 0)
        {
          played++;
        }
        if(tab[i][j] > 0)
        {
          won++;
        }
      }
      wp[i] = static_cast<double>(won) / static_cast<double>(played);
    }

    for(int team = 0; team < N; team++)
    {
      double wp_[N];
      for(int i = 0; i < N; i++)
      {
        int played = 0;
        int won = 0;
        for(int j = 0; j < N; j++)
        {
          if(j == team)
          {
            continue;
          }
          if(tab[i][j] >= 0)
          {
            played++;
          }
          if(tab[i][j] > 0)
          {
            won++;
          }
        }
        wp_[i] = static_cast<double>(won) / static_cast<double>(played);
      }

      double sum_wp = 0;
      int played = 0;
      for(int i = 0; i < N; i++)
      {
        if(tab[team][i] >= 0)
        {
          sum_wp += wp_[i];
          played++;
        }
      }
      owp[team] = sum_wp / static_cast<double>(played);
    }

    for(int i = 0; i < N; i++)
    {
      double sum_owp = 0;
      int played = 0;
      for(int j = 0; j < N; j++)
      {
        if(tab[i][j] >= 0)
        {
          sum_owp += owp[j];
          played++;
        }
      }
      oowp[i] = sum_owp / static_cast<double>(played);
    }

    cout << "Case #" << t << ":" << endl;
    double rpi[N];
    for(int i = 0; i < N; i++)
    {
      rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
      cout << rpi[i] << endl;
    }
  }
}

