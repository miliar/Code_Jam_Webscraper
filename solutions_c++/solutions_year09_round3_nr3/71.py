#include <cstdio>
#include <string>
#include <map>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int L[105];
int P, Q;
bool done[105][105];
int ans[105][105];

const int INF = 1000000000;

int memo(int a, int b)
{
  if(b-a<=1) return 0;

  if(done[a][b]) return ans[a][b];
  
  int ret = L[b]-L[a]-2;

  int mincost=INF;
  for(int i=a+1; i<b; i++){
    mincost = min(mincost, memo(a, i)+memo(i, b));
  }

  done[a][b] = true;
  ans[a][b] = mincost+ret;
  //printf("a=%d b=%d ans=%d\n", a, b, ans[a][b]);
  return ans[a][b];
}

int main()
{
  int cases;
  scanf("%d", &cases);
  for(int cas=0; cas<cases; cas++){
    for(int i=0; i<105; i++) for(int j=0; j<105; j++) done[i][j]=false;
			       
    printf("Case #%d: ", cas+1);
    
    scanf("%d %d", &P, &Q);
    
    L[0]=0;
    for(int i=1; i<=Q; i++) scanf("%d", &L[i]);
    Q+=2;
    L[Q-1]=P+1;

    printf("%d\n", memo(0, Q-1));
  }
}
