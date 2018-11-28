#include<cstdio>
#include<algorithm>
using namespace std;
int t,n,a[1005],tmp,ac;
int gcd(int x,int y){
    if (x%y==0) return y;
    else return gcd(y,x%y);   
}
int main(){
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-output-small.out","w",stdout);
    scanf("%d",&t);
    for (int tt=1; tt<=t; tt++){
        scanf("%d",&n);
        for (int i=1; i<=n; i++)
            scanf("%d",&a[i]);
        sort(a+1,a+n+1);
        if (n==3){
           if (a[1]==a[2]&&a[2]==a[3]) ac=0;
           else if (a[1]==a[2]) a[2]=a[3],n=2;
           else if (a[2]==a[3]) n=2;
           else{
                tmp=gcd(a[2]-a[1],a[3]-a[2]);
                ac=a[3]%tmp;
                ac=(tmp-ac)%tmp;  
           }       
        }
        if (n==2){
           tmp=a[2]-a[1];
           ac=a[2]%tmp;
           ac=(tmp-ac)%tmp;          
        }
        printf("Case #%d: %d\n",tt,ac);
    }
    return 0;    
}
