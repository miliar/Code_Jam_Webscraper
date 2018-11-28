#include <cstdio>
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;
int T,N,D,t,i,j;

int main() {
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);

  scanf("%d",&T);
  for (t=1;t<=T;t++) {
    scanf("%d",&N);
    vector<int> d(N),l(N);
    for (i=0;i<N;i++)
      cin>>d[i]>>l[i];

    scanf("%d",&D);
    vector<int> move(N,0);
    move[0]=d[0]<<1;
    for (i=1;i<N;i++)
      for (j=0;j<i;j++)
        if (move[j]>=d[i])
          move[i]=max(move[i],min(d[i]-d[j],l[i])+d[i]);

    printf("Case #%d: ",t);
    printf(*max_element(move.begin(),move.end())>=D?"YES\n":"NO\n");
  }
  return 0;
}
