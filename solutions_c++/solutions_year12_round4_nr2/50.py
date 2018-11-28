#include <stdio.h>
#include <ctype.h>
#include <iostream>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <assert.h>

//#define M_PI 3.141592653589793238462643
#define eps 1e-8
#define inf ((int)1e9)
#define pb push_back
#define mp make_pair

using namespace std;

set <pair <int, int> > S;
int sz, n, w, l;
set <pair <int, int> > :: iterator it;
vector <pair <int, int> > V;
pair <int, int> A[1100];
int Res[1100][2];
int R[1100];

int main()
{
  int tst, cnt, i, j, x, y;
  freopen(".in", "r", stdin);
  freopen(".out", "w", stdout);
  scanf("%d", &tst);
  for (cnt=1; cnt<=tst; cnt++)
  {
    cerr<<cnt<<endl;
    scanf("%d%d%d", &n, &w, &l);
    for (i=0; i<n; i++)
    {
      scanf("%d", &A[i].first), A[i].second=i, j=0;
      while ((1<<j)<A[i].first)
        j++;
      A[i].first=(1<<j);
      //cerr<<"??? "<<A[i].first<<endl;
    }
    printf("Case #%d:", cnt);
    sort(A,A+n,greater<pair <int, int> >());
    for (i=0; i<n; i++)
      R[A[i].second]=A[i].first;
    S.clear(), S.insert(mp(0,0)), sz=A[0].first;
    for (i=0; i<n; i++)
    {
      while (sz>A[i].first)
      {
        sz/=2, V.clear();
        for (it=S.begin(); it!=S.end(); it++)
          V.pb(mp(it->first+2*sz,it->second));
        for (j=0; j<(int)V.size(); j++)
          S.insert(V[j]);
      }
      x=S.begin()->first, y=S.begin()->second;
      Res[A[i].second][0]=x, Res[A[i].second][1]=y, S.erase(S.begin());
      if (y+2*sz<=l)
        S.insert(mp(x,y+2*sz));
      if (S.size()==0)
        S.insert(mp(x+2*sz,0));
    }
    for (i=0; i<n; i++)
      assert(Res[i][0]<=w), printf(" %d %d", Res[i][0], Res[i][1]);
    for (i=0; i<n; i++)
      for (j=i+1; j<n; j++)
        assert(((Res[i][0]-Res[j][0])*1ll*(Res[i][0]-Res[j][0])+(Res[i][1]-Res[j][1])*1ll*(Res[i][1]-Res[j][1]))>=(R[i]+R[j])*(R[i]+R[j]));
    printf("\n");
  }
  return 0;
}
