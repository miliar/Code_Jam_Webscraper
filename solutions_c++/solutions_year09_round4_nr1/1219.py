#include <iostream>
#include <queue>
#include <vector>
#include <map>

using namespace std;

struct state
{
  int a, d;
  state() {}
  state(int _a, int _d)
  { a = _a; d = _d; }
};

struct comp
{
  bool operator () (const state &a,const state &b) const
  { return a.d > b.d || (a.d == b.d && a.a > b.a); }
};

int n;
char t[16];
int A[16];
queue < state> q;
bool minD[8*8*8*8*8*8*8*8*8];

int GenNumber(vector<int> help)
{
  int res = 0;
  for (int i = n - 1; i >= 0; i--)
    res = res * 8 + help[i];
  return res;
}

void TryToPush(int a, int dist)
{
  if ((minD[a] == 0)) { minD[a] = 1; q.push(state(a, dist)); }
}

int Solve()
{
  memset(minD, 0, sizeof(minD));
  q = queue < state> ();
  
  scanf("%d", &n);
  for (int i = 0; i < n; i++)
    {
      A[i] = 0;
      scanf("%s", &t);
      for (int j = n - 1; j >= 0; j--)
        A[i] = A[i] * 2 + (t[j] - '0');
    }
  vector<int> help;
  for(int i = 0; i < n; i++) help.push_back(i);
  int tmp = GenNumber(help);
  int dist;

  TryToPush(tmp, 0);
  while (!q.empty())
  {
    tmp = (q.front()).a; dist = (q.front()).d; q.pop();
        
    help.clear();
    for (int i = 0; i < n; i++) 
      {
        help.push_back(tmp % 8);
        tmp /= 8;
      }

    bool answ = 1;
    for (int i = 0; i < n && answ; i++)
      for (int j = i + 1; j < n && answ; j++)
        if ((A[help[i]] & (1 << j))) {  answ = 0; }
    
    if (answ) return dist;
    
    for(int i = 0 ;i < (n - 1); i++)
      {
        swap(help[i], help[i + 1]);
        TryToPush(GenNumber(help), dist + 1);
        swap(help[i], help[i + 1]);
      }
  }
}

int main()
{
  int tests;
  scanf("%d", &tests);
  for (int i = 1; i <= tests; i ++)
    {
      int res = Solve();
      printf("Case #%d: %d\n", i, res);
    }
  
  //system("pause");
  return 0;
}
