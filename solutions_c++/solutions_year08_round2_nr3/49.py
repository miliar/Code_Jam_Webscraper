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

int tests;

#define N 2000000

int n, m;
int t[N];
int a[N];
int ind[N];

void update( int i )
{
  while (i < n)
  {
    t[i]++;
    i = i | (i + 1);
  }
}
int get( int i )
{
  int res = 0;
  while (i >= 0)
  {
    res += t[i];
    i = (i & (i + 1)) - 1;
  }
  return res;
}
int rsq( int i, int j )
{
  return get(j) - get(i - 1);
}
int empty( int i, int j )
{
  if (i > j)
    return 0;
  return j - i + 1 - rsq(i, j);
}

int bin_search( int l, int r, int q, int key )
{  
  int start = l;
  int p = -1;
  while (l <= r)
  {
    //printf("(%i, %i)\n", l, r);
    int mid = (l + r) / 2;
    //printf("check %i\n", mid);
    int e = empty(start, mid);
    //printf("empty on int [%i, %i] = %i\n", start, mid, empty(start, mid));
    if (e >= q && a[mid] == 0)
    {
      p = mid;
      //printf("(%i, %i)\n", l, r);      
    }
    if (e >= q)
      r = mid - 1;
    else
      l = mid + 1;
    //printf("(%i, %i)\n", l, r);
  }
  a[p] = key;
  update(p);
  //printf("put %i on pos %i\n", key, p);
  return p;
}
int put_card( int key, int start )
{
 
  int e = empty(start + 1, n - 1);
  int q = key;
  //printf("try to put %i from pos %i in place %i\n", key, start, q);
  if (e >= q)
    return bin_search(start + 1, n - 1, q, key );
  else
  {
    q -= e;
    start = 0;
    int all = empty(0, n - 1);
    q %= all;    
    if (q == 0)
      q = all;
    //printf("try to put %i from pos %i in place %i\n", key, start, q);       
    return bin_search(0, n - 1, q, key);
  }
}

int main()
{
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);
  
  READ;
  foo >> tests;
  FOR(test,1,tests)
  {
    scanf("%i%i", &n, &m);
    FOR(i,0,m-1)
      scanf("%i", &ind[i]);
    FILL(t);
    FILL(a);
    a[0] = 1;
    update(0);
    int prev = 0;
    FOR(i,2,n)
    {
      int _prev = put_card(i, prev);
      prev = _prev;
    }
    /*FOR(i,0,n-1)
      printf("%i ", a[i]);
    printf("\n");*/
      
    cout << "Case #" << test << ":";
    FOR(i,0,m-1)
      printf(" %i", a[ind[i] - 1]);
    printf("\n");
  }

  return 0;
}
