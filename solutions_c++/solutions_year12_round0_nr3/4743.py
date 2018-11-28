#include <cstdio>
#include <cstring>

using namespace std;

char buffer[20];
int gtc[3000000], count[3000000], zz, ii, jj, T, A, B;

int rotate(int n, int co)
{
    int l1, l2, ii = 1;
    for (; co > 0; co--)
        ii *= 10;
    if (n / ii == 0)
        return -1;
    sprintf(buffer, "%d", n);
    l1 = strlen(buffer);
    sprintf(buffer, "%d%d", n % ii, n / ii);
    sscanf(buffer, "%d", &ii);
    sprintf(buffer, "%d", ii);
    l2 = strlen(buffer);

    if (l1 != l2)
        return -1;
    return ii;
}

int main(void)
{
    scanf("%d\n", &T);
    for (ii = 1; ii <= T; ii++)
    {
        count[0] = 0;
        scanf("%d %d\n", &A, &B);
        for (zz = A; zz <= B; zz++)
        {
            for (jj = 1; ; jj++)
            {
                int t = rotate(zz, jj);
                if (t == -1)
                    break;
                if (t >= A && t <= B && t < zz)
                {
                    count[0]++;
                }
            }
        }
        printf("Case #%d: %d\n", ii, count[0]);
    }



    return 0;
}
