#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>

using namespace std;
int t;
double n,pg,pd;
int main(int argc, char** argv) {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    for(int i = 1;i <=t; ++i){
        scanf("%lf%lf%lf",&n,&pd,&pg);
        bool flag = true;int j;
        for(j = 1;j <= n; ++j) if((int)(pd * j) % 100 == 0){
            flag = true;break;
        }
        if(j == n + 1) flag = false;
        if(pg > n * pd) flag = false;
        if(pg == 100 && pd < 100) flag = false;
        if(pg == 0 && pd > 0) flag = false;
        if(flag)
            printf("Case #%d: Possible\n",i);
        else
            printf("Case #%d: Broken\n",i);
    }
    return 0;
}

