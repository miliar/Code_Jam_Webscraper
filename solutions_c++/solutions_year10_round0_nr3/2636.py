#include<cstdio>
#include<queue>
using namespace std;
int main()
{
  int T;
  scanf("%d",&T);
  for(int i=1;i<=T;i++){
    int R,k,N,cost = 0;
    queue<int> q;
    scanf("%d%d%d",&R,&k,&N);
    for(int j=0;j<N;j++){
      int t;
      scanf("%d",&t);
      q.push(t);
    }
    for(int j=0;j<R;j++){
      int r = 0,c = 0;
      while(1){
	int nr = q.front();
	if(r+nr > k || c >= N){
	  cost += r;
	  break;
	}
	r += nr;
	q.pop();
	q.push(nr);
	c++;
      }
    }
    printf("Case #%d: %d\n",i,cost);
  }
  return 0;
}
