#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
const double PI = acos(-1.0);
const int maxn=505,mod=100003;
typedef long long LL;

LL C[maxn][maxn],f[maxn][maxn];

int main() {
    //freopen("C-small-attempt0.in", "r", stdin);
    //freopen("C-small-attempt0.out", "w", stdout);
    freopen("C-large.in", "r", stdin);
    freopen("C-large2.out", "w", stdout);
    
    for(int i=0;i<maxn;i++){
        C[i][0]=1;
        for(int j=1;j<=i;j++)
            C[i][j]=(C[i-1][j-1]+C[i-1][j])%mod;
    }
    for(int i=2;i<maxn;i++){
        f[i][1]=1;
        for(int j=2;j<i;j++){
            f[i][j]=0;
            for(int k=0;k<=j-2;k++){
                f[i][j]=(f[i][j]+f[j][j-k-1]*C[i-j-1][k])%mod;
            }
        }
    }
    int Tn;
    scanf("%d", &Tn);
    for (int T = 1; T <= Tn; T++) {
        int n;
    	scanf("%d",&n);
    	printf("Case #%d: ", T);
    	LL ans=0;
    	for(int i=1;i<n;i++)
            ans=(ans+f[n][i])%mod;
    	printf("%I64d\n",ans);
    }
	return 0;
}
