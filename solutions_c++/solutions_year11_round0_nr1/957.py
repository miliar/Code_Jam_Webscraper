#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <bitset>
#include <set>
#include <deque>

using namespace std;
#define AUTO(a, b) typeof(b) a = (b)

typedef unsigned long long ull;
typedef unsigned uint;

pair<int,int> v[101];
int n;
uint  dp  [101][101][101];
bool  inq [101][101][101];

struct state {
  int i, a, b;
};

template<typename Work>
void add(state const& q, int nt, Work& work)
{
  if( q.a < 0 || q.a >= 100 || q.b < 0 || q.b >= 100 )
    return;
  if( nt < dp[q.i][q.a][q.b] )
  {
    dp[q.i][q.a][q.b] = nt;
    if( !inq[q.i][q.a][q.b] )
    {
      inq[q.i][q.a][q.b] = true;
      work.push_back(q);
    }
  }
}
int solve()
{
  memset(inq, 0, sizeof(inq));
  memset(dp, -1, sizeof(dp));
  
  deque<state> work;
  state st = { 0, 0, 0 };
  work.push_back(st);
  inq[0][0][0] = true;
  dp[0][0][0] = 0;
  
  while( !work.empty() )
  {
    st = work.front();
    work.pop_front();
    inq[st.i][st.a][st.b] = false;
    int nt = dp[st.i][st.a][st.b] + 1;

    if( v[st.i].first && v[st.i].second == st.a )
    {
      if( st.i + 1 == n )
        return nt;
      
      for( int db = -1; db <= 1; ++db )
      {
        state q = { st.i+1, st.a, st.b+db };
        add(q, nt, work);
      }
    }
    else if( !v[st.i].first && v[st.i].second == st.b )
    {
      if( st.i + 1 == n )
        return nt;
      for( int da = -1; da <= 1; ++da )
      {
        state q = { st.i+1, st.a+da, st.b };
        add(q, nt, work);
      }
    }
    else
    {
      for( int da = -1; da <= 1; ++da )
      for( int db = -1; db <= 1; ++db )
      {
        state q = { st.i, st.a + da, st.b + db };
        add(q, nt, work);
      }
    }
  }
  
  return -1;
}

int main()
{
  int T;
  scanf("%d", &T);
  for( int C = 1; C <= T; C++ )
  {
    scanf("%d", &n);
    
    char buff[100];
    int b;
    for( int i = 0; i != n; ++i )
    {
      scanf("%s %d", buff, &b);
      v[i] = make_pair(buff[0] == 'O', b-1);
    }
    
    printf("Case #%d: %d\n", C, solve());
  }
  return 0;
}