#include <iostream>
#include <string>
#include <map>

using namespace std;


unsigned long long int Solve()
{
  bool used[128];
  memset(used, 0, sizeof(used));
  map<char, int> op;
  int base = 0;
  
  string t;
  cin >> t;
  for (int i = 0; i < t.size(); i++)
    {
      if (op.find(t[i]) == op.end())
        {
          for(int j = 0; j < 128; j++)
            if (!used[j]) 
              {
                if(j == 0 && i == 0) continue;
                op.insert(pair<char,int>(t[i],j));
                used[j] = 1; base ++;
                break;
              }
        }
    }
  
  if (base == 1) base = 2;
  
  unsigned long long res = 0;
  for (int i = 0; i < t.size(); i++)
    res = res * base + op[t[i]];
  return res;
}

int main()
{
  int tests;
  scanf("%d", &tests);
  
  for (int i = 1; i <= tests; i++)
    {
      cout << "Case #" << i << ": "<< Solve() << endl;
    }
    
  //system("pause");
  return 0;
}
