#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

vector <int> v1,v2;
int n;

void init(){
  int i,t;
  v1.clear();
  v2.clear();
  scanf("%d",&n);
  for (i=0;i<n;i++){
    scanf("%d",&t);
    v1.push_back(t);
  }
  for (i=0;i<n;i++){
    scanf("%d",&t);
    v2.push_back(t);
  }
  sort(v1.begin(),v1.end());
  sort(v2.rbegin(),v2.rend());  
}

long long solve(){
  int i;
  long long res=0;
  for (i=0;i<n;i++){
    res=res+v1[i]*v2[i];
  }
  return res;
}

int main(){
  int k,i;
  scanf("%d",&k);
  for (i=1;i<=k;i++){
    init();
    printf("Case #%d: %lld\n",i,solve());
  }
  return 0;
}

