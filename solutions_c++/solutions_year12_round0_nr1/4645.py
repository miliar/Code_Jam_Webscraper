#include <cstdio>
#include <cstring>

char h[27] = "yhesocvxduiglbkrztnwjpfmaq";
char a[1024];

int T, n;
int main() {
    freopen ("a.in", "r", stdin);
    freopen ("a.out", "w", stdout);
    scanf ("%d\n", &T);
    int i;
    for (int t = 1; t <= T; ++t) {
        memset (a, 0, sizeof (a));
        gets(a);
        n = strlen(a);
        printf ("Case #%d: ", t);
        for (i = 0; i < n; ++i)
            if (a[i] == ' ')
                printf (" ");
            else
                printf ("%c", h[a[i] - 'a']);
        printf("\n");
    }
}
