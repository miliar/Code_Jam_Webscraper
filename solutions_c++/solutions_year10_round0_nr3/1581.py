#include <iostream>

using namespace std;

typedef long long int uint;

uint G[1001]; // groups
int next[1001];
uint vals[1001];
bool visited[1001];

void buildTable(unsigned int n, unsigned int k)
{
  uint i, j, curr;
  // build next's table
  for(i=0; i < n; i++)
  {
    curr = 0;
    j = i;
    while(curr == 0 || j != i)
    { 
      if(curr + G[j] <= k)
      {
        curr += G[j];
        j++;
        if(j >= n)
          j = 0;
      }
      else
        break;
    }
    vals[i] = curr;
    next[i] = j;
  }
}
void solveCase(uint caseNum)
{
  unsigned int r, k, n; // inputs
  cin >> r >> k >> n;
  uint i, j;
  for(i=0; i < n; i++)
  { 
    next[i] = -1;
    vals[i] = 0;
    visited[i] = false;
    cin >> G[i];
  }

  buildTable(n,k);

  // simulate
  uint runs = 0, total = 0;
  i = 0;
  while(runs < r && !visited[i])
  {
    total += vals[i];
    visited[i] = true;
    i = next[i];
    runs++;
  }

  if(runs < r)
  { // in cicle, cicle starts at i
    // calculate cicle len and cost
    uint len = 0, cost = 0, left = r - runs;
    j = i;
    while(cost == 0 || j != i)
    {
      len++;
      cost += vals[j];
      j = next[j];
    }
    
    total += cost * (left / len);
    runs = 0;
    while(runs < (left % len))
    {
      total += vals[i];
      i = next[i];
      runs++;
    }
  }
  cout << "Case #" << caseNum << ": " << total << endl;
}

int main()
{
  uint t, i;

  cin >> t;
  for(i=1; i<=t; i++)
    solveCase(i);

  return 0;
}
