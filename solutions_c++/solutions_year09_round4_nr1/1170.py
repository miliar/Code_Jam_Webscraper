#include <stdio.h>

int main()
{
    int T, N;
    int i, j, k, val;
    char input[128];
    int array[40], ans;

    scanf("%d", &T);
    for(i=0; i<T; i++)
    {
        scanf("%d\n", &N);

        for(j=0; j<N; j++)
        {
            array[j] = 0;
            scanf("%s", input);
            for(k=0; k<N; k++)
            {
                if( input[k]=='1' )
                {
                    array[j] = k;
                }
            }
        }

        ans = 0;
        for(j=0; j<N; j++)
        {
            if( array[j]>j )
            {
                for(k=j+1; k<N; k++)
                {
                    if( array[k]<=j )
                    {
                        val = array[k];
                        for(int p=k; p>j; p--)
                        {
                            array[p] = array[p-1];
                            ans++;
                        }
                        array[j] = val;
                        break;
                    }
                }
/*
                for(k=0; k<N; k++)
                {
                    printf("%d ", array[k]);
                }
                printf("\n");
*/
            }
        }
        printf("Case #%d: %d\n", i+1, ans);
    }

    return 0;
}
