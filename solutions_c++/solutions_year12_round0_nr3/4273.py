#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

int Loop,Loo;
int A,B;
int n,m;
int res;

bool ok(int n,int m)
{
    int s[6],e[6];
    int k=m,i=0,t,base,j;
    while(k)
        {
            s[i]=k%10;
            ++i;
            k /= 10;
        }
    for(k=i-1;k>=0;--k)
        e[i-k-1]=s[k];
    for(k=0;k<i;++k)
        s[k]=e[k];
    for(k=0;k<i;++k)
        {
            t = s[k];
            if(0==t)
                continue;
            //base = 10;
            for(j = (k+1)%i;j != k;j=(j+1)%i)
                {
                    t = t*10+s[j];
                    //base *= 10;
                }
            if(t == n)
                return true;
        }
    return false;
}

int main(void)
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&Loop);
    ok(123,132);
    for(Loo=1;Loo<=Loop;++Loo)
        {
            res = 0;
            scanf("%d%d",&A,&B);
            for(n=A;n<B;++n)
                {
                    for(m=n+1;m<=B;++m)
                        {
                            if(ok(n,m))
                                {
                                    ++res;
                                    //printf("%d %d\n",n,m);
                                }
                        }
                }
            printf("Case #%d: %d\n",Loo,res);
        }
    return 0;
}
