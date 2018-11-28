#include <cstdio>


int sprawdz(int i, int a, int b)
{
    if (i < 10)
        return 0;

    char buf[10];
    sprintf(buf,"%d",i);
    int r = 0;
    int x = 10;
    int c = 1;
    while (x <= i)
    {
        x *= 10;
        c++;
    }
    x /= 10;

    int num[10];
    num[0] = i;
    r = 1;
    while(c--)
    {
        int d = i/x;
        i = (i%x)*10+d;
        if (i>num[0] && i>=x && i<=b)
        {
            bool byl = false;
            for (int in=0; in<r; in++)
                if (i == num[in])
                {
                    byl = true;
                    break;
                }
            if (!byl)
                num[r++] = i;
        }
    }
    return r-1;
}

int main()
{
    int T, A, B, res=0;
    scanf("%d",&T);
    for (int tn=1; tn<=T; tn++)
    {
        res = 0;
        scanf("%d %d",&A,&B);
        for (int i=A; i<B; i++)
            res += sprawdz(i,A,B);
        printf("Case #%d: %d\n",tn,res);
    }
}
