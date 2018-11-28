#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int n;
char str[50];
long long mat[50];
long long up[50];

int solve() {
    up[0] = 0;
    int ans = 0;
    for(int i = 1;i <= n;++i) {
        for(int j = i - 1;j < n;++j) {
            if( mat[j] < up[i]) {
                while(j != i - 1) {
                    if(j < i - 1) {
                        swap(mat[j],mat[j + 1]);
                        j++;
                    }
                    else {
                        swap(mat[j],mat[j - 1]);
                        j--;
                    }
                    ans++;
                }
                break;
            }
        }
    }
    return ans;
}

int main() {
   // freopen("data.in","r",stdin);
    freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    int cas = 1;
    while(T--) {
        scanf("%d",&n);
        for(int i = 0;i < n;++i) {
            scanf("%s",str);
            mat[i] = 0;
            up[i + 1] = (long long)powl(2,i + 1);
            for(int j = 0;j < n;++j) {
                mat[i] += ((1LL)<<(j)) * (str[j] - '0');
            }
        }
        printf("Case #%d: %d\n",cas++,solve());
    }
    return 0;
}
