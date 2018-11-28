#include <cstdio>

int l, d, n;
int i, j, k, ans;
char w[5100][20], in[2000];
bool candi[20][26];
FILE * fp;
int main()
    {
    fp = fopen("a.out", "wt");
    scanf("%d%d%d", &l, &d, &n);
    for (i = 0; i < d; i++)
        scanf("%s", w[i]);
    for (i = 0; i < n; i++)
        {
        for (j = 0; j < l; j++)
            for (k = 0; k < 26; k++)
                candi[j][k] = false;
        scanf("%s", in);
        k = 0;
        for (j = 0; in[j] != 0; j++)
            {
            if (in[j] == '(')
                {
                j++;
                while (in[j] != ')')
                    {
                    candi[k][in[j] - 'a'] = true;
                    j++;
                    }
                }
            else
                {
                candi[k][in[j] - 'a'] = true;
                }
            k++;
            }
        ans = 0;
        for (j = 0; j < d; j++)
            {
            for (k = 0; k < l; k++)
                {
                if (!candi[k][w[j][k] - 'a'])
                    break;
                }
            if (k == l)
                ans++;
            }
        fprintf(fp, "Case #%d: %d\n", i + 1, ans);
        }
    return 0;
    }
