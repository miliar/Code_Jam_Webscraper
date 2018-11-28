#include <iostream>
#include <string>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)n; i++)

int t, l, n, k;
char c;
long double w[10000];
string s[10000];
string p[10000];
string tmp;

long double ans;


void read(int v, bool need)
{
  if (need)
    {
      scanf("\n");
      scanf("%c", &c);
    }

  cin >> w[v];

  scanf("\n");
  scanf("%c", &c);

  s[v] = "";

  while (c != ')' && c != '(')
    {
      s[v] = s[v] + c;
      scanf("\n");
      scanf("%c", &c);
    }


  if (s[v] == "")
    return;

  if (c == '(')
    read(2*v, false);
   else
    read(2*v, true);

  read(2*v+1, true);

  scanf("\n");
  scanf("%c", &c);
}


void go(int v)
{
  ans *= w[v];
  
  if (s[v] == "")
    return;

  forn(i, k)
    if (p[i] == s[v])
      {
        go(2*v);
        return;
      }
  
  go(2*v+1);
}


int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  scanf("%d", &t);


  forn(tt, t)
  {
    printf("Case #%d:\n", tt+1);
    
    scanf("%d", &l);
    scanf("\n");

    read(1, true);

    scanf("%d", &n);
    forn(i, n)
      {
        cin >> tmp >> k;

        forn(j, k)
          cin >> p[j];

        ans = 1.0;
        go(1);

        printf("%.7lf\n", (double)ans);
      }
  }

}
    
