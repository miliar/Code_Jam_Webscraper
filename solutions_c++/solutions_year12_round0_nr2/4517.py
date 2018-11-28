#include "iostream"
#include "cstdio"
#include "cstring"
#include "algorithm"
#include "cmath"
#include "string"
using namespace std;
#define maxn 55
int num[maxn];
int val[maxn];
int ans[maxn][maxn][5];
int n, s, p, aans;
bool flag1, flag2;
void init() {
    memset(num, 0, sizeof(num));
    for(int i = 0; i <= 10; i++)
        for(int j = 0; j <= 10; j++)
            for(int k = 0; k <= 10; k++)
                if(abs(i-j) <= 2 && abs(i-k) <= 2 && abs(j-k) <=2) {
                    int t = i + j + k;
                    ans[t][num[t]][0] = i, ans[t][num[t]][1] = j, ans[t][num[t]][2] = k;
                    num[t]++;
                }
}

int main() {
    init();
    int T, Case = 1;
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> T;
    while(T--) {
        aans = 0;
        cin >> n >> s >> p;
        for(int i = 0; i < n; i++)
            cin >> val[i];
        sort(val, val + n);
        for(int i = 0; i < n; i++) {
            flag1 = flag2 = false;
            for(int j = 0; j < num[val[i]]; j++) {
                int p1 = ans[val[i]][j][0];
                int p2 = ans[val[i]][j][1];
                int p3 = ans[val[i]][j][2];
                int t = max(p1, max(p2, p3));
                if(t >= p) {
                    if((abs(p1-p2) == 2 || abs(p1-p3) == 2 || abs(p3-p2) ==2) && s > 0) flag1 = flag2 = true;
                    else if(abs(p1-p2) <= 1 && abs(p1-p3) <= 1 && abs(p2-p3) <= 1) {
                        flag1 = true;
                        flag2 = false;
                        break;
                    }
                }
            }
            if(flag1) {
                aans++;
                if(flag2) s--;
            }
        }
        printf("Case #%d: %d\n", Case++, aans);
    }
    return 0;
}
