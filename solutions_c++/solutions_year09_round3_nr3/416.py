#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int Solve()
{
  int p, q;
  scanf("%d %d", &p, &q);
  vector <int> t;
  for (int i = 0; i < q; i++)
    {
      int tmp;
      scanf("%d", &tmp);
      t.push_back(tmp);
    }
  sort(t.begin(), t.end());
 
  bool used[128]; int minn = INT_MAX;
  do
  {
    memset(used, 0, sizeof(used));
    int pay = 0;
    for (int i = 0; i < q; i++)
      {
        
        for(int k = t[i] - 1; k >= 1; pay++, k-- )
          if (used[k]) break;
        for(int k = t[i] + 1; k <= p; pay++, k++ )
          if (used[k]) break;
        used[t[i]] = 1;
      }
    if (pay < minn) minn = pay;
  } while ( next_permutation(t.begin(), t.end()));
  
  return minn;
}

int main()
{ 
  int tests;
  scanf("%d", &tests);
  for (int i = 1; i <= tests; i++)
    {
      cout << "Case #" << i << ": " << Solve() << endl;
    }
    
  //system("pause");
  return 0;
}
