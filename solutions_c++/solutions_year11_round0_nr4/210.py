#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int debug = 1;
    if( debug ){
        freopen("D-large.in","r",stdin);
        freopen("D-large.out","w",stdout);
    }
    int Cas, n, a;
    scanf("%d",&Cas);
    for(int cas=1; cas<=Cas; ++cas){
        scanf("%d",&n);
        int res = 0;
        for(int i=1; i<=n; i++){
            scanf("%d",&a);
            if( a!=i ) res++;
        }
        printf("Case #%d: %.6f\n",cas,1.0*res);
    }
    if( debug ){
        fclose(stdin);
        fclose(stdout);
    }
    return 0;
}
