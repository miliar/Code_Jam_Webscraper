#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
using namespace std;
void base_conv(int s, int b, char* buf)
{
    int i;
    i = 0;
    while (s) {
        buf[i++] = (s % b) + '0';
        s /= b;
    }
    buf[i] = 0;
}
int main()
{
    int tc, cn;
    int i, j, k;
    int n;
    int base[10];
    int res, fl, temp;
    int len;
    char buf[100];
    char* ptr;
    scanf("%d", &tc);
    gets(buf);
    for (cn = 1; cn <= tc; cn++) {
        gets(buf);
        n = 0;
        ptr = strtok(buf, " ");
        while (ptr != NULL) {
            base[n] = atoi(ptr);
            n++;
            ptr = strtok(NULL, " ");
        }
        for (res = 2; ; res++) {
            for (i = 0; i < n; i++) {
                set<int> st;
                fl = 0;
                temp = res;
                while (1) {
//printf("temp = %d\n", temp);
                    if (temp == 1) {
                        fl = 1;
                        break;
                    }
                    if (st.find(temp) != st.end()) {
                        break;
                    }
                    st.insert(temp);
                    base_conv(temp, base[i], buf);
                    len = strlen(buf);
                    temp = 0;
                    for (j = 0; j < len; j++) {
                        temp += (buf[j]-'0')  * (buf[j]-'0');
                    }
                }
                if (!fl)
                    break;
//printf("%d is happy on base %d\n", res, base[i]);
            }
            if (i == n) {
                break;
            }
        }
        printf("Case #%d: %d\n", cn, res);
    }
    return 0;
}
