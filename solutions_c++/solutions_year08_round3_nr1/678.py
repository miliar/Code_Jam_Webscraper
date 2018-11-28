/// Problem A
/// gvaf --- Round 1C: Gooogle Code Jam 2008

#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <list>
#include <stack>
#include <iostream>
using namespace std;

void solve(int id, int P, int K, int L);

void solve(int id, int P, int K, int L, vector<int> & freq);

int main()
{
  int N;
  int P, K, L;

  cin >> N;

  for(int id = 0; id < N; ++id)
   {
     cin >> P >> K >> L;
     vector<int> freq;

     for(int j = 0; j < L; ++j)
     {
      int fr;
      cin >> fr;
      freq.push_back(fr);
     }

    solve(id+1, P, K, L, freq);
    
   } 



 return 0;
}

void solve(int id, int P, int K, int L, vector<int> & freq)
{
  sort(freq.begin(), freq.end(), greater<int>());
  vector<int> keyholes(K);
  long res = 0;

  int cur = 0;
  for(int i = 0; i < L; ++i)
  {
    while( keyholes[cur] + 1 > P )
      ++cur;

    if( cur >= K ) 
     {
      cout << "Case #" << id << ": Impossible" << endl;
      return;
     }

    ++keyholes[cur];        
    res += freq[i] * keyholes[cur];
    cur = (cur + 1) % K;
  }
 

   cout << "Case #" << id << ": " << res << endl;
  
}
