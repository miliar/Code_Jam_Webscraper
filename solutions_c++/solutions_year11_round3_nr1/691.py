#include <iostream>

using namespace std;

void solve()
{
     int N, M;
     cin >> N >> M;
     char R[50][50];
     
     for (int i = 0; i < N; i++) 
      for (int j = 0; j < M; j++) 
       cin >> R[i][j];
     
     bool flag = 0;
     for (int i = 0; i < N; i++)
      for (int j = 0; j < M; j++)
      {
          if (R[i][j] == '#')
          {
               if (i == N-1 || R[i+1][j] == '.' || j == M-1 || R[i][j+1] == '.' || R[i+1][j+1] == '.')
               {
                     flag = 1;
                     break;
               }
               else
               {
                   R[i][j] = R[i+1][j+1] = '/';
                   R[i][j+1] = R[i+1][j] = '\\';
               }
          }
      }
     
     if (flag)
     {
          cout << "Impossible" << endl;
     }
     else
      for (int i = 0; i < N; i++) 
      {  
          for (int j = 0; j < M; j++) 
           cout <<  R[i][j];
          cout << endl;
      }
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        cout << "Case #" << i + 1 << ":" << endl;
        solve();
    }
}
