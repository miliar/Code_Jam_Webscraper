#include<cstdio>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<vector>

using namespace std;

#define TASK ""
#define deb(x) cerr<<#x<<'='<<(x)<<endl
#define forn(i,n) for(int i=0;i<(int)n;i++)

const int N=1<<20;
int old[2][N],nw[2][N];
int x[1000];
int main()
{
  #ifdef DEBUG
  freopen(TASK"in","r",stdin);
  freopen(TASK"out","w",stdout);
  #endif
  int tests_n;
  scanf("%d\n",&tests_n);
  forn(test_id,tests_n)
  {
    printf("Case #%d: ",test_id+1);
    int n;
    deb(test_id);
    scanf("%d",&n);
    forn(fl,2)
      forn(i,N)
      {
        old[fl][i]=-(1<<30);
        nw[fl][i]=-(1<<30);
      }
    old[0][0]=0;
    int s=0;
    int mx=-1;
    forn(i,n)
      scanf("%d ",&x[i]);
    sort(x,x+n);
    int last=0;
    forn(i,n)
    {
      s^=x[i];
      forn(fl,2)
        forn(j,max((last^x[i]),last)+1)
          nw[fl][j]=(-(1<<30));
      int nmx=0;
      forn(fl,2)
        forn(j,last+1)
          if(old[fl][j]!=-(1<<30))
          {
            nmx=max(nmx,max(j,j^x[i]));
            nw[fl][j^x[i]]=max(nw[fl][j^x[i]],old[fl][j]+x[i]);
            nw[true][j]=max(nw[fl][j],old[fl][j]);
          }
      last=nmx;
      forn(fl,2)
        forn(j,last+1)
          old[fl][j]=nw[fl][j];
    }
    forn(i,last+1)
      if((i == (s^i)))
      {
        mx=max(old[true][i],mx);
      }
    if(mx==-1)   	
      puts("NO");
    else
      printf("%d\n",mx);
  }
  return 0;
}
