//kbriut@yahoo.com
//GNU:Ming@Code:Blocks
#include<stdio.h>
#include<iostream>
using namespace std;
typedef long long LL;
LL i,j,n,t,mn,sum,xsum,txt;
int main(){
    //freopen("1.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    scanf("%lld",&t);
    while(t--){
        scanf("%lld",&n);
        sum=xsum=mn=0;
        for(i=1;i<=n;i++){
            cin>>j;
            sum+=j;
            if(mn>j||mn==0)mn=j;
            xsum^=j;
        }
        if(xsum)cout<<"Case #"<<++txt<<": NO"<<endl;
        else cout<<"Case #"<<++txt<<": "<<sum-mn<<endl;
    }
    return 0;
}
