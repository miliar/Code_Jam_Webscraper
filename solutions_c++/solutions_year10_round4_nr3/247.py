#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
typedef long long LL;
const double EPS = 1e-8;
const int INF = (1<<29);

int n;
bool a[1100][1100],b[200][200];

int main(){
  int ca; scanf("%d",&ca);
  for (int tt=1; tt<=ca; tt++){
    scanf("%d",&n);
    memset(a,0,sizeof(a));
    for (int i=0; i<n; i++){
      int x1,y1,x2,y2; scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
      for (int x=x1; x<=x2; x++){
        for (int y=y1; y<=y2; y++){
          a[x][y]=true;
        }
      }
    }
    int ans=0;
    while (true){
      int cnt=0;
      for (int i=1; i<=100; i++){
        for (int j=1; j<=100; j++){
          cnt += (a[i][j]==1);
        }
      }
      if (cnt==0) break;
      ans++;

      for (int i=1; i<=100; i++){
        for (int j=1; j<=100; j++){
          b[i][j]=a[i][j];
          if (a[i][j] && !a[i-1][j] && !a[i][j-1]) b[i][j]=false;
          if (!a[i][j] && a[i-1][j] && a[i][j-1]) b[i][j]=true;
        }
      }
      for (int i=1; i<=100; i++){
        for (int j=1; j<=100; j++){
          a[i][j]=b[i][j];
        }
      }
    }
    printf("Case #%d: %d\n",tt,ans);
  }
  return 0;
}
