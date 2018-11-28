#include<iostream>
#include<stdio.h>
#include<map>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<string>
#include<math.h>
using namespace std;

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("outC.txt","w",stdout);
    int t,N,L,H,i,j,k,a[110];
    scanf("%d",&t);
    for(k=1;k<=t;k++) {
        scanf("%d%d%d",&N,&L,&H);
        for(i=0;i<N;i++) scanf("%d",&a[i]);
        printf("Case #%d: ",k);
        for(i=L;i<=H;i++) {
            for(j=0;j<N;j++) {
                if(i%a[j]==0||a[j]%i==0) continue;
                else break;
            }
            if(j==N) {
                printf("%d\n",i);
                break;
            }
        }
        if(i>H) printf("NO\n");
    }
    return 0;
}
