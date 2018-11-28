#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <queue>
#include <time.h>

using namespace std;

#define RP(a,h) for(int (a)=0; (a)<(h); (a)++)
#define FR(a,l,h) for((a)=(l); (a)<=(h); (a)++)
#define INF 2000000000
#define sz size()
#define pb push_back
#define sv(v) sort((v).begin(), (v).end())
#define ABS(x) (((x)>0)?(x):(-(x)))




vector< pair< pair<int, int>, int > > allt;
bool check[2001];
int main()
{
    int test;
    
    cin >> test;
    
    int turn, na, nb;
    int t1, t2, t3, t4;

    RP(t, test)
    {
          allt.clear();
          vector<int> res(2, 0);
          cin >> turn;
          cin >> na >> nb;
          RP(i, na)
          {
                scanf("%d:%d %d:%d", &t1, &t2, &t3, &t4);
                allt.pb(make_pair(make_pair(t1*60 + t2, t3*60 + t4), 0));
          }
          
          RP(i, nb)
          {
                scanf("%d:%d %d:%d", &t1, &t2, &t3, &t4);
                allt.pb(make_pair(make_pair(t1*60 + t2, t3*60 + t4), 1));
          }
          sv(allt);

          memset(check, false, sizeof(check));
          
          vector< pair <int, int> > sche;
          
          RP(i, na+nb)
          {
                //cout << allt[i].second << endl;
                bool found = false;
                RP(j, sche.sz)
                {
                      if (sche[j].first == allt[i].second && sche[j].second <= allt[i].first.first)
                      {
                         found = true;
                         sche[j].first = 1 - sche[j].first;
                         sche[j].second = allt[i].first.second + turn;
                         break;
                      }
                }
                
                if (! found)
                {
                      //cout << allt[i].second << endl;
                      sche.pb(make_pair(1 - allt[i].second, allt[i].first.second + turn));
                      res[allt[i].second] ++;
                }
          }
          
          cout << "Case #" << t+1 << ": " << res[0] << " " << res[1] << endl;

    }
        
    return 0;
}
