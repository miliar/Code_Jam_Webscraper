#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char comb[256][256];
    char oppo[256][256];
    char elem_list[128];
    int tc;
    scanf("%d", &tc);
    for (int ncase = 1; ncase <= tc; ++ncase)
    {
        memset(comb, 0, sizeof(comb));
        memset(oppo, 0, sizeof(oppo));
        char buf[128];
        int ncomb;
        scanf("%d", &ncomb);
        for (int i = 0; i < ncomb; ++i)
        {
            scanf("%s", buf);
            comb[buf[0]][buf[1]] = buf[2];
            comb[buf[1]][buf[0]] = buf[2];
        }
        int noppo;
        scanf("%d", &noppo);
        for (int i = 0; i < noppo; ++i)
        {
            scanf("%s", buf);
            oppo[buf[0]][buf[1]] = 1;
            oppo[buf[1]][buf[0]] = 1;
        }
        int ninv;
        scanf("%d", &ninv);
        scanf("%s", buf);
        int nelems = 0;
        for (int i = 0; i < ninv; ++i)
        {
            char invoke = buf[i];
            if (nelems)
            {
                char res = comb[elem_list[nelems - 1]][invoke];
                if (res > 0)
                {
                    elem_list[nelems - 1] = res;
                }
                else
                {
                    for (int j = 0; j < nelems; ++j)
                    {
                        if (oppo[elem_list[j]][invoke])
                        {
                            nelems = 0;
                            break;
                        }
                        if (j + 1 == nelems)
                        {
                            elem_list[nelems++] = invoke;
                            break;
                        }
                    }
                }
            }
            else
            {
                elem_list[nelems++] = invoke;
            }
        }
        printf("Case #%d: [", ncase);
        for (int i = 0; i < nelems; ++i)
        {
            if (i + 1 == nelems)
            {
                printf("%c", elem_list[i]);
            }
            else
            {
                printf("%c, ", elem_list[i]);
            }
        }
        puts("]");
    }
    return 0;
}
