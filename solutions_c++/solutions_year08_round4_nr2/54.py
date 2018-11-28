#include <iostream>
#include <cmath>
using namespace std;
bool ok[100000000];
int main() {
        int T;scanf("%d",&T);for (int t=1; t<=T; t++) {
            int A,N,M;scanf("%d %d %d",&N,&M,&A);
            for (int i=0; i<=N*M; i++) ok[i]=false;
            for (int i=0; i<=N; i++)
            for (int j=0; j<=M; j++) {
                int tmp = i*j;
                ok[tmp]=true;
                if (tmp>=A && ok[tmp-A]) {
                    int k,l;
                    if (tmp-A==0) k=l=0;
                    else
                    for (k=1; k<=N; k++) {
                        if ((tmp-A)%k!=0) continue;
                        l=(tmp-A)/k;
                        if (l>M) continue;
                        break;
                    }
                    printf("Case #%d: 0 0 %d %d %d %d\n",t,i,l,k,j);
                    goto next;
                }   
            }
            printf("Case #%d: IMPOSSIBLE\n",t);
            next:;
        }
}
