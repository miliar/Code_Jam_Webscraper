#include <iostream>
using namespace std;
/*
const char* double_check(int y, int x, int a, int b, int len)
{
        int p[] = {10, 100, 1000, 10000, 100000, 1000000};

        bool result = (x < y); 
        result = result && (a <= x) && (y <= b);
        if (result)
                for (int i = 0; i <= len - 1; i++) {
                        int t = x % p[i];
                        int left = len - i;
                        t = t * p[left - 1];
                        t = t + x / p[i];
                        if (t == y)
                                return "Pass";
                }
        return "Failed";
}
*/
void split(int num, int digits[], int &len)
{
        len = -1;
        while (num) {
                digits[++len] = num % 10;
                num /= 10;
        }

        int i = 0, j = len;
        while (i < j) {
                int t = digits[i];
                digits[i] = digits[j];
                digits[j] = t;
                ++i, --j;
        }
}

int join(int pos, int digits[], int len)
{
        int result = 0;
        for (int i = pos + 1; i <= len; i++)
                result = result * 10 + digits[i];
        for (int i = 0; i <= pos; i++)
                result = result * 10 + digits[i];
        return result;
}

bool exist(int p, int num[], int tot)
{
        for (int i = 0; i < tot; i++)
                if (num[i] == p)
                        return true;
        return false;
}

int main(void)
{
        int T;
        cin >> T;
        for (int i = 1; i <= T; i++) {
                int ans = 0;
                int a, b;
                scanf("%d%d", &a, &b);

                for (int k = a; k <= b; k++) {
                        int num[10], len;
                        int result[10], tot = 0;
                        split(k, num, len);

                        int fr;
                        fr = 0;
                        while (fr + 1 <= len) {
                                if (num[fr + 1]) {
                                        int rk = join(fr, num, len);
                                        if (rk < k && a <= rk && !exist(rk, result, tot)) {
                                                result[tot++] = rk;
                                                ++ans;
                                                // printf("%d %d\n", k, rk);
                                                // printf("%s\n", double_check(k, rk, a, b, len));
                                        }
                                }
                                ++fr;
                        }
                }

                cout << "Case #" << i << ": " << ans << endl;
        }
        return 0;
}
