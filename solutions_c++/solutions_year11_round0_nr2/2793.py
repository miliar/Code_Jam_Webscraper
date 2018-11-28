#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <fstream>
using namespace std;

int main()
{
  int T, c, d, n, l, fa[30][30];
  bool flag, fb[30][30];
  char q[110];
  string s;
  ifstream cin("d.txt");
  FILE *fout = fopen("dd.txt", "w");
  
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cin >> c;
    memset(fa, -1, sizeof(fa));
    for (int i = 0; i < c; i++)
    {
      cin >> s;
      fa[s[0] - 'A'][s[1] - 'A'] = fa[s[1] - 'A'][s[0] - 'A'] = s[2] - 'A';
    }
    
    cin >> d;
    memset(fb, false, sizeof(fb));
    for (int i = 0; i < d; i++)
    {
      cin >> s;
      fb[s[0] - 'A'][s[1] - 'A'] = fb[s[1] - 'A'][s[0] - 'A'] = true;
    }
    
    cin >> n >> s;
    l = 0;
    for (int i = 0; i < n; i++)
    {
      if (l > 0 && fa[s[i] - 'A'][q[l - 1] - 'A'] != -1)
      {q[l - 1] = fa[s[i] - 'A'][q[l - 1] - 'A'] + 'A'; continue;}
      
      flag = false;
      for (int j = 0; j < l && !flag; j++)
        if (fb[s[i] - 'A'][q[j] - 'A']) {l = 0; flag = true;}
      
      if (!flag) q[l++] = s[i];
    }
    
    fprintf(fout, "Case #%d: [", t);
    for (int i = 0; i < l; i++)
      if (i == 0) fprintf(fout, "%c", q[i]);
      else fprintf(fout, ", %c", q[i]);
    fprintf(fout, "]\n");
  }
  
  fclose(fout);
  return 0;
}
