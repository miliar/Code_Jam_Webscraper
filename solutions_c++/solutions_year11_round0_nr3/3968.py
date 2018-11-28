#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

#define IN freopen("C-small-attempt0.in","r",stdin);
#define OUT freopen("C.out","w",stdout);

#define SIZE 1010

int candy[SIZE],T,N,ans;

int main(){
    IN
    OUT
    int i,j,t,tmp,Sean,Patrick;
    scanf("%d",&T);
    for(t=1;t<=T;t++){

        scanf("%d",&N);
        for(i=0;i<N;i++){
            scanf("%d",&candy[i]);
        }

        ans = 0;
        int sum;
        for(i=0;i<(1<<N);i++){
            tmp = i;
            sum = Sean = Patrick = 0;
            for(j=0;j<N;j++){
                if(tmp & 1) Patrick ^= candy[j];

                else {
                    Sean ^= candy[j];
                    sum += candy[j];
                }
                tmp >>= 1;
            }
            if(Sean == Patrick && Sean!=0){
                if(sum > ans) ans = sum;
            }
        }
        printf("Case #%d: ",t);
        if(ans) printf("%d\n",ans);
        else printf("NO\n");
    }
    return 0;
}
