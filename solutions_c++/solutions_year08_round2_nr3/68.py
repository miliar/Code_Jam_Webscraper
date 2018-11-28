#include<algorithm>
#include<cstdlib>
#include<iostream>
#include<map>
#include<sstream>
#include<set>
#include<string>
#include<numeric>
#include<vector>
#include<cmath>

#define PB push_back
#define SZ(x) int((x).size())
#define ALL(a) (a).begin(),(a).end()
#define REP(i,n) for(int i=0;i<(n);i++)

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

int y[5005];

int main()
{
  int T;
  scanf("%d", &T);
  for(int t = 1 ; t <= T ; t++)
    {
      printf("Case #%d:", t);
      int K,n;
      int d[100];
      scanf("%d%d",&K,&n);
      REP(i,n)
        scanf("%d",&d[i]);
      memset(y,0,sizeof(y));
      int c=0;
      y[0]=1;
      for(int k=2;k<=K;k++)
        {
          int u=1+(k-1)%(K-k+1);
          for(;;c=c==K-1?0:c+1)
            {
              if(!y[c])
                u--;
              if(!u)
                break;
            }
          y[c]=k;
        }
      REP(i,n)
        printf(" %d",y[d[i]-1]);
      puts("");
    }

  return 0;
}
