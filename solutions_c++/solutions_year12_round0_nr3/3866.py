#include <algorithm>
#include <iostream>
#include <string>
#include <string.h>
#include <cstdio>

using namespace std;

const int MAXN = 10000010;

int fac[100];

bool used[MAXN];

void init(){
    fac[0] = 1;
    for (int i = 1; i <= 9; i++){
        fac[i] = fac[i - 1] * 10;
    }
}

int main(){
    int t, A, B, ans;
    init();
    freopen("C.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    for (int i = 1; i <= t; i++){
        ans = 0;
        scanf("%d%d", &A, &B);
        memset(used, false, sizeof(used));
        for (int j = A; j <= B; j++){
            if (used[j]) continue;
            bool flag = true;
            int digit = 0, temp = j, cnt = 0, cur;
            while (temp){
                digit++;
                temp /= 10;
            }

            temp = j;
            while (!used[temp]){
                used[temp] = true;
                if (flag && temp >= A && temp <= B){
                    cnt++;
                }
                int t1 = temp % 10;
                temp /= 10;
                if (t1 != 0){
                    temp += t1 * fac[digit - 1];
                    flag = true;
                }else{
                    flag = false;
                }
            }
            ans += cnt * (cnt - 1) / 2;
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
}
/*
int main(){
    int t, n, p, s;
    freopen("B.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    for (int i = 1; i <= t; i++){
        scanf("%d%d%d", &n, &p, &s);
        for (int j = 0; j < n; j++){
            scanf("%d", &array[j]);
        }
        sort(array, array + n);
        int ans = 0;
        for (int j = 0; j < n; j++){
            int t1 = array[j] / 3;
            int t2 = t1;
            if (array[j] % 3 == 2){
                t1++, t2++;
            }
            if (array[j] % 3 == 1){
                t1++;
            }
            if (t1 >= s){
                ans++;
                continue;
            }
            if (t1 + 1 >= s && p > 0 && t2 > 0){
                ans++;
                p--;
            }
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}
*/
