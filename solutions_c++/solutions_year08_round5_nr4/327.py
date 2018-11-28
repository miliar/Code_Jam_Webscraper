#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

#define forn(i,n) for(int i=0;i<(n);i++)
#define forab(i,a,b) for(int i=(a);i<(b);i++)

#define ii pair<int,int>

int w,h;

set <ii> s;
map <ii,int> a;

int c(ii p)
{
    if (p.first <= 0 || p.second <= 0 || s.find(p) != s.end())
     return 0;
    if (a.find(p) == a.end())
      a[p] = (c(ii(p.first-1,p.second-2)) + c(ii(p.first-2,p.second-1))) % 10007;
    return a[p];
}

int main()
{
    int casos;
    cin >> casos;
    forn(caso,casos)
    {
        int h,w,R;
        cin >> h >> w >> R;
        s.clear();
        a.clear();
        forn(i,R)
        {
          int x,y;
          cin >> x >> y;
          s.insert(ii(x,y));
        }
        a[ii(1,1)] = 1;
        cout << "Case #" << caso+1 << ": " << c(ii(h,w)) << endl;
    }
    return 0;
}
