#include <iostream>

using namespace std;

int v1[900];
int v2[900];

int cmp1( const void *a,const void *b ){
    return *(int*)a - *(int*)b;
}
int cmp2( const void *a,const void *b ){
    return *(int*)b - *(int*)a;
}

int main(){
    freopen("a.in","r",stdin);
    freopen("a.txt","w",stdout);
    int i,j,t;
    scanf("%d",&t);
    
    for( i=1;i<=t;i++ ){
        int n;
        scanf("%d",&n); 
        for( j=0;j<n;j++ ) scanf("%d",v1+j);
        for( j=0;j<n;j++ ) scanf("%d",v2+j); 
        qsort( &v1[0],n,sizeof(int),cmp1 ); 
        qsort( &v2[0],n,sizeof(int),cmp2 );
        __int64 ans = 0;
        for( j=0;j<n;j++ ){
            ans += v1[j]*v2[j]; 
        }
        printf("Case #%d: %I64d\n",i,ans);
    }
    
    
    
    return 0;
}
