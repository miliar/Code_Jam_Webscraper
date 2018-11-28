#include <iostream>
#include <vector>
using namespace std;

int main()
{
  int T;
  cin>>T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #"<<t<<":"<<endl;
    int R, C;
    cin>>R;
    cin>>C;
    char** a = new char*[R];
    for (int j = 0; j < R; j++)
    {
      a[j]=new char[C];
      for (int k = 0; k < C; k++)
      {
        cin >> a[j][k];
      }
    }
    bool impossible = false;
    for (int j = 0; j < R; j++)
    {
      int sum = 0;
      for (int k = 0; k < C; k++)
      {
        if(a[j][k] == '#') sum++;
      }
      if (sum % 2 != 0)
      {
        impossible = true;
        break;
      }
    }
    if (impossible)
    {
      cout << "Impossible" << endl;
      continue;
    }
    for (int j = 0; j < C; j++)
    {
      int sum = 0;
      for (int k = 0; k < R; k++)
      {
        if(a[k][j] == '#') sum++;
      }
      if (sum % 2 != 0)
      {
        impossible = true;
        break;
      }
    }
    if (impossible)
    {
      cout << "Impossible" << endl;
      continue;
    }
    for (int j = 0; j < R; j++)
    {
      if (impossible) break;
      for (int k = 0; k < C; k++)
      {
        if (impossible) break;
        if (a[j][k] == '#')
        {
          if (j+1 >= R || k+1 >= C) 
          {
            cout << "Impossible" << endl;
            impossible = true;
          }else
          {
            if (a[j+1][k] == '#' && a[j][k+1] == '#' && a[j+1][k+1] == '#')
            {
              a[j][k] = '/';
              a[j+1][k] = '\\';
              a[j][k+1] = '\\';
              a[j+1][k+1] = '/';
            }
            else
            {
              cout << "Impossible" << endl;
              impossible = true;
            }
          }
        }
      }
    }
    if (impossible) continue;

    for (int j = 0; j < R; j++)
    {
      for (int k = 0; k < C; k++)
      {
        cout << a[j][k];
      }
      cout<<endl;
    }
           
    cout.precision(7);
    /*for (int j = 0; j < N; j++)
    {
    cout << (0.25)<<endl;
    }*/
  }

  return 0;
}