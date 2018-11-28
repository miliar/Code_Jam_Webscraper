#include<cstdio>
#include<cmath>

int t;
long long l, p, c;

long long calc()
{
    scanf("%lld%lld%lld", &l, &p, &c);
    long long anz=0;
    for(long long i=l; i<p; i*=c)
    {
        //printf("%lld\n", i);
        ++anz;
    }

/*
    printf("anz: %lld\n", anz);
    if(anz==1)
        return 0;*/
    return ceil(log(anz)/log(2));
}

int main()
{
    int i,j;

    scanf("%d", &t);

    for(i=0; i<t; i++)
    {
        printf("Case #%d: %lld\n", i+1, calc());
    }

    return 0;
}
