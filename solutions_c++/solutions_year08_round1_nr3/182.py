#include <iostream>
using namespace std;

// I used Windows Calculator to get this table:
int ans[32] = {
    0,
    0,
    27,
    143,
    751,
    935,
    607,
    903,
    991,
    335,
    47,
    943,
    471,
    55,
    447,
    463,
    991,
    95,
    607,
    263,
    151,
    855,
    527,
    743,
    351,
    135,
    407,
    903,
    791,
    135,
    647,
};
int cases, cas = 1, n;

int main() {
    for (scanf("%d", &cases); cases--; ) {
        scanf("%d", &n);
        printf("Case #%d: %03d\n", cas++, ans[n]);
    }
    return 0;
}
