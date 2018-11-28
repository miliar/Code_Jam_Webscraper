#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
const int MOD = 100003;
int table[26] = {
    0,0,1,2,3,5,8,14,24,43,77,140,256,472,874,1628,3045,5719,10780,20388,38674,73562,40265,68060,13335,84884
};
int n;

int main() {
    int tt, cas=1;
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small.out","w", stdout);
    scanf("%d",&tt);
    while(tt--) {
        scanf("%d",&n); 
        int ans=table[n];
        printf("Case #%d: %d\n",cas++,ans%MOD);
    }
    //system("pause");
    return 0;
}
