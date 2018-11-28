#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <iostream>
#include <map>
using namespace std;

#define For(i, n) for(int i=0; i<n; i++)
const int INF=1000000000;

int H, W;
char A[15][15];

int numbits(int x)
{
  int ret=0;
  while(x>0) {
    if(x%2) ret++;
    x/=2;
  } 
  return ret;
}

bool isok(int x)
{
  if((x&(x<<1))!=0) return false;
  return true;
}

bool compat(int p, int c)
{
  if(!isok(p) or !isok(c)) return false;
  if((p&(c<<1))!=0) return false;
  if((p&(c>>1))!=0) return false;
  return true;
}

bool obstruction(int s, int r)
{
  for(int i=0; i<W; i++){
    if((s&(1<<i))!=0 and A[r][i]!='.') return true;
  }
  return false;
}

int C[1500000][15];
int main()
{
  int T;
  scanf("%d", &T);
  for(int t=0; t<T; t++){
 

    scanf("%d%d\n", &H, &W);
    int S=1<<W;
    for(int i=1; i<=H; i++)
      scanf("%s\n", A[i]);
    
    For(i, S) C[i][0]=-INF;
    C[0][0]=0;
    for(int i=1; i<=H; i++){
      For(c, S){
	C[c][i]=0;
	For(p, S){
	  if(!obstruction(c, i) and compat(p, c)){
	    C[c][i]=max(C[c][i], C[p][i-1]+numbits(c));
	  }
	}
	//printf("c=%d i=%d C=%d\n", c, i, C[c][i]);
      }
    }

    int best=0;

    For(i, S) if(isok(i)) best=max(best, C[i][H]);
    
    printf("Case #%d: %d\n", t+1, best);
  }
  return 0;
}
