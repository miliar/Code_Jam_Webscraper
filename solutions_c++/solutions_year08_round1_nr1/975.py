#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct a_s
{
    long long v;
    long long abs_v;
    bool used;
};

int main(void)
{
    FILE *fp1;
    char *c = NULL;
    char oneword[100];
    int test = 0, num_test = 0;
    int arr_num;
    struct a_s one[800];
    struct a_s two[800];
    struct a_s tmp;
    int i, j, ptr;
    long long scaler = 0;
    long long max = 0;

    fp1 = fopen("in.txt", "r");
    if ( fp1 == NULL )
    {
        printf("File failed to open\n");
        exit(1);
    }

    fscanf(fp1, "%d\n", &num_test);
    for (test=0; test<num_test; test++)
    {
        fscanf(fp1, "%d\n", &arr_num);
        for (i=0; i<arr_num; i++)
        {
            int v;
            fscanf(fp1, "%d", &v);
            one[i].v = (long long) v;
            one[i].abs_v = v;
            if ( v < 0 )
                one[i].abs_v = -v;
            one[i].used = false;
        }
        fscanf(fp1, "\n");
        for (i=0; i<arr_num; i++)
        {
            int v;
            fscanf(fp1, "%d", &v);
            two[i].v = (long long) v;
            two[i].abs_v = v;
            if ( v < 0 )
                two[i].abs_v = -v;
            two[i].used = false;
        }
        fscanf(fp1, "\n");

        // sort one
        for (i=0; i<arr_num; i++)
        {
            for (j=arr_num-1; j>=i+1; j--)
            {
                if ( one[j-1].abs_v < one[j].abs_v )
                {
                    // swap
                    tmp = one[j];
                    one[j] = one[j-1];
                    one[j-1] = tmp;
                }
            }
        }

        scaler = 0;
        for (i=0; i<arr_num; i++)
        {
            max = 100000 * 100000;
            ptr = 0;
            for (j=0; j<arr_num; j++)
            {
                if ( two[j].used == false )
                {
                    if ( (one[i].v * two[j].v) < max )
                    {
                        ptr = j;
                        max = one[i].v * two[j].v;
                    }
                }
            }

            scaler += max;
            two[ptr].used = true;
        }

        printf("Case #%d: %lld\n", test+1, scaler);
    }

    fclose(fp1);

    return 0;
}
