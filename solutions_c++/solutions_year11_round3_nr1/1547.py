#include<iostream>
#include<string.h>
using namespace std;

const int MAXN = 128;

int r,c,t;
char m[MAXN][MAXN];

bool solve()
{
     for(int i = 0; i < r; i++)
      for(int j = 0; j < c; j++)
      {
              if(m[i][j] == '#' && m[i][j + 1] == '#' && m[i + 1][j] == '#' && m[i + 1][j + 1] == '#')
              {
                         m[i][j] = '/';
                         m[i][j + 1] = '\\';
                         m[i + 1][j] = '\\';
                         m[i + 1][j + 1] = '/';
              }
      }
     
     for(int i = 0; i < r; i++)
      for(int j = 0; j < c; j++)
       if(m[i][j] == '#')
        return 0;
     
     return 1;   
} 

int main()
{
    cin >> t;
    int test = 0;
    while(test < t)
    {
               memset(m, 0, sizeof(m));
               
               test++;
               cin >> r >> c;
               
               for(int i = 0; i < r; i++)
                for(int j = 0; j < c; j++)
                 cin >> m[i][j];
               
               cout << "Case #" << test << ":" << endl;
               if(solve() == 0)
                cout << "Impossible" << endl;
               else 
                for(int i = 0; i < r; i++)
                {
                        for(int j = 0; j < c; j++)
                         cout << m[i][j];
                        cout << endl;
                }  
    }
    return 0;
}
