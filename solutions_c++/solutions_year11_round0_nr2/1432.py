#include <iostream>
#include <vector>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <string>

using namespace std;

int trans[30][30];
bool op[30][30];

int main(void)
{

  int T;
  cin >> T;
  for(int c = 1; c <= T; c++)
  {
    int C, D, N;
    memset(trans, -1, sizeof(trans));
    memset(op, 0, sizeof(op));
    cin >> C;
    for(int i = 0; i < C; i++){
      string s;
      cin >> s;
      int x = s[0] - 'A';
      int y = s[1] - 'A';
      trans[x][y] = trans[y][x] = s[2];      
    }
    cin >> D;
    for(int i = 0; i < D; i++)
    {
      string s;
      cin >> s;
      int x = s[0] - 'A';
      int y = s[1] - 'A';
      op[x][y] = op[y][x] = true;
    }
    cin >> N;
    string s;
    cin >> s;
    string res;
    res.push_back(s[0]);
    for(int i = 1; i < N; i++)
    {
      int sz = res.size();
      int tr;       
      if(sz > 0 && (tr = trans[res[sz-1]-'A'][s[i]-'A']) != -1)
      {
        res[sz-1] = (char)tr;
      }
      else
      {
        if(res.size() == 0) res.push_back(s[i]);
        else
        {
          for(int j = 0; j < sz; j++)
          {
            if(op[res[j]-'A'][s[i]-'A'])
            {
              res.clear();
              break;
            }
          }
          if(res.size() > 0) res.push_back(s[i]);
        }
      }
    }
    if(res.size() == 0)
    printf("Case #%d: [",c);
    else
    printf("Case #%d: [%c",c,res[0]);

    for(int i = 1; i < res.size(); i++)
    {
      printf(", %c",res[i]);
    }
    printf("]\n");
  }
  return 0;

}
