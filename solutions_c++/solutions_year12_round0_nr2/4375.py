#include <cstdio>
#include <algorithm>

using namespace std;

int data[239], n, s, p;
int flag[31][11];

void init() {
    for (int a = 0; a <= 10; ++a)
    for (int b = a; (b <= a+2) && (b <= 10); ++b)
    for (int c = b; (c <= a+2) && (c <= 10); ++c) {
        if (a + 2 > c) {
            for (int i = c; i >= 0; --i)
                flag[a + b + c][i] = 2;
        }
        else
            for (int i = c; i >= 0; --i)
                if (flag[a + b + c][i] == 0)
                    flag[a + b + c][i] = 1;
    }
}

void one_test(int test) {
    scanf("%d%d%d", &n, &s, &p);
    for (int i = 0; i < n; ++i)
        scanf("%d", &data[i]);
    sort(data, data + n);

    int res = 0;
    for (int i = 0; i < n; ++i)
        if (flag[data[i]][p] == 2)
            res++;
        else if (flag[data[i]][p] == 1 && s > 0) {
            res++;
            s--;
        }
    printf("Case #%d: %d\n", test, res);
}

int main() {
    int cases;

    init();

    scanf("%d", &cases);
    for (int i = 0; i < cases; ++i)
        one_test(i + 1);

    return 0;
}
