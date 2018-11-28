#include<iostream>
#include<cstdio>
#include<string.h>
#include<string>
#include<math.h>
#include<algorithm>
using namespace std;

long long a[1000];
int b[1000];
int n;


int main(){
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%d",&a[i]);
        long long tmp1 = 0,tmp2 = 0;
        bool flag = 0;
        printf("Case #%d:\n",cas);
        for(int i=1;i<(3<<n);i++){
            int tmp = i;
            tmp1 = tmp2 = 0;
            memset(b,0,sizeof(b));
            int nn = 0;
            while(tmp){
                b[nn++] = tmp%3;
                tmp /= 3;
            }
            for(int j = 0;j<n;j ++){
                if(b[j]==1) tmp1 += a[j];
                else if(b[j]==2) tmp2 += a[j];
            }
            if(tmp1 == tmp2){
                for(int k = 0;k<n;k++) if(b[k]==1)
                    printf("%d ",a[k]);
                puts("");
                for(int k=0;k<n;k++) if(b[k]==2)
                    printf("%d ",a[k]);
                puts("");
                flag = 1;
                break;
            }
        }
        if(!flag) puts("Impossible");
    }
    return 0;
}
