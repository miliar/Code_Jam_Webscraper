#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define Base 100003
using namespace std;
int ntest,n;
typedef long long ll;
ll g[501][501],sum[501][501],F[501][501];
ll cal(int x,int y){
    if (!x) return 1;
    return sum[x][y];
}

int main(){
    freopen("C-large.in","r",stdin);
    freopen("test.out","w",stdout);    
    for(int i = 1; i <= 500; i++){
        g[1][i] = 1;
        sum[1][i] = sum[1][i-1] + 1;
    }
    for(int i = 2; i <= 500; i++) for(int j = 1; j <= 500; j++){
        g[i][j] = sum[i-1][j-1];
        sum[i][j] = (sum[i][j-1] + g[i][j]) % Base;
    }
    for(int i = 1; i <= 500 ; i++){
        F[i][1] = 1;
        for(int j = 2; j <= i-1; j++)
        for(int k = j-1; k >= 1; k--)
        F[i][j] = (F[i][j] + F[j][k] * cal(j-k-1,i-j-1)) % Base;
    }    
    scanf("%d",&ntest);
    for(int test=0; test<ntest; test++){
        printf("Case #%d: ",test+1);     
        scanf("%d",&n);
        ll res = 0;
        for(int i = 1; i<= n;i++)
            res = (res + F[n][i]) % Base;
        printf("%lld\n",res);
    }
    return 0;
}
