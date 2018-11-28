#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cctype>

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define sz(a) (int)(a).size()
#define pb push_back
#define mp make_pair
#define fi first
#define se second


typedef long long ll;
typedef pair <int, int> pii;
int tab[104][105];
char ans[105][105];
vector<pair<int, pair<int, int> > > cells;
pair<int, int> sdv[4];

int main()
{
  freopen("b.in", "r", stdin);
  freopen("tm.out", "w", stdout);
  int t, h, w;
  sdv[0].fi = -1;
  sdv[0].se = 0;

  sdv[1].fi = 0;
  sdv[1].se = -1;

  sdv[2].fi = 0;
  sdv[2].se = 1;

  sdv[3].fi = 1;
  sdv[3].se = 0;

  scanf("%d", &t);
  forn(tests, t)
  {
     cells.resize(0);
     scanf("%d%d", &h, &w);
     forn(i, h)
       forn(j, w){
         scanf("%d", &tab[i][j]);
         cells.push_back(mp(tab[i][j], mp(i, j)));
       }
  
    char cur = 'a'-1;

    int wh = w*h;
    sort(cells.begin(), cells.end());
    memset(ans,0, sizeof(ans));
    forn(i, cells.size())
    {
      int lmin = cells[i].fi;
      int lnum = 0;
      forn(j, 4)
      {
        int ni = cells[i].se.fi+sdv[j].fi;
        int nj = cells[i].se.se+sdv[j].se;

        if ((ni>=0)&&(nj>=0)&&(ni<h)&&(nj<w))
        {
           if (tab[ni][nj]<lmin)
           lmin = tab[ni][nj], lnum = j;
        }
      }
      if (lmin<tab[cells[i].se.fi][cells[i].se.se])
      {
        int ni = cells[i].se.fi+sdv[lnum].fi;
        int nj = cells[i].se.se+sdv[lnum].se;
        ans[cells[i].se.fi][cells[i].se.se] = ans[ni][nj];      
      }
      else
      {
        cur++;
        ans[cells[i].se.fi][cells[i].se.se] = cur;
      }
    }
    printf("Case #%d:\n",tests+1);
    set<char> rs;
    rs.clear();
    char res[40];
    memset(res, 0, sizeof(res));
    char reb = 'a';
    forn(i, h)
      forn(j, w)
	  {
		 if (rs.find(ans[i][j]) == rs.end())
	 	 {
			rs.insert(ans[i][j]);
			res[ans[i][j]-'a'] = reb;
			reb++;
 		 }
      }
    forn(i, h)
      forn(j, w)
  	ans[i][j] = res[ans[i][j]-'a'];
    forn(i, h)
    {
      forn(j, w)
        printf("%c ", ans[i][j]);
      printf("\n");
    }
  }
  return 0;
}
