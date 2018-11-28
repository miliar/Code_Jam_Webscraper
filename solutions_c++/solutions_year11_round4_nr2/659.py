/* Writen by Filip Hlasek 2011 */
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <string>
#include <algorithm>
#include <cmath>

#define FOR(i,n) for(i=0;i<n;i++)
#define MAXR 555

using namespace std;

char m[MAXR][MAXR];
int R,C,D;

bool ok(int x,int y,int s){
  int i,j;
  double c=(double)(s-1)/2,sum=0;;
  //printf("x:%d y:%d s:%d\n",x,y,s);
  FOR(i,s) FOR(j,s){
    if((i+j==0)||(i+j==2*(s-1))||(i==0&&j==s-1)||(i==s-1&&j==0)) continue;
    sum+=(i-c)*(m[x+i][y+j]);
  }
  //printf("sum:%lf\n",sum);
  if(abs(sum)>1e-6) return false;
  sum=0;;
  FOR(i,s) FOR(j,s){
    if((i+j==0)||(i+j==2*(s-1))||(i==0&&j==s-1)||(i==s-1&&j==0)) continue;
    sum+=(j-c)*(D+m[x+i][y+j]);
  }
  if(abs(sum)>1e-6) return false;
  return true;
}

int main(int argc, char *argv[]){
  int t,T,i,j,k,result;
  scanf("%d",&T);
  FOR(t,T){
    result=-1;
    scanf("%d%d%d",&R,&C,&D);
    FOR(i,R){
      scanf("%s",m[i]);
      FOR(j,C) m[i][j]-='0';
    }
    for(i=3;i<=min(R,C);i++) for(j=0;j+i<=R;j++) for(k=0;k+i<=C;k++) if(ok(j,k,i)) result=i;
    printf("Case #%d: ",t+1);
    if(result<3) printf("IMPOSSIBLE\n");
    else printf("%d\n",result);
  }
  return 0;
}
