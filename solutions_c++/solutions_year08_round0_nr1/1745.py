#include<cstdio>
#include<vector>
#include<iostream>
#include<string>
#include<algorithm>
#include<numeric>
#include<cmath>
#include<map>

using namespace std;

#define PB push_back
#define SZ(x) int((x).size())
#define ALL(a) (a).begin(),(a).end()
#define REP(i,n) for(int i=0;i<(n);i++)
 
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;

const int MAX_S = 100;

int main()
{
  int N;
  char b[200];
  scanf("%d\n", &N);
  for(int n = 1 ; n <= N ; n++)
    {
      int S;
      scanf("%d\n", &S);
      map<string, int> se;
      REP(s,S)
	{
	  fgets(b, 200, stdin);
	  se[string(b)] = s;
	}
      int Q;
      scanf("%d\n", &Q);
      int ce[MAX_S];
      memset(ce, 0, sizeof(ce));
      REP(q,Q)
	{
	  fgets(b, 200, stdin);
	  int cq=se[string(b)];
	  ce[cq] = MAX_S;
	  REP(qq,S)
	    if(qq != cq)
	      ce[cq] = min(ce[qq] + 1, ce[cq]);
	}
      printf("Case #%d: %d\n", n, *min_element(ce, ce + S));
    }


  return 0;
}
