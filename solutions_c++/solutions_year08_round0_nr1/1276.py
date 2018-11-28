/**********************************************************************
Author: WHU_GCC
Created Time: 2008年07月17日 星期四 21时51分08秒
File Name: gcj_a.cpp
Description: 
**********************************************************************/
#include <iostream>
#include <string>
using namespace std;
#define out(x) (cout << #x << ": " << x << endl)
const int maxint = 0x7FFFFFFF;
template <class T> void get_max(T &a, const T &b) {b > a ? a = b : 1;}
template <class T> void get_min(T &a, const T &b) {b < a ? a = b : 1;}

int S, N;
string se[110];
string qu[1100];

int f[1100][110];

int main() {
    int ca, c = 1;
    for (scanf("%d", &ca); ca--;) {
        printf("Case #%d: ", c++);

        char s[1000];        
        scanf("%d", &S);
        gets(s);
        for (int i = 1; i <= S; i++) {
            gets(s);
            se[i] = s;
        }
        scanf("%d", &N);
        gets(s);
        for (int i = 1; i <= N; i++) {
            gets(s);
            qu[i] = s;
        }
        
        memset(f, -1, sizeof(f));
        for (int i = 1; i <= S; i++)
            f[0][i] = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 1; j <= S; j++)
                if (f[i][j] != -1) {
                    for (int k = 1; k <= S; k++) {
                        if (qu[i + 1] != se[k]) {
                            if (f[i + 1][k] != -1)
                                get_min(f[i + 1][k], f[i][j] + (j != k));
                            else
                                f[i + 1][k] = f[i][j] + (j != k);
                        }
                    }
                }
        }
        int min = maxint;
        for (int i = 1; i <= S; i++)
            if (f[N][i] != -1)
                get_min(min, f[N][i]);
        printf("%d\n", min);
    }
    return 0;
}

