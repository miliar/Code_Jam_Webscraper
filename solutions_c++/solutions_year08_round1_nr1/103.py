#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<sstream>
#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
using namespace std;
int x[1000];
int y[1000];
void solve(){
  int n;
  scanf("%d",&n);
  for(int i=0;i<n;i++){
    scanf("%d",x+i);
  }
  for(int i=0;i<n;i++){
    scanf("%d",y+i);
  }
  sort(x,x+n);
  sort(y,y+n);
  long long w=0;
  for(int i=0;i<n;i++){
    w+=(long long)x[i]*y[n-1-i];
  }
  cout << w << endl;
}
int main(){
  int n;
  scanf(" %d ",&n);
  for(int t=1;t<=n;t++){
    printf("Case #%d: ",t);
    solve();
  }
}
