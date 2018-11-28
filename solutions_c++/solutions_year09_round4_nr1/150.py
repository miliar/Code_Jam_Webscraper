#include <stdio.h>
#include <cstring>

char A[100][100];
int r[100], n;

void swap(int a, int b)
{
    /*
    for(int i=0; i<n; ++i)
    {
        int tmp = A[a][i];
        A[a][i] = A[b][i];
        A[b][i] = tmp;
    }
    */
    int tmp = r[a];
    r[a] = r[b];
    r[b] = tmp;
}

int main()
{
    int t, tc = 0, ans = 0;
    scanf("%d", &t);
    while(t--)
    {
        ans = 0;
        scanf("%d", &n);
        for(int i=1; i<=n; ++i)
        {
            r[i] = 0;
            scanf("%s", A[i]);
            for(int j=1; j<=n; ++j)
            {
                if(A[i][j-1] == '1') r[i] = j;
            }
            //puts(A[i]);
        }

        //for(int i=1; i<=n; ++i) printf("%d ", r[i]);
        //puts("");

        for(int i=1; i<=n; ++i)
        {
            if(r[i] <= i) continue;

            int j = i + 1;
            while(j<=n && r[j]>i) j++;

            for(; j>i; --j)
            {
                ans++;
                swap(j, j - 1);
            }
        }
        printf("Case #%d: %d\n", ++tc, ans);
    }
    return 0;
}

