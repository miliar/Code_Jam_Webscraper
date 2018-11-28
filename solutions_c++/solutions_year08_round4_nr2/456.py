#include<cstdio>
#include<algorithm>
using namespace std;

int main()
{
  int T;
  scanf("%d", &T);
  for(int t=0; t<T; t++){
    int N, M, A;
    bool found=false;
    scanf("%d%d%d", &N, &M, &A);
    int x1, x2, y1, y2;
    for(x1=0; x1<=N; x1++)
      for(y1=0; y1<=M; y1++)
	for(x2=0; x2<=N; x2++)
	  for(y2=0; y2<=y1; y2++){
	    if(abs(x1*y2-x2*y1)==A){
	      found=true;
	      goto done;
	    }
	  }
    
  done:
    printf("Case #%d: ", t+1);
    if(!found) printf("IMPOSSIBLE\n");
    else printf("0 0 %d %d %d %d\n", x1, y1, x2, y2);
  }
  return 0;
}
