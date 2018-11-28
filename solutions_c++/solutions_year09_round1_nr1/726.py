#include<algorithm>
#include<stdio.h>

FILE * in = fopen("in.in","r");
FILE * out = fopen("out.out","w");

int conv(int n , int base)
{
    int ret = 0;
    int res[10] , resc = 0;
    while(n)
    {
        res[resc++] = (n % base);
        n /= base;
    }
    for(int i = resc-1 ;i > -1;i--)
        ret *= 10 , ret += res[i];
    return ret;
}

bool test(int n , int base)
{
    int m , sum;
    for(int i=0;i<600;i++)
    {
        m = n;
        sum = 0;
        while(m)
        {
            int j = (m % 10) * (m % 10);
            sum += j;
            m /= 10;
        }
        if(sum > 500) continue;
        sum = conv(sum,base);
        if(sum == 1) return 1;
        n = sum;
    }
    return 0;
}

int main()
{
    int i , a , k , b[11] , bc = 0 , tt , c = 0;
    char x;
    fscanf(in,"%d\n",&k);
    while(k--)
    {
        bc = 0 , tt = 0;
        c++;
        while(1)
        {
            fscanf(in,"%c",&x);
            if(x == ' ')
            {
                b[bc++] = tt;
                tt = 0;
                continue;
            }
            if(x == '\n') break;
            tt *= 10 , tt += x - '0';
        }
        b[bc++] = tt;
        for(i=2;;i++)
        {
            for(a=0;a<bc;a++)
            {
                int j = conv(i,b[a]);
                if(!test(j,b[a])) break;
            }
            if(a == bc)
            {
                fprintf(out,"Case #%d: %d\n",c,i);
                break;
            }
        }
    }
    //getchar();
    return 0;
}
