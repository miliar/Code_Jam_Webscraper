#include <cstdio>
#include <cstring>

char text[1024];
char pattern[] = " welcome to code jam";
int LP, N;
int A[32];

int main()
{
    int i, j, k, t;
    scanf ("%d\n", &N);
    LP = strlen(pattern);
    for (t = 1; t <= N; t++) {
        fgets(text, 1024, stdin);
        memset(A, 0, sizeof(A));
        A[0] = 1;
        for (i = 0; text[i]; i++)
        for (j = LP - 1; j > 0; j--)
            if (text[i] == pattern[j]) {
                A[j] += A[j - 1];
                A[j] %= 10000;
            }
        printf ("Case #%d: %04d\n", t, A[LP - 1]);
    }
    return 0;
}
