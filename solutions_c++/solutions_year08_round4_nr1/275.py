#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <vector>
#include <algorithm>

using namespace std;

#define PI 3.1415926535897932384626433832795
#define INF (int)1e9
#define EPS 1e-9

#define SQR(a) ((a)*(a))

#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define SORT(a) sort(a.begin(), a.end())
#define CLEAR(a) a.clear()
#define FILL(a) memset(a, 0, sizeof(a))
#define SIZE(a) (int)a.size()
#define LEN(a) (int)a.length()
#define SUBSTR(i,j) substr(i,j-i+1)
#define PB push_back
#define MP make_pair
#define VI vector<int>
#define VS vector<string>

stringstream foo("");
string buf;

#define READ getline(cin, buf), foo.clear(), foo.str(buf)

#define N 20000

int n, v;
int gate[N], change[N];
int value[N];
int s;
int t[N][2];
bool mark[N][2];

int tests;

int calc( int i, int r )
{
  if (i >= s)
  {
    if (r == value[i])
      return 0;
    else
      return INF;
  }
  if (mark[i][r])
    return t[i][r];
  
  mark[i][r] = true;
  t[i][r] = INF;

    // AND gate
    if (gate[i] == 1)
    {
      if (r == 1)
      {
        t[i][r] = min(t[i][r], calc(i * 2, 1) + calc(i * 2 + 1, 1));
      }
      else
      {
        t[i][r] = min(t[i][r], calc(i * 2, 0) + calc(i * 2 + 1, 1));
        t[i][r] = min(t[i][r], calc(i * 2, 1) + calc(i * 2 + 1, 0));
        t[i][r] = min(t[i][r], calc(i * 2, 0) + calc(i * 2 + 1, 0));                
      }
    }    
    // OR gate 
    if (gate[i] == 0)
    {
      if (r == 1)
      {
        t[i][r] = min(t[i][r], calc(i * 2, 0) + calc(i * 2 + 1, 1));
        t[i][r] = min(t[i][r], calc(i * 2, 1) + calc(i * 2 + 1, 0));
        t[i][r] = min(t[i][r], calc(i * 2, 1) + calc(i * 2 + 1, 1));          
      }
      else
      {
        t[i][r] = min(t[i][r], calc(i * 2, 0) + calc(i * 2 + 1, 0));
      }
    }

  if (!change[i])
    return t[i][r];

    // ANG gate
    if (gate[i] == 1)
    {
      if (r == 1)
      {
        t[i][r] = min(t[i][r], calc(i * 2, 0) + calc(i * 2 + 1, 1) + 1);
        t[i][r] = min(t[i][r], calc(i * 2, 1) + calc(i * 2 + 1, 0) + 1);
        t[i][r] = min(t[i][r], calc(i * 2, 1) + calc(i * 2 + 1, 1) + 1);          
      }
      else
      {
        t[i][r] = min(t[i][r], calc(i * 2, 0) + calc(i * 2 + 1, 0) + 1);
      } 
    }
    // OR gate
    if (gate[i] == 0)
    {
      if (r == 1)
      {
        t[i][r] = min(t[i][r], calc(i * 2, 1) + calc(i * 2 + 1, 1) + 1);
      }
      else
      {
        t[i][r] = min(t[i][r], calc(i * 2, 0) + calc(i * 2 + 1, 1) + 1);
        t[i][r] = min(t[i][r], calc(i * 2, 1) + calc(i * 2 + 1, 0) + 1);
        t[i][r] = min(t[i][r], calc(i * 2, 0) + calc(i * 2 + 1, 0) + 1);                
      }      
    }
  
  return t[i][r];
}

int main()
{
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);
  
  READ;
  foo >> tests;
  FOR(test,1,tests)
  {
    scanf("%i%i", &n, &v);
    FOR(i,1,(n-1)/2)
      scanf("%i%i", &gate[i], &change[i]);
    FOR(i,(n-1)/2+1,n)
      scanf("%i", &value[i]);
    s = (n-1)/2 + 1;    
    FILL(mark);
    int res = calc(1, v);
    cout << "Case #" << test << ": ";
    if (res >= INF)
      printf("IMPOSSIBLE\n");
    else
      printf("%i\n", res);
  }

  return 0;
}
