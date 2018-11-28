#include <iostream>
#include <cmath>
using namespace std;
int vals[20000];
int change[20000];
int minfor[20000][2];
int M;
int main() {
        int T;scanf("%d",&T);for (int t=1; t<=T; t++) {
            int V;scanf("%d %d",&M,&V);
            for (int i=1; i<=M; i++) {
                if (2*i>=M) {
                    scanf("%d",&vals[i]);
                } else {
                    scanf("%d %d",&vals[i],&change[i]);
                }
            }
            for (int i=M; i>=1; i--)
            for (int j=0; j<=1; j++) {
                if (2*i>=M) {
                    if (vals[i]==j) minfor[i][j]=0;
                    else minfor[i][j]=10000000;
                } else {
                    if (vals[i]==0) {
                        // or gate
                        minfor[i][0]=min(!change[i]?10000000:1+min(minfor[2*i][0],minfor[2*i+1][0]),minfor[2*i][0]+minfor[2*i+1][0]);
                        minfor[i][1]=min(minfor[2*i][1],minfor[2*i+1][1]);
                    } else if (vals[i]==1) {
                        minfor[i][0]=min(minfor[2*i][0],minfor[2*i+1][0]);
                        minfor[i][1]=min(minfor[2*i][1]+minfor[2*i+1][1],!change[i]?10000000:1+min(minfor[2*i][1],minfor[2*i+1][1]));
                    }
                }
            }
            printf("Case #%d: ",t);
            if (minfor[1][V]<10000000) printf("%d\n",minfor[1][V]);
            else printf("IMPOSSIBLE\n");
        }
}
