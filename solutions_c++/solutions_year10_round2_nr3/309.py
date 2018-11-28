#include<cassert>
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
#define sqr(a) (a)*(a)
#define forn(i,n) for(int i=0;i<(int)n;i++)
#define taskname ""
typedef long long ll;
using namespace std;
#define N 1000
#define K 100003
int ans[N];
int main()         
{
  //#ifdef DEBUG
  /*freopen(taskname".in","r",stdin);                         
  freopen(taskname".out","w",stdout);*/
  //#endif
  int testn;
  scanf("%d ",&testn);
  forn(test,testn)
  {
    int n;
    printf("Case #%d: ",test+1);
    scanf("%d",&n);
    int s=0;
    forn(mask,1<<(n-1))
    {
      int sz=1;
      forn(i,n-1)
      {
        if(mask>>i&1)
          ans[i+2]=(sz++);
        else 
          ans[i+2]=-1;
      }
      int tmp=n;
      while(tmp!=-1&&tmp!=1)
        tmp=ans[tmp];
      if(tmp==1)
      {
        s=(s+1)%K;
        //cerr<<mask<<endl;
      }
    }
    printf("%d\n",s);
  }
  return 0;
}

