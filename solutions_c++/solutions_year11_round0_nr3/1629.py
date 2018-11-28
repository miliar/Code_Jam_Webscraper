#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#define oo 200000000
using namespace std;

void solve(int test){
    int n;
    scanf("%d",&n);
    long long a[n+1];
    for(int i=0;i<n;i++)scanf("%lld",&a[i]);
    sort(a,a+n);
    long long xorsum=0,sum=0;
    for(int i=0;i<n;i++){
        xorsum^=a[i];
        sum+=a[i];
    }
    if(xorsum!=0){
        printf("Case #%d: NO\n",test);
    }
    else printf("Case #%d: %lld\n",test,sum-a[0]);
}
void solve_slow(int test){
    int n;
    scanf("%d",&n);
    int a[n+5];
    for(int i=0;i<n;i++)scanf("%d",&a[i]);
    int mx=-1;
    for(int i=0;i< (1<<n);i++){
        int xorsum1=0,xorsum2=0,sum1=0,sum2=0;
        for(int j=0;j<n;j++){
            if( (i>>j)%2 ){
                xorsum1^=a[j];
                sum1+=a[j];
            }
            else{
                xorsum2^=a[j];
                sum2+=a[j];
            }
        }
        if(xorsum1==xorsum2&&sum1!=0&&sum2!=0){
            mx=max(mx,max(sum1,sum2));
        }
    }
    if(mx==-1)
    printf("Case #%d: NO\n",test);
    else printf("Case #%d: %d\n",test,mx);
}
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large2.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        solve(i);
        //solve_slow(i);
    }
}
