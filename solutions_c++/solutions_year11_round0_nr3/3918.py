#include <iostream>
#include <cstdio>

using namespace std;

int main(){
    long long res,min,t,n,c[1005],a,b;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    cin >> t;

    for(int i=1;i<=t;i++){
        cin >> n;
        a=0;
        res=0;
        min=1000080;
        for(int j=1;j<=n;j++){
            cin >> c[j];
            if(min>c[j]) min=c[j];
            a=(a xor c[j]);
            res+=c[j];
        }

        if(a==0){
            b=res-min;
            printf("Case #%d: %d\n",i,b);
        }
        else{
            printf("Case #%d: NO\n",i);
        }
    }
}
