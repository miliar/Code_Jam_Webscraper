#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main(){
    int t,n,s,p,a[105],cas=0;
 // freopen("B-large.in","r",stdin);
 // freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    while(t--){
        scanf("%d%d%d",&n,&s,&p); 
        int cnt=0;
        for(int i=1;i<=n;i++){
            scanf("%d",&a[i]);
            if(a[i]>=p*3-2)
               cnt++;
        }    
        for(int i=1;i<=n;i++){
            if(a[i]<p*3-2&&a[i]>=p*3-4&&s&&(p!=1)){
               cnt++;
               s--;
            }
        }
        printf("Case #%d: %d\n",++cas,cnt);
    }
    return 0;
}
        
         
