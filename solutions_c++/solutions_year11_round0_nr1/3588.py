#include<cassert>
#include<queue>
#include<cstring>
#include<cstdio>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<cmath>
#include<iostream>
#include<algorithm>

#define eps 1e-12

#define sqr(a) ((a)*(a))
#define mp(a,b) make_pair(a,b) 
#define forn(i,n) for(int i=0;i<(int)n;i++)
#define taskname ""
#ifdef DEBUG
#define deb(x) cerr<<#x<<'='<<x<<endl
#else
#define deb(x) 
#endif
typedef long long ll;

using namespace std;
int last[2];
char ss[3]="OB";
int x[2];
#define abs(x) ((x)>0?(x):-(x))
int main()         
{
//  assert(freopen(taskname"in","r",stdin));
//  assert(freopen(taskname"out","w",stdout));
  int test_n;
  scanf("%d",&test_n);
  forn(test_id,test_n)
  {
    printf("Case #%d: ",test_id+1);
    int t=0;
    x[0]=x[1]=1;
    last[0]=last[1]=0;
    int n;
    scanf("%d ",&n);
    forn(i,n)
    {
      char c;
      int k;
      scanf(" %c %d",&c,&k);
      forn(i,2)
        if(ss[i]==c)
        {
          t=max(t+1,last[i]+abs(x[i]-k)+1);
          last[i]=t;
          x[i]=k;
        }
    }
    printf("%d\n",t);
  }
  return 0;
}

