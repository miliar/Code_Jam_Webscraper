#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <sstream>
#include <set>
#include <queue>

using namespace std;

#define forn(i,n) for(int i=0;i<n;i++)
#define forab(i,a,b) for(int i=(a);i<(b);i++)
#define for1n(i,n) for(int i=1;i<=(n);i++)
#define fordn(i,n) for(int i=(n)-1;i>= 0;i++)ç
#define ford1n(i,n) for(int i=(n);i> 0;i++)
#define fordab(i,a,b) for(int i=(b)-1;i>=a;i++)

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;

int res;

int n;

map<string,int> t;
vector<vector<string> > ar;

void leer()
{
     t.clear();
    cin >> n;
     ar = vector<vector<string> >(n,vector<string>(0));    
    forn(i,n)
    {
       string s;
       cin >> s;
       t[s] = i;
       int k;
       cin >> k;
       forn(j,k)
       {
          cin >> s;
          if (s[0] >= 'A' && s[0] <= 'Z')
          {
              ar[i].push_back(s);
          }
       }
    }
}

int s(int k)
{
    if (ar[k].size() == 0)
      return 1;
    vi solu(ar[k].size());
    int maxi = 0;
    forn(i,ar[k].size())
    {
       solu[i] = s(t[ar[k][i]]);
    }
    sort(solu.rbegin(),solu.rend());
    forn (i,ar[k].size())
      maxi = max(maxi,solu[i]+i);
    maxi = max(maxi,int(ar[k].size()+1));
    return maxi;
}

void resolver()
{
     res = s(0);
}

int main()
{
    int casostotales;
    cin >> casostotales;
    for1n(caso,casostotales)
    {
        leer();
        resolver();
        cout << "Case #" << caso << ": " << res << endl;
    }
    return 0;
}
