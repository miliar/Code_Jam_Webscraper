#include <cstdio>
#include <vector>
using namespace std;

const int MAXM=105;

class T
{
public:
  T() { }
  T(int _batch, int _val) { batch=_batch, val=_val; }
  int batch, val;
};

vector<T> next[MAXM];
int n,m;

bool check(int st)
{
  for(int i=0;i<m;i++) {
    bool in=0;
    for(int j=0;j<next[i].size();j++)
      if(((st>>next[i][j].batch)&1) == next[i][j].val)
	{ in=1; break; }
    if(!in) return 0;
  }
  return 1;
}

int main()
{
  int tt;
  scanf("%d",&tt);
  for(int t=1;t<=tt;t++) {
    for(int i=0;i<MAXM;i++)
      next[i].clear();
    scanf("%d%d", &n, &m);
    for(int i=0;i<m;i++) {
      int num;
      scanf("%d", &num);
      while(num--) {
	int batch, val;
	scanf("%d%d", &batch, &val);
	next[i].push_back(T(batch-1, val));
      }
    }
    int res=-1, resval=50;
    for(int st=0;st<(1<<n);st++) { //1 iff melted
      if(!check(st)) continue;
      int b=__builtin_popcount(st);
      if(b<resval) {
	res=st; resval=b;
      }
    }
    printf("Case #%d: ", t);
    if(res==-1)
      { printf("IMPOSSIBLE\n"); continue; }
    for(int i=0;i<n;i++)
      printf("%d ", (res>>i)&1);
    printf("\n");
  }
  return 0;
}
