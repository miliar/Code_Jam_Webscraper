#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

int list[100][3];
int n;

void init(){
  int i;
  scanf("%d",&n);
  for (i=0;i<n;i++){
    scanf("%d%d%d",&list[i][0],&list[i][1],&list[i][2]);
  }
}

double dist(int a,int b){
  return (sqrt((list[a][0]-list[b][0])*(list[a][0]-list[b][0])+(list[a][1]-list[b][1])*(list[a][1]-list[b][1]))+list[a][2]+list[b][2])/2;
}

double solve(){
  int i,j,k;
  double res,t;
  
  if (n==1) return list[0][2];
  if (n==2) return max(list[0][2],list[1][2]);
  
  res=10000000;
  for (i=0;i<3;i++){
    for (j=i+1;j<3;j++){
      for (k=0;k<3;k++)if(k!=i && k!=j){
        t=max(dist(i,j),(double)list[k][2]);
        if (t<res) res=t;
      }
    }
  }
  return res;
}

int main(){
  int t,k=0;
  scanf("%d",&t);
  while (t--){
    k++;
    printf("Case #%d: ",k);
    init();
    printf("%.12lf\n",solve());
  }
  return 0;
}

