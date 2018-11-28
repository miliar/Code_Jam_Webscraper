#include<iostream>
#include<string.h>
#include<stdio.h>
#include<math.h>
using namespace std;

int main() {
    FILE* f;
    f = fopen("PA.txt", "w");
    int T, A, B;
    int i, j, Count = 1;
    double p[100000], total, keep, enter, back, ans, tmp;
    cin >> T;
    while(T--) {
        cin >> A >> B;
        total = 1;
        for(i = 1;i <= A;i++) {
            cin >> p[i];
            total *= p[i];
        }
        keep = (B - A + 1) * total + ((B - A + 1) + (B + 1)) * (1 - total);
        enter = 1 + B + 1;
        ans = min(keep, enter);
        tmp = total;
        for(i = 1;i < A;i++) {
            tmp = tmp / p[A - i + 1];
            back = ((2 * i) + (B - A + 1)) * tmp + ((2 * i) + (B - A + 1) + B + 1) * (1 - tmp);
            ans = min(ans, back);
        }
        printf("Case #%d: %.6f\n", Count, ans);
        fprintf(f, "Case #%d: %.6f\n", Count++, ans);
    }
}
