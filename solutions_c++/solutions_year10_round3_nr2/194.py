# include <iostream>
# include <vector>

using namespace std;

long long l, p, c;
int test;

int main() {
    scanf("%d", &test);
    for (int testId = 1; testId <= test; testId++) {
        scanf("%lld%lld%lld", &l, &p, &c);

        long long cnt = 0;
        for (; l < p; l *= c, cnt++) ;

        long long res = 0;
        long long power = 1;
        for (; power < cnt; power *= 2, res++) ;

        printf("Case #%d: %lld\n", testId, res);
    }

    return 0;
}