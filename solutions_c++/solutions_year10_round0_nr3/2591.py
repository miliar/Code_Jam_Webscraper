#include <cstdio>

int mic[1010][32][2];
//      from  cn 0to 1cnx
int in[1010];
int main()
{
    freopen("out3.txt", "w", stdout);
    int testI, testCount;
    scanf("%d", &testCount);
    for(testI = 1; testI <= testCount; testI++)
    {
        int r,k,n;
        scanf("%d %d %d", &r, &k, &n);
        for(int i = 0; i < n; i++)
            scanf("%d", &in[i]);

        for(int i = 0; i < n; i++)
        {
            int sum = 0;
            for(int j = 0; j < n; j++)
            {
                if(sum + in[(i+j)%n] <= k)
                {
                    mic[i][0][0] = (i+j+1)%n;
                    sum += in[(i+j)%n];
                    mic[i][0][1] = sum;
                }else break;
            }
            //printf("%d %d %d\n", i, mic[i][0][0], mic[i][0][1]);
        }
        int sum = 0;
        int j;
        for(j = 1; (1<<j) <= r; j++)
            for(int i = 0; i < n; i++)
            {
                mic[i][j][0] = mic[ mic[i][j-1][0] ][j-1][0];
                mic[i][j][1] = mic[i][j-1][1] + mic[ mic[i][j-1][0] ][j-1][1];
            }
        sum = 0;
        for(int i = 0; j >= 0; j--)
        {
            if((1<<j)<=r)
            {
                sum += mic[i][j][1];
                i = mic[i][j][0];
                r-=(1<<j);
            }
        }
        printf("Case #%d: %d\n", testI, sum);
    }
    return 0;
}
