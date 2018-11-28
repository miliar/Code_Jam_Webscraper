#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define llong long long
#define maxn 1024

int n;
int A[maxn],B[maxn];

int main(){
    //freopen("data.in","r",stdin);
    //freopen("data.out","w",stdout);
    int cases;
    scanf("%d",&cases);
    int k=1;
    while(cases-->0){
       scanf("%d",&n);
       for(int i=0;i<n;i++)scanf("%d",&A[i]);
       for(int i=0;i<n;i++)scanf("%d",&B[i]);
       sort(A,A+n);
       sort(B,B+n);
       reverse(B,B+n);
       llong res=0;
       for(int i=0;i<n;i++)res+=A[i]*B[i];
       printf("Case #%d: %I64d\n",k++,res);
    }
    return 0;
}
