#include<cstdio>
#include<algorithm>
using namespace std;

int t;
int n, k;

int main(){
  freopen("A-large.in", "r", stdin);
  freopen("out.out", "w", stdout);
    
    scanf("%d", &t);
    for(int i=1; i<=t; ++i){
        scanf("%d%d", &n, &k);
        
        int workTimes=1;
        for(int j=1; j<=n; ++j)
            workTimes*=2;
        /*
        printf("k=%d, n=%d, workTimes=%d\n", k, n, workTimes);
        if((k+1)%workTimes==0) printf("workTimes pass\n");
        if(k>=workTimes-1) printf("k greater than workTimes\n");
        if(k%2!=0) printf("have power\n");*/
        
        
        if((k+1)%workTimes==0&& k>=workTimes-1 && k%2!=0)
            printf("Case #%d: ON\n", i);
        else
            printf("Case #%d: OFF\n", i);
    }
    return 0;
}
