#include<iostream>
#include<string>
#include<algorithm>
#include<map>
#include<memory>
#include<vector>
#include<set>
#include<cstdio>

using namespace std;

bool findsol(int w, int h, int A) {
    for(int i=1; i<=w; i++) {
        if(A % i == 0 && A / i <= h) {
            printf("0 0 %d %d %d %d\n", w, A/i, i, h);
            return true;
        }
    }
    return false;
}

int main() {
    int t, m, n, a;
    cin >> t;
    for(int c=1; c<=t; c++) {
        cin >> n >> m >> a;
        printf("Case #%d: ", c);
        for(int w=1; w<=n; w++) {
            for(int h=m; h>0; h--) {
                int A = w*h - a;
                if(A < 0) break;
                if(A == 0) {
                    printf("0 0 0 %d %d 0\n", h, w);
                    goto END;
                }
                else if(findsol(w, h, A)) goto END;
            }
        }
        printf("IMPOSSIBLE\n");
        END:;
    }
}
