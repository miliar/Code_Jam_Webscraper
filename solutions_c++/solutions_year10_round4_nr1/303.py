#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <functional>
#include <sstream>
#include <iostream>
#include <ctime>
#include <algorithm>
using namespace std;

#define DEBUG(x...) printf(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define _foreach(it, b, e) for(__typeof__(b) it = (b); it != (e); ++it)
#define foreach(x...) _foreach(x)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll; // sao dois L's!!!
const double eps = 1e-9;

// em caso de emergencia
#define _inline(f...) inline f() __attribute__((always_inline)); f

int sq(int a) { return a * a; }

char tab[500][500];//, tab2[500][500], tab3[500][500];
char buf[220][220];
int k;

int main()
{
  int ntests;
  scanf(" %d", &ntests);
  for (int test=1; test<=ntests; ++test)
    {
      memset(tab, 0, sizeof(tab));
      // memset(tab2, 0, sizeof(tab2));
      // memset(tab3, 0, sizeof(tab3));
      scanf(" %d", &k);
      for (int i=0; i<2*k-1; ++i)
	for (int j=0; j<k; ++j)
	  if (i-j >= 0 && i-j < k)
	    scanf(" %c", &tab[i-j][j]);
      // for (int i=0; i<k; ++i)
      // 	for (int j=0; j<k; ++j)
      // 	  tab2[i][j] = tab[k+j][k+i];
      // for (int i=0; i<k; ++i)
      // 	for (int j=0; j<k; ++j)
      // 	  tab3[i][j] = tab[k+k-j-1][k+k-i-1];
      // for (int i=0; i<k; ++i)
      // 	{
      // 	  for (int j=0; j<k; ++j)
      // 	    printf(" %c", tab[k+i][k+j]);
      // 	  printf("\n");
      // 	}
      // for (int i=0; i<k; ++i)
      // 	{
      // 	  for (int j=0; j<k; ++j)
      // 	    printf(" %c", tab2[i][j]);
      // 	  printf("\n");
      // 	}
      //int mincost = inf;
      // //for (int nk=k; nk<=2*k; ++nk)
      // for (int i=0; i<=2*k; ++i)
      // 	for (int j=0; j<=2*k; ++j)
      // 	  {
      // 	    bool ok = true;
      // 	    for (int a=0; a<k; ++a)
      // 	      for (int b=0; b<k; ++b)
      // 		if (tab[a+i][b+j] != 0 && (tab[a+i][b+j] != tab2[a][b] || tab[a+i][b+j] != tab3[a][b]))
      // 		  ok = false;
      // 	    // if (ok)
      // 	    //   printf("d: %d %d\n", i, j);
      // 	    if (ok)
      // 	      mincost = min(mincost, sq(k + max(abs(k-i), abs(k-j))) - sq(k));
      // 	  }
      bool goon = true;
      for (int nk=k; nk<=3*k+2&&goon; ++nk)
	for (int i=0; i<=nk-k&&goon; ++i)
	  for (int j=0; j<=nk-k&&goon; ++j)
	    {
	      memset(buf, 0, sizeof(buf));
	      for (int a=0; a<k; ++a)
		for (int b=0; b<k; ++b)
		  buf[i+a][j+b] = tab[a][b];
	      // for (int a=0; a<nk; ++a) {
	      // 	for (int b=0; b<nk; ++b)
	      // 	  printf("%c ", (buf[a][b]==0)?'0':buf[a][b]);
	      // 	printf("\n");
	      // }
	      bool ok = true;
	      for (int a=0; a<nk&&ok; ++a)
		for (int b=0; b<nk&&ok; ++b)
		  {
		    if (buf[b][a] == 0)
		      buf[b][a] = buf[a][b];
		    else if (buf[a][b] != 0 && buf[a][b] != buf[b][a])
		      { ok = false; }
		  }
	      for (int a=0; a<nk&&ok; ++a)
		for (int b=0; b<nk&&ok; ++b)
		  {
		    if (buf[nk-b-1][nk-a-1] == 0)
		      buf[nk-b-1][nk-a-1] = buf[a][b];
		    else if (buf[a][b] != 0 && buf[nk-b-1][nk-a-1] != buf[a][b])
		      { ok = false; }
		  }
	      // for (int a=0; a<nk; ++a) {
	      // 	for (int b=0; b<nk; ++b)
	      // 	  printf("%c ", (buf[a][b]==0)?'0':buf[a][b]);
	      // 	printf("\n");
	      // }
	      if (ok)
		{
		  printf("Case #%d: %d\n", test, sq(nk) - sq(k));
		  goon = false;
		}
	      // else printf(":(\n");
	    }
    }
  return 0;
}
