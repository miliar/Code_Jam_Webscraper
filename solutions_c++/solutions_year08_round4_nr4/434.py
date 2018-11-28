#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define maxn 102400

int a[10];
char A[maxn],B[maxn];
int sz,k;
int done(){
    int t=1;
    for(int i=1;i<sz;i++)if(B[i]!=B[i-1])t++;
    return t;
}
int work(){
    scanf("%d",&k);scanf("%s",A);
    sz=strlen(A);
    int res=sz;
    for(int i=0;i<k;i++)a[i]=i;
    do{
       for(int i=0;i<sz;i+=k){
           for(int j=0;j<k;j++){
              B[i+j]=A[i+a[j]];
           }        
       }
       res=min(res,done());
    }while(next_permutation(a,a+k));
    return res;
}

int main(){
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int cases,k=1;
    scanf("%d",&cases);
    while(cases-->0){
         printf("Case #%d: %d\n",k++,work());
    }
    return 0;
}
