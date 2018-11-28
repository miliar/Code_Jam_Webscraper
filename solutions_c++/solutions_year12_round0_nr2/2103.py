#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <map>
using namespace std;
int ntest;
int n,S,p;
int a[4];
int f(int x){
    a[0] = x/3; x-=x/3;
    a[1] = x/2; 
    a[2] = x-x/2;
    if(a[2]>=p) return true;    
    if( (a[2]==a[1] && a[1] ) && a[2]+1 == p && S){
        S--;
        return true;
    }
    return 0;
}
int x;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&ntest);
    for(int t=0; t<ntest; t++){    
        scanf("%d %d %d",&n,&S,&p);
        int res=0;
        for(int i=0; i<n; i++){
            scanf("%d",&x);
            res+=f(x);
        }
        printf("Case #%d: %d\n",t+1,res);
    }
    return 0;
}
