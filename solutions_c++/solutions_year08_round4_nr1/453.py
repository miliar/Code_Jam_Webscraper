#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>

#define f(x,y) for(int x=0; x<(y); ++x)
using namespace std;
#define MAX 10001
int N, M, V, G, C, type[MAX], chab[MAX], val[MAX], inv[MAX];
int main(){
  scanf("%d", &N);
  f(t, N){
    scanf("%d%d", &M, &V);
    int i;
    for (i=1; i<= (M-1)/2; ++i){
      scanf("%d%d", &type[i], &chab[i]);
      val[i]=0;
      inv[i]=MAX+1;
    }
    for(i; i<=M; ++i){
      scanf("%d", &val[i]);
      inv[i]=MAX+1;
    }
    // Go!
    for(int i=(M-1)/2; i>=1; --i){
      int val1= (val[2*i] && val[2*i+1]);
      int val2= (val[2*i] || val[2*i+1]);      
      if(type[i]==1) val[i]= val1;
      else           val[i]= val2;
      int res=MAX+1;
      if(chab[i]==1){
	if(val1!=val2){
	  res=1;
	  //printf("At %d\n", i);
	}
	else if(val[2*i] == !type[i]) res=min(inv[2*i]+1, inv[2*i+1]+1);
	else res=min(inv[2*i], inv[2*i+1]);
      } else{
	if(type[i]==1 && val[i]==1){
	  res=min(inv[2*i], inv[2*i+1]);
	} else if(type[i]==1 && val[i]==0){
	  if(val[2*i]==0 && val[2*i+1]==0)
	    res=inv[2*i]+inv[2*i+1];
	  else if(val[2*i]==0)
	    res=inv[2*i];
	  else if(val[2*i+1]==0){
	    res=inv[2*i+1];
	    //printf("Here at %d (%d)", i, inv[3]);

	  }
	} else if(type[i]==0 && val[i]==0){
	  res=min(inv[2*i], inv[2*i+1]);
	} else{
	  if(val[2*i]==1 && val[2*i+1]==1)
	    res=inv[2*i]+inv[2*i+1];
	  else if(val[2*i]==1)
	    res=inv[2*i];
	  else if(val[2*i+1]==1)
	    res=inv[2*i+1];
	}	
      }
      inv[i]=res;
    }
    printf("Case #%d: ", t+1);
    if(V==val[1]) printf("0\n");
    else if(inv[1]>=MAX) printf("IMPOSSIBLE\n");
    else printf("%d\n", inv[1]);
  }
  return 0;
}
