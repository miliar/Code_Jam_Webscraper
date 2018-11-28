#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;
int N;
int v[1024];

int C[1024],Q;

int sol(){
    int i,j,k;
    scanf("%d",&N);    
    for (i=0;i<N;i++) scanf("%d",v+i);
    sort(v,v+N);
    if (N==0){
        return 0;
    }
    k=v[0]; C[0]=1; Q=0;
    for (i=1;i<N;i++){
        if (k==v[i]){
            C[Q]++;
        }else if (k==v[i]-1){
            k=v[i];
            C[++Q]=1;
        }else{
            C[++Q]=0;
            k=v[i];
            C[++Q]=1;
        }
    }
    C[++Q]=0;
    Q++;
    int r = N;
    while (1){
        for (i=0;i<Q;i++){
            if (C[i]!=0) break;
        }
        if (i==Q) break;
        for (k=i;k<Q;k++) if (C[k]>C[k+1]) break;
        for (j=i;j<=k;j++) C[j]--;
        if (k-i+1<r) r=k-i+1;
    }
    return r;
}

int main(){
    int t,cas;
    scanf("%d",&t);
    for (cas=1;cas<=t;cas++)
        printf("Case #%d: %d\n",cas,sol());
    return 0;
}

