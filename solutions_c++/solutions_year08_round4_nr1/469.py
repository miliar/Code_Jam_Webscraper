#include<cstdio>
#include<algorithm>
using namespace std;

const int INF=100000;
int M, val[11000], gate[11000], ch[11000];
int C[11000];

int main()
{
  int N;
  scanf("%d", &N);
  for(int t=0; t<N; t++){
    int V;
    scanf("%d%d", &M, &V);
    
    { 
      int i;
      for(i=0; i<int((M-1)/2); i++)
	scanf("%d %d", &gate[i], &ch[i]);
      for(; i<M; i++)
	scanf("%d", &val[i]);
    }
    
    for(int i=M-1; i>=0; i--){
      C[i]=INF;
      if(2*i+1<M){
	if(gate[i]==1) val[i]=val[2*i+1]&val[2*i+2];
	else val[i]=val[2*i+1]|val[2*i+2];

	if(gate[i]){
	  if(val[i]){  //AND, 1
	    C[i]=min(C[2*i+1], C[2*i+2]);
	  }
 	  else{   //AND, 0
	    int x=0, y=1;
	    if(val[2*i+1]==0) x+=C[2*i+1]; 
	    if(val[2*i+2]==0) x+=C[2*i+2];

	    if(val[2*i+1]==0 and val[2*i+2]==0) y+=min(C[2*i+1], C[2*i+2]);
	    C[i]=x;
	    if(ch[i]) C[i]=min(C[i], y);
	    //printf("x=%d y=%d\n", x, y);
	  }
	}
	else{
	  if(!val[i]){  //OR, 0
	    C[i]=min(C[2*i+1], C[2*i+2]);
	  }
	  else{   //OR, 1
	    int x=0, y=1;
	    if(val[2*i+1]==1) x+=C[2*i+1]; 
	    if(val[2*i+2]==1) x+=C[2*i+2];

	    if(val[2*i+1]==1 and val[2*i+2]==1) y+=min(C[2*i+1], C[2*i+2]);
	    C[i]=x;
	    if(ch[i]) C[i]=min(C[i], y);
       
	  }
	}
      }
      //printf("i=%d C=%d\n", i, C[i]);
    }

    if(val[0]==V) C[0]=0;
    printf("Case #%d: ", t+1);
    if(C[0]>10000) printf("IMPOSSIBLE\n");
    else printf("%d\n", C[0]);
    
  }
  return 0;
}
