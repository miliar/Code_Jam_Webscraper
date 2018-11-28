/**********************************************************************
Author: Felicia
Created Time:  2009/9/13 1:11:01
File Name: b.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

typedef long long int64;
const int maxint = 0x7FFFFFFF;
const int64 maxint64 = 0x7FFFFFFFFFFFFFFFLL;

char s[100];
int n;

int cnt[10];

bool decr(int p) {
    for (int i = p + 1; i <= n; ++i) {
        if (s[i] > s[i - 1])
            return false;
    }
    return true;
}

void calc() {
    n = strlen(s + 1);
    
    if (decr(1)) {
        memset(cnt, 0, sizeof(cnt));
        for (int i = 1; i <= n; ++i) {
            cnt[s[i] - '0']++;
        }
        for (int i = 1; i <= 9; ++i) {
            if (cnt[i] > 0) {
                cnt[i]--;
                s[0] = i + '0';
                break;
            }
        }
        for (int i = n; i >= 1; --i) {
            bool flag = false;
            for (int j = 9; j >= 1; --j) {
                if (cnt[j] > 0) {
                    flag = true;
                    cnt[j]--;
                    s[i] = j + '0';
                    break;
                }
            }
            if (!flag) {
                s[i] = '0';
            }
        }
        printf("%s\n", s);
        return;
    }
    
    for (int i = 2; i <= n; ++i) {
        if (decr(i)) {
            memset(cnt, 0, sizeof(cnt));
            for (int j = i - 1; j <= n; ++j) {
                cnt[s[j] - '0']++;
            }
            
            for (int j = s[i - 1] - '0' + 1; j <= 9; ++j) {
                if (cnt[j] > 0) {
                    cnt[j]--;
                    s[i - 1] = j + '0';
                    break;
                }
            }
            
            for (int j = n; j >= i; --j) {
                for (int k = 9; k >= 0; --k) {
                    if (cnt[k] > 0) {
                        cnt[k]--;
                        s[j] = k + '0';
                        break;
                    }
                }
            }
            
            break;
        }
    }
    
    printf("%s\n", s + 1);
}

int main() {
    freopen("b-large.out", "w", stdout);
    int ca;
    scanf("%d", &ca);
    for (int T = 1; T <= ca; ++T) {
        printf("Case #%d: ", T);
        s[0] = '0';
        scanf("%s", s + 1);
        calc();
    }
    return 0;
}

