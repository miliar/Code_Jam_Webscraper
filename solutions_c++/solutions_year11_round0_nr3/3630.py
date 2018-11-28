#include<iostream>
using namespace std;
int main(){
    freopen("C-large.in", "r",stdin);
    freopen("C-large.out", "w",stdout);
    int t,n,i,arr[10000];
    int sol,t1=1,min,sum;
    scanf("%d",&t);
    while(t--){
               sum=0;
               scanf("%d",&n);
               for(i=0;i<n;i++){
                               scanf("%d",&arr[i]);
                               sum+=arr[i];
                               if(!i) min=arr[i];
                               else min>arr[i]?min=arr[i]:min=min;
                               }
               sol=arr[0];
    for(i=1;i<n;i++) sol^=arr[i];
    if(sol) printf("Case #%d: NO\n",t1++);
    else{
         printf("Case #%d: %d\n",t1++,sum-min);
         }
    }
    getchar();
    getchar();
    return 0;
}
