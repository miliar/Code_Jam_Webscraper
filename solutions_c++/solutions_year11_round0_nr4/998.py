#include <cstdio>

using namespace std;

int main()
{
    int n; scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int a; scanf("%d", &a);
        int count = 0;
        for (int j = 1; j < a + 1; j++) {
            int b; scanf("%d", &b);
            if (b != j) {
                count++;
            }
        }
        double h = count;
        printf("Case #%d: %f\n", (i + 1), h);
    }   
    return 0;
}
