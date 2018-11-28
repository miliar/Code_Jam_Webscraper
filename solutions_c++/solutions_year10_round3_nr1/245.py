# include <iostream>

using namespace std;

const int MaxN = 1005;

int n;
int H1[MaxN];
int H2[MaxN];

int test;

int main() {
    scanf("%d", &test);
    for (int testId = 1; testId <= test; testId++) {
        scanf("%d", &n);
        int res = 0;
        for (int i = 0; i < n; i++) {
            scanf("%d%d", &H1[i], &H2[i]);
            for (int j = 0; j < i; j++)
                if ((H1[i] < H1[j]) != (H2[i] < H2[j]))
                    res++;
        }

        printf("Case #%d: %d\n", testId, res);
    }

    return 0;
}