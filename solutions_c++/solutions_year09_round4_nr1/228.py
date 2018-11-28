#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <cstring>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)n; i++)
#define all(a) a.begin(), a.end()
#define fs first
#define sc second

typedef long long int64;


int t, n, ans;
vector<int> a[50];
vector<bool> u[50];
char ch;

void swp(vector<int> &a, vector<int> &b)
{
  vector<int> c;
  c = a;
  a = b;
  b = c;
}

void swp(vector<bool> &a, vector<bool> &b)
{
  vector<bool> c;
  c = a;
  a = b;
  b = c;
}


int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  scanf("%d", &t);

  forn(i, 50)
    a[i].resize(50);
  forn(i, 50)
    u[i].resize(50);

  forn(w, t)
    {
      ans = 0;
      
      scanf("%d", &n);
      
      forn(i, n)
        forn(j, n)
          u[i][j] = false;
      
      forn(i, n)
        {
          scanf("\n");
          forn(j, n)
            {
              scanf("%c", &ch);
              a[i][j] = ch - '0';
            }
        }

      forn(i, n)
        for(int j = n-1; j >= 0; j--)
          {
            u[i][j] = true;
            if (a[i][j] == 1)
              break;
          }

      forn(k, n)
        {
          for(int i = k; i < n; i++)
            if (u[i][k])
              {
                for(int j = i; j > k; j--)
                  {
                    ans++;
                    swp(a[j], a[j-1]);
                    swp(u[j], u[j-1]);
                  }
                break;
              }
        }

      printf("Case #%d: %d\n", w+1, ans);
    }
}
