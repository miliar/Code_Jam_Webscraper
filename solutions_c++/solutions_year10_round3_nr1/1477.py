#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
struct data{
  int a,b;
  bool operator<(const data &d)const{
    return a < d.a;
  }
};

int main()
{
  int T;
  scanf("%d",&T);
  for(int i=0;i<T;i++){
    data d[10000];
    int n;
    scanf("%d",&n);
    for(int j=0;j<n;j++){
      scanf("%d%d",&d[j].a,&d[j].b);
    }
    sort(d,d+n);
    int cnt = 0;
    for(int j=1;j<n;j++){
      for(int k=0;k<n-1;k++){
	if(d[k].b > d[j].b) cnt++;
      }
    }
    printf("Case #%d: %d\n",i+1,cnt);
  }
  return 0;
}
