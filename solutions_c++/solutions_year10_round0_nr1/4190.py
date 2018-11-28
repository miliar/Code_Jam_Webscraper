#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,k;

int main(){
    freopen("A-small.in","r",stdin);
    freopen("A-small.out","w",stdout);
    scanf("%d",&t);
    for (int o=1;o<=t;o++){
        scanf("%d%d",&n,&k);
        int base=1<<n;
        if (k%base==base-1) printf("Case #%d: ON\n",o);
            else printf("Case #%d: OFF\n",o);
    }
    return 0;
}
