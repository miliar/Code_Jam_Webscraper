#include <algorithm>
#include <iostream>
using namespace std;

void
solve(int cases)
{
    char N[32];
    int i, j, k;
    int prev;

    // read
    N[0] = '0';
    gets(&N[1]);

    // solve
    prev = N[strlen(N) - 1];
    for (i = strlen(N) - 2; i >= 0; i--) {
        if (N[i] < prev) break;
        prev = N[i];
    }
//printf("%s i=%d\n", N, i);
    k = N[i];
    sort(&N[i], &N[strlen(N)]);

    for (j = i + 1; j < strlen(N); j++) {
        if (N[j] > k) {
            k = N[j];
            break;
        }
    }
//printf("%s j=%d\n", N, j);
    memmove(&N[i + 1], &N[i], j - i);
//printf("%s\n", N);
    N[i] = k;

    // output result
    if (N[0] == '0') strcpy(N, N+1);
    cout << "Case #" << cases << ": " << N << endl;
}

int
main()
{
    int N, i;

    cin >> N;
    (void)getchar();
    for (i = 0; i < N; i++) {
        solve(i + 1);
    }

}
