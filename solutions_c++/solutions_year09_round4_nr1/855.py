#include<stdio.h>

int testcase, t;


char M[80][80];
int n;

void swap(int ti, int tj)
{
    int i;
    char tmp;
    for(i = 0; i < n; i ++)
    {
        tmp = M[ti][i];
        M[ti][i] = M[tj][i];
        M[tj][i] = tmp;
    }
}
int get_ans(int k)
{
    int i, j;
    if(k == n)
        return 0;
    for(i = k; i < n; i ++)
    {
        for(j = k + 1; j < n; j ++)
            if(M[i][j] == '1')
                break;
        if(j == n)
            break;
    }
//    printf("i = %d n = %d\n", i, n);
    int ans = 0;
    for(j = i; j > k; j --)
        swap(j, j - 1);
    ans = i - k + get_ans(k + 1);
    return ans;
}
int main()
{
    scanf("%d", &testcase);
    int i, j;
    for(t = 1; t <= testcase; t ++)
    {
        scanf("%d", &n);
        for(i = 0; i < n; i ++)
            scanf("%s", M[i]);
        printf("Case #%d: %d\n", t, get_ans(0));
    }
    return 0;
}
