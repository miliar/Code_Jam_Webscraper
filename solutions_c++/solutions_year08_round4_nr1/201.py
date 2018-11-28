#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std; typedef unsigned long ulong; typedef long long llong;

inline int gate(int c, int a, int b) { return c?(a && b):(a || b); }

int main()
{
int cases;

cin >> cases;

for(int loop=1;loop<=cases;loop++)
{
  int i,j,k,l,x;
  int m,v; cin >> m >> v;

  int G[m+1],V[m+1],C[m+1];
  int M[2][m+1];
  int cut=(m+1)/2;

  for(i=1;i<=(m-1)/2;i++) cin >> G[i] >> C[i];
  for(;i<=m;i++) cin >> V[i];

  for(i=cut;i<=m;i++) { M[V[i]][i]=0; M[!V[i]][i]=99999999; }

  for(i=cut-1;i>0;i--) for(j=0;j<2;j++)
  {
    int m=99999999;

    for(k=0;k<2;k++) for(l=0;l<2;l++) for(x=0;x<=C[i];x++)
    {
      int a=M[k][2*i], b=M[l][2*i+1];

      if (gate( (G[i]+x)%2, k, l) == j)
      { m = min(m,a+b+x); }
    }

    M[j][i]=m;
  }

  if (M[v][1] < 100000)
    cout << "Case #" << loop << ": " << M[v][1] << endl;
  else
    printf("Case #%d: IMPOSSIBLE\n",loop);
}

}
