#include <iostream>

using namespace std;
int a[1002],n;
int ntest;
long long R,K;
int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&ntest);
    for(int t=0; t<ntest; t++){
        printf("Case #%d: ",t+1);
        scanf("%lld %lld",&R,&K);
        long long res=0;
        scanf("%d",&n);
        for(int i=0; i<n; i++) scanf("%d",&a[i]);
        if(R<=1000000){
            int i=0;
            for(int c=0; c<R; c++){
                int j=0;
                int temp=0;
                while(temp+a[(i+j)%n]<=K && j<n){
                    temp+=a[(i+j)%n];
                    j++;
                }
                i=(i+j)%n;
                res += 1LL*temp;
            }
        }
        else{
            int i=0, count=0;
            do{
                count++;
                int j=0;
                int temp=0;
                while(temp+a[(i+j)%n]<=K && j<n){
                    temp+=a[(i+j)%n];
                    j++;
                }
                i=(i+j)%n;
                res += 1LL*temp;
            }while(i!=0 && count<R);        
            
            res = (R/count)*1LL*res;
            R%=count;
            i=0;
            for(int c=0; c<R; c++){
                int j=0;
                int temp=0;
                while(temp+a[(i+j)%n]<=K && j<n){
                    temp+=a[(i+j)%n];
                    j++;
                }
                i=(i+j)%n;
                res += 1LL*temp;
            }
        }
        printf("%lld\n",res);
    }
    return 0;
}
