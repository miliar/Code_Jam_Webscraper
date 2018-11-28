#include <iostream>
#include <cstdio>

using namespace std;

int n;
int ans[100];
void run(){
     printf("%d\n",ans[n]);
}

int main(){
    int t;
    ans[2] = 1;
ans[3] = 2;
ans[4] = 3;
ans[5] = 5;
ans[6] = 8;
ans[7] = 14;
ans[8] = 24;
ans[9] = 43;
ans[10] = 77;
ans[11] = 140;
ans[12] = 256;
ans[13] = 472;
ans[14] = 874;
ans[15] = 1628;
ans[16] = 3045;
ans[17] = 5719;
ans[18] = 10780;
ans[19] = 20388;
ans[20] = 38674;
ans[21] = 73562;
ans[22] = 40265;
ans[23] = 68060;
ans[24] = 13335;
ans[25] = 84884;

    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d",&t);
    for (int i = 1; i <= t; ++i){
        printf("Case #%d: ", i);
        scanf("%d",&n);
        run();
    }
    return 0;
}

