#include <iostream>

using namespace std;

long long solve()
{
  int R, k, N;
  int g[1010];
  
  int np[1010]; // # of people
  int ng[1010]; // # of groups
  
  cin >> R >> k >> N;
  
  for(int i = 0; i < N; i++)
  {
    cin >> g[i];
  }

  for(int i = 0; i < N; i++)
  {
    np[i] = 0;
    ng[i] = 0;
    
    for(int j = i; j < i+N; j++)
    {
      if(np[i] + g[j%N] > k)
        break;
      
      np[i] += g[j%N];
      ng[i] ++;
    }
  }
  
  long long ret = 0;
  
  int ptr = 0;
  
  for(int i = 0; i < R; i++)
  {
    ret += np[ptr];
    ptr = (ptr + ng[ptr]) % N;
  }
  
  return ret;
}

int main()
{
  int T;
  cin >> T;
  
  for(int i = 0; i < T; i++)
  {
    cout << "Case #" << (1+i) << ": " << solve() << endl;
  }
  
  return 0;
}
