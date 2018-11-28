#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <complex>
#define MAXN 10005
using namespace std;
int num[MAXN];
int main(){
    int T;
    int N,L,R;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("csmall.txt","w",stdout);
    scanf("%d",&T);
    for(int k=1;k<=T;k++){
        scanf("%d%d%d",&N,&L,&R);
        for(int i=0;i<N;i++){
            scanf("%d",&num[i]);
        }
        printf("Case #%d: ",k);
        bool ff=false;
        for(int s=L;s<=R;s++){
            bool flag=true;
            for(int i=0;i<N;i++){
                if(num[i]%s!=0 && s%num[i]!=0){
                    flag=false;
                    break;
                }
            }
            if(flag){
                ff=true;
                printf("%d\n",s);
                break;
            }
        }
        if(!ff)printf("NO\n");
    }
    return 0;
}
