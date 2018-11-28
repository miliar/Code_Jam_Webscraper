#include<iostream>
#include<vector>
#include<string>

using namespace std;

const int MAX_D = 5 * 1000;
const int MAX_L = 15;

int L, D;
string dico[MAX_D];

inline bool match(vector<int> &mask, int d)
{
  for(int l = 0; l < L; l++)
    if(((mask[l] >> (dico[d][l]-97)) & 1) == 0)
      return 0;
  return 1;
}

int main()
{
  int T;
  cin >> L >> D >> T;
  for(int d = 0; d < D; d++)
    cin >> dico[d];
  for(int t = 1; t <= T; t++)
    {
      string s;
      cin >> s;
      vector<int> mask(L);
      int pos_cur = 0;
      for(int l = 0; l < L; l++)
        {
          if(s[pos_cur] != '(')
            mask[l] = 1 << (s[pos_cur++]-97);
          else
            {
              for(pos_cur++; s[pos_cur] != ')'; pos_cur++)
                mask[l] |= 1 << (s[pos_cur]-97);
              pos_cur++;
            }
        }
      int r = 0;
      for(int d = 0; d < D; d++)
        r += match(mask, d);
      cout << "Case #" << t << ": " << r << "\n";
    }
}
