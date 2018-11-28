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

typedef pair<int,int> pt;

int main()
{
  int T;
  scanf("%d", &T);
  for(int t = 1 ; t <= T ; t++)
    {
      printf("Case #%d: ", t);
      ll n, A, B, C, D, x0, y0, M;
      scanf("%lld%lld%lld%lld%lld%lld%lld%lld",
            &n, &A, &B, &C, &D, &x0, &y0, &M);
      ll X=x0,Y=y0;
      ll q[3][3];
      memset(q,0,sizeof(q));
      REP(i,n)
        {
          q[X%3][Y%3]++;
          X=(A*X+B)%M;
          Y=(C*Y+D)%M;
        }
      
      
      ll d=0;
      REP(x1,3)
        REP(y1,3)
        {
          d+=q[x1][y1]*(q[x1][y1]-1)*(q[x1][y1]-2)/6;

          for(int x3=x1;x3<3;x3++)
            for(int y3=x3==x1?y1+1:0;y3<3;y3++)
              if((2*x1+x3)%3==0&&(2*y1+y3)%3==0)
              d+=q[x1][y1]*(q[x1][y1]-1)*q[x3][y3]/2;

          for(int x2=x1;x2<3;x2++)
            for(int y2=x2==x1?y1+1:0;y2<3;y2++)
              {
                if((x1+2*x2)%3==0&&(y1+2*y2)%3==0)
                  d+=q[x1][y1]*q[x2][y2]*(q[x2][y2]-1)/2;

                for(int x3=x2;x3<3;x3++)
                  for(int y3=x2==x3?y2+1:0;y3<3;y3++)
                    if((x1+x2+x3)%3==0&&(y1+y2+y3)%3==0)
                      d+=q[x1][y1]*q[x2][y2]*q[x3][y3];
              }
        }
      printf("%lld", d);
      puts("");
    }

  return 0;
}
