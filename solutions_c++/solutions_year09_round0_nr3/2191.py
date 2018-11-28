#include <iostream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)n; i++)

const int N = 1000;
const int M = 25;
const int K = 10000;

char buf[N];
string s, t;
int w, n, m;

int T[N][M];

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  scanf("%d", &w);
  
  t = "welcome to code jam";
  
  forn(x, w)
    {
      scanf("\n");
      gets(buf);
      s = buf;

      n = s.length();
      m = t.length();

      memset(T, 0, sizeof(T));
      
      for(int i = 0; i <= n; i++)
        T[i][0] = 1;

      for(int i = 1; i <= n; i++)
        for(int j = 1; j <= m; j++)
          {
            T[i][j] = T[i-1][j];
            if (s[i-1] == t[j-1])
              T[i][j] = (T[i][j] + T[i-1][j-1]) % K;
          }

       printf("Case #%d: %04d\n", x+1, T[n][m]);
    }
}
