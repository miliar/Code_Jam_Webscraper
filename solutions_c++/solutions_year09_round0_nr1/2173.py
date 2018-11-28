#include <iostream>

using namespace std;               

#define forn(i, n) for(int i = 0; i < (int)n; i++)

const int N = 6000;
const int M = 600;
const int K = 256;

char buf[N];
string s[N], t;
int l, n, m;
int use[K];
bool ok[N];


int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  scanf("%d%d%d", &l, &n, &m);

  forn(i, n)
    {
      scanf("\n");
      gets(buf);
      s[i] = buf;
    }

  forn(x, m)
    {
      scanf("\n");
      gets(buf);
      t = buf;

      int cur = 0;

      memset(use, 255, sizeof(use));
      memset(ok, 1, sizeof(ok));

      for(int i = 0; i < l; i++)
        {
          if (t[cur] == '(')
            {
              cur++;
              while (t[cur] != ')')
                {
                  use[ t[cur] ] = i;
                  cur++;
                }
            }
           else
            use[ t[cur] ] = i;
          
          cur++;


          forn(j, n)
            ok[j] = ok[j] && (use[ s[j][i] ] == i);
        }

      int ans = 0;
      forn(i, n)
        ans += (int)ok[i];

      printf("Case #%d: %d\n", x+1, ans);
    }
}
