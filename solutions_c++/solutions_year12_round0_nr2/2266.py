#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
  int N;

  cin >> N;

  for(int cas = 1; cas <= N; cas++)
  {
    int n,s,p;

    cin >> n >> s >> p;

    vector<int> ns(n);

    int ps=0,pp=0,pb=0,pd=0;
    
    for(int i = 0; i < n; i++)
    {
      int k;
      cin >> k;

      if(k % 3 == 0)
      {
        if(k / 3 >= p) pp++;

        if(k >= 2)
        {
          ps++;
          if(k / 3 + 1 >= p){
            pb++;
            if(k/3 >= p) pd++;
          }
        }
      }
      else if(k % 3 == 1)
      {
        if(k/3 + 1 >= p) pp++;
        if(k >= 2)
        {
          ps++;
          if(k / 3 + 1 >= p){
             pb++;
             pd++;
          }         
        }
      }
      else
      {
        if(k/3 + 1 >= p) pp++;
        if(k >= 2)
        {
          ps++;
          if(k / 3 + 2 >= p)
          {
            pb++;
            if(k/3 + 1 >= p) pd++;
          }
        }
      }
    }

    int pdif = pb-pd;
    int res;
    if(pdif >= s)
    {
      res = s + pp;
    }
    else
    {
      if(s > pb)
      {
        res = pb + pp - pd;
      }
      else
      {
        res = pp + pdif;
      }

    }

    cout << "Case #" << cas << ": " << res << endl;

  }

  return 0;
}
