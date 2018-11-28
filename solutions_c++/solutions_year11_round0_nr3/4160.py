#include<iostream>
using namespace std;

int a[1005];
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C.ans","w",stdout);
    int t,cs = 1;
    cin>>t;
    while(t--){
        int n,i,r = 0,sum = 0;
        cin>>n;
        for(i = 0;i<n;i++){
              cin>>a[i];
              r^=a[i];
              sum+=a[i];
        }
        sort(a,a+n);
        sum-=a[0];
        if(r==0)
                printf("Case #%d: %d\n",cs++,sum);
        else printf("Case #%d: NO\n",cs++);
    }
}
