#include <iostream>
#include <cstdio>
using namespace std;
const int N = 200;
int t[N],n,s,p;
int main(){
     // freopen("test.in","r",stdin);
      //freopen("test.out","w",stdout);
      int T;scanf("%d",&T);
      for (int k=1;k<=T;k++){
            scanf("%d%d%d",&n,&s,&p);
            int cnt = 0;
            for (int i=1;i<=n;i++){
                  scanf("%d",&t[i]);
                  if (t[i]>=3*p-2) cnt++;
            }
            for (int i=1;i<=n;i++){
                  if (t[i]>=3*p-4 && t[i]<3*p-2 && s>0){
                        if (p==0){
                              cnt++;
                              s--;
                        } else {
                              if (t[i] == 0) continue;
                              else {
                                    cnt++;
                                    s--;
                              }
                        }
                  }
            }
            printf("Case #%d: %d\n",k,cnt);
      }
      return 0;
}
