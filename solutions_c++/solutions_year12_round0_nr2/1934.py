#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int ntest,n,s,p,arr[120],ret;
    scanf("%d",&ntest);
    for (int test=1;test<=ntest;++test){
        scanf("%d %d %d",&n,&s,&p);
        for (int i=0;i<n;++i){
            scanf("%d",&arr[i]);
        }
        sort(arr,arr+n);
        ret=0;
        for (int i=n-1;i>=0;--i){
            if (arr[i]/3>=p) ret++;
            else if (arr[i]/3==p-1 && arr[i]%3>0) ret++;
            else if (arr[i]/3==p-1 && arr[i]%3==0 && arr[i]>0 && s>0){ ret++; s--;}
            else if (arr[i]/3==p-2 && arr[i]%3==2 && arr[i]>0 && s>0){ ret++; s--;}
            else break;
        }
        printf("Case #%d: %d\n",test,ret);
    }
    return 0;
}
