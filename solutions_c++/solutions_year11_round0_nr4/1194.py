#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;


int main()
{
  int T;
  cin >> T;    
  for (int t = 1; t <= T; t++)
  {
    vector<int> array;
    array.push_back(0);
    vector<bool> visited;
    visited.push_back(true);
    int cyclesum = 0;
    int n; cin >> n;
    for (int i = 1; i <= n; i++)
    {
      int k; cin >> k;
      array.push_back(k);      
      visited.push_back(false);
    }    
    for (int i =1 ; i <= n;i++)
    {
      if (!visited[i])
      {
        vector<int> cycle;
        int j = i;
        int k = array[j];
        while (k != j)
        {     
          if (visited[j]) break;        
          cycle.push_back(j);
          visited[j] = true;  
          j = k;
          k = array[j];                  
        }
        cyclesum += cycle.size();
      }
    }
    printf("Case #%i: %.6f\n", t, (float)cyclesum);
  }
  
}