#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

int tn,n;
int a[810],b[810];

int comp1(const void* l,const void *r){
    return *(int*)l-*(int*)r;
}

int comp2(const void* l,const void *r){
    return *(int*)r-*(int*)l;
}

int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int i,j;
    int cn =1;
    scanf("%d",&tn);
    while(tn--){
        scanf("%d",&n);
        for(i=0;i<n;i++) scanf("%d",&a[i]);
        for(i=0;i<n;i++) scanf("%d",&b[i]);
        qsort(a,n,sizeof(int),comp1);
        qsort(b,n,sizeof(int),comp2);
        __int64 sum = 0;
        for(i=0;i<n;i++) sum+=a[i]*b[i];
        printf("Case #%d: %I64d\n",cn,sum);
        cn++;
    }
    return 0;
}

