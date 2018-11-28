#include <stdio.h>
#include <algorithm>

using namespace std;

const int maxn = 1024;

int id[maxn],P[maxn],L[maxn];
int N;

bool cmp(int i,int j){
    int a,b;
    a = L[i]*P[j];
    b = L[j]*P[i];
    if (a==b) return i<j;
    else return a<b;
}

void sol(int cas){
    int i,j,k;
    scanf("%d",&N);
    for (i=0;i<N;i++) scanf("%d",L+i);
    for (i=0;i<N;i++) scanf("%d",P+i);
    for (i=0;i<N;i++) id[i]=i;
    sort(id,id+N,cmp);
    printf("Case #%d:",cas);
    for (i=0;i<N;i++) printf(" %d",id[i]);
    printf("\n");
}

int main(){
    int cas,T;
    scanf("%d",&T);
    for (cas=1;cas<=T;cas++)sol(cas);
    return 0;
}

