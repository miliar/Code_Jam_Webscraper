#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>


using namespace std;

int L[1111], P[1111], X[1111], v[1111];

bool cmp(int a, int b) {
  int aa=L[a]*100+L[b]*X[a];
  int bb=L[b]*100+L[a]*X[b];
  return aa==bb?a<b:aa<bb;
}


int main() {
  int T;
  scanf("%d", &T);
  for (int tc=1; tc<=T; tc++) {
    int N;
    cin>>N;

    for (int i=0; i<N; i++) cin>>L[i];
    for (int i=0; i<N; i++) cin>>P[i];

    for (int i=0; i<N; i++) X[i]=100-P[i];

    for (int i=0; i<N; i++) v[i]=i;

    sort(v, v+N, cmp);
    
      
    printf("Case #%d:", tc);
    for (int i=0; i<N; i++)
      printf(" %d", v[i]);
    
    puts("");
      
  }

  return 0;
}
