#include<iostream>
#include<string>
#include<algorithm>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

bool gt(int a, int b) {
    return a > b;
}

int main() {
    FILE* f = fopen("PB.txt", "w");
    int i, count = 1;
    int T, N, S, P, a[100], best[100], ans;

    cin >> T;
    while(T--) {
        cin >> N >> S >> P;
        
        for(i = 0;i < N;i++) {
            cin >> a[i];
        }
        
        sort(a, a + N, gt);
        
        for(i = 0;i < N;i++) {
            best[i] = a[i] / 3;
            if(a[i] % 3) best[i] += 1;
        }
        
        ans = 0;
        
        for(i = 0;i < N;i++) {
            if(best[i] >= P) ans++;
            if(best[i] == P - 1 && S > 0 && a[i] < 29 && a[i] > 1 && (a[i] % 3 != 1)) {
                S--;
                ans++;
            }
        }
        
        cout << "Case #" << count << ": " << ans << endl;
        fprintf(f, "Case #%d: %d\n", count++, ans);
    }
}
