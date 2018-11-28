#include<cstdio>

int nums[100];
int n;

int main()
{
    int t, teste;
    int i, j, k;
    int aux;
    scanf("%d", &teste);
    for (t=0; t<teste; t++)
    {
        char buf[100];
        int resp = 0;
        scanf("%d", &n);
        for (i=0; i<n; i++)
        {
            scanf("%s", buf);
            nums[i] = -1;
            for (j=0; j<n; j++)
            {
                if (buf[j] == '1')
                    nums[i] = j;
            }
        }
        for (i=0; i<n; i++)
        {
            if (nums[i] > i)
            {
                for (j=i+1; j<n; j++)
                {
                    if (nums[j] <= i)
                        break;
                }
                resp += j-i;
                aux = nums[j];
                for (k = j-1; k >= i; k--)
                {
                    nums[k+1] = nums[k];
                }
                nums[i] = aux;
            }
        }
        printf("Case #%d: %d\n", t+1, resp);
    }
    return 0;
}
