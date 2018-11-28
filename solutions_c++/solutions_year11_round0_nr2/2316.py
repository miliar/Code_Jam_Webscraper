#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

int t, n, c;
char s[200], nw;
bool op[256][256];
char com[256][256];
vector<char> out;

int main()
{
  scanf("%d", &t);
  for (int i = 0; i < t; i++)
  {
    memset(com, 0, sizeof(com));
    memset(op, false, sizeof(op));
    out.clear();
    scanf("%d", &c);
    for (int j = 0; j < c; j++)
    {
      scanf("%s", s);
      com[s[0]][s[1]] = com[s[1]][s[0]] = s[2];
    }
    scanf("%d", &c);
    for (int j = 0; j < c; j++)
    {
      scanf("%s", s);
      op[s[0]][s[1]] = op[s[1]][s[0]] = true;
    }
    scanf("%d %s", &n, s);
    for (int j = 0; j < n; j++)
    {
      if (out.size() && (nw = com[out[out.size()-1]][s[j]]))
      {
        out.pop_back();
        out.push_back(nw);
      }
      else 
      {
        bool good = true;
        for (int k = 0; k < out.size(); k++)
          if (op[out[k]][s[j]])
            good = false;
        if (good) out.push_back(s[j]);
        else out.clear();
      }
    }
    printf("Case #%d: [", i + 1);
    for (int j = 0; j < out.size(); j++)
    {
      if (j) printf(", ");
      printf("%c", out[j]);
    }
    printf("]\n");
  }
  return 0;
}
