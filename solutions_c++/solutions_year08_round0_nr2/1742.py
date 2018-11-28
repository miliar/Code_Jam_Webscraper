#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<numeric>
#include<cmath>

using namespace std;

#define PB push_back
#define SZ(x) int((x).size())
#define ALL(a) (a).begin(),(a).end()
#define REP(i,n) for(int i=0;i<(n);i++)
 
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;

int main()
{
  int T[2][2500];
  
  int N;
  scanf("%d", &N);
  for(int n = 1 ; n <= N ; n++)
    {
      memset(T, 0, sizeof(T));
      int t, nn[2] ;
      scanf("%d%d%d", &t, &nn[0], &nn[1]);
      REP(i,2)
	REP(n,nn[i])
	{
	  int h1,m1,h2,m2;
	  scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
	  int a1 = 60 * h1 + m1, a2 = 60 * h2 + m2 + t;
	  T[i][a1]--;
	  T[1-i][a2]++;
	}
 
      int nb[] = {0,0}, sum[] = {0,0};
      for(int h = 0 ; h < 2400 ; h++)
	REP(i,2)
	  {
	    sum[i] += T[i][h];
	    if(sum[i] < 0)
	      {
		nb[i] -= sum[i];
		sum[i] = 0;
	      }
	  }

      printf("Case #%d: %d %d\n", n, nb[0], nb[1]);
    }
  return 0;
}
