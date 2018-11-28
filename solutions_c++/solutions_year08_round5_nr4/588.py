#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>

#define f(x,y) for(int x=0; x<(y); ++x)
using namespace std;
int N, W, H, R, arr[105][105];
int main(){
  scanf("%d", &N);
  f(t, N){
    scanf("%d%d%d", &H, &W, &R);
    for(int i=1; i<=H; ++i)
      for(int j=1; j<=W; ++j)
	arr[i][j]=0;
    f(i, R){
      int x, y;
      scanf("%d%d", &x, &y);
      arr[x][y]=-1;
    }
    arr[1][1]=1;
    for(int i=1; i<=H; ++i){
      for(int j=1; j<=W; ++j){
	if(arr[i][j]==-1){}
	else {
	  if(i>=3 && j>=2 && arr[i-2][j-1]>0){
	    if(arr[i-2][j]!=-1 || arr[i][j-1]!=-1)
	      arr[i][j]+=arr[i-2][j-1];
	  }
	  if(i>=2 && j>=3 && arr[i-1][j-2]>0){
	    if(arr[i-1][j]!=-1 || arr[i][j-2]!=-1)
	      arr[i][j]+=arr[i-1][j-2];
	  }
	}
	arr[i][j]%=10007;
	//printf("(%d)", arr[i][j]);
      }
      //printf("\n");
    }
    printf("Case #%d: %d\n", t+1, arr[H][W]);
  }
  return 0;
}
