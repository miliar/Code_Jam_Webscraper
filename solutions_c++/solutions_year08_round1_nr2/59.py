#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define forn(i,n) for(int i=0;i<(n);i++)

int main()
{
    int T;
    cin >> T;
    forn(caso,T)
    {
      int n,m;
      cin >> n >> m;
      vector<vector<int> > p(m);
      vector<int> mal(m,-1);
      vector<int> sol(n,0);
      forn(i,m)
      {
        int t;
        cin >> t;
        forn(j,t)
        {
          int x,y;
          cin >> x >> y;
          if (y)
            mal[i] = x-1;
          else
            p[i].push_back(x-1);
        }
      }
      bool cambia = true;
      while (cambia)
      {
            cambia = false;
            forn(i,m)
            if (p[i].empty() && mal[i] != -1 && sol[mal[i]] == 0)
            {
               sol[mal[i]] = 1;
               cambia = true;
               forn(j,m)
               {
                 forn(k,p[j].size())
                 if (p[j][k] == mal[i])
                 {
                   swap(p[j][k],p[j][p[j].size()-1]);
                   p[j].pop_back();
                   break;
                 }
               }
            }
      }
      bool gano = true;
      forn(i,m)
       if (p[i].empty() && (mal[i] == -1 || sol[mal[i]] == 0))
       {
          gano = false;
          break;
       }
      cout << "Case #" << caso+1<<":";
      if (gano)
      {
        forn(i,n)
          cout << " " << sol[i];
      }
      else
        cout << " IMPOSSIBLE";
      cout << endl;
    }
    return 0;
}
