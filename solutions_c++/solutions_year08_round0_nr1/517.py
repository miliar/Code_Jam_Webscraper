#include <stdio.h>
#include <string.h>

FILE *inf, *outf;
int n, s, q;
char ss[110][110], qs[1010][110];
int cnt;
bool chk[110];
int answer;

int main()
{
    int l1, l2, l3;

    inf = fopen("a.in", "r");
    outf = fopen("a.out", "w");
    fscanf(inf, "%d", &n);
    for (l1 = 1; l1 <= n; l1++)
    {
        fscanf(inf, "%d\n", &s);
        for (l2 = 1; l2 <= s; l2++)
            fgets(ss[l2], 100, inf);
        fscanf(inf, "%d\n", &q);
        for (l2 = 1; l2 <= q; l2++)
            fgets(qs[l2], 100, inf);
        for (l2 = 1; l2 <= s; l2++)
            chk[l2] = false;
        cnt = 0;
        answer = 0;
        l2 = 1;
        do {
            for (l3 = 1; l3 <= s; l3++)
                if (strcmp(qs[l2], ss[l3]) == 0 && chk[l3] != true)
                {
                    chk[l3] = true;
                    cnt++;
                }
            if (cnt == s)
            {
                for (l3 = 1; l3 <= s; l3++)
                    chk[l3] = false;
                cnt = 0;
                answer++;
            }
            else
                l2++;
        } while (l2 <= q);
        fprintf(outf, "Case #%d: %d\n", l1, answer);
    }
    return 0;
}
