#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

#define forn(i,n) for(int i=0;i<(n);i++)
#define forab(i,a,b) for(int i=(a);i<(b);i++)

int cuenta(int a)
{
    int suma = 0;
    forn(i,30)
      suma += (((1<<i) & a) != 0);
    return suma;
}

int d[15][1<<11];
int f[15];

inline bool vale(int a,int b)
{
     return  (a & b) == 0 && (a & (b<<1)) == 0 && (a & (b>>1)) == 0;
}

int main()
{
    int casos;
    cin >> casos;
    forn(caso,casos)
    {
        int m,n;
        cin >> m >> n;        
        vector<vector<bool> > t;
        t.resize(m);
        forn(i,m)
         t[i].resize(n);
        string s;        
        getline(cin,s);
        forn(i,m)
        {
          getline(cin,s);
          forn(j,n)
            t[i][j] = (s[j] == 'x');
        }
        forn(i,n)
        {
          f[i]  = 0;
          forn(j,m)
           if (t[j][i])
             f[i] |= (1<<j);
        }
        forn(i,1<<m)
          if ((f[0] & i) == 0)
            d[0][i] = cuenta(i);
          else
            d[0][i] = -1;
        forab(j,1,n)
        forn(i,1<<m)
        if ((f[j] & i) == 0)
        {
          int maxi = -1;
          forn(k,1<<m)
          if (d[j-1][k] != -1 && vale(i,k))
             maxi = max(maxi,d[j-1][k]);
          d[j][i] = maxi + cuenta(i);
        }
        else
          d[j][i] = -1;
        int sol = 0;
        forn(i,1<<m)
          sol = max(sol,d[n-1][i]);
        cout << "Case #" << caso+1 << ": " << sol << endl;
    }
    return 0;
}
