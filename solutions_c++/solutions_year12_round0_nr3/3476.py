#include<stdio.h>
#include<iostream>
#include<string.h>
#include<string>
#include<algorithm>
#include<map>
using namespace std;

map<pair<int,int>,bool> mp;
int dgt(int n)
{
    int digitlen=0;
    int tmpn = n;
    while(tmpn)
    {
        digitlen++;
        tmpn/=10;
    }
    return digitlen;
}
int pow_10(int pow)
{
    int ret=1;
    for(int i=0;i<pow;i++)
    {
        ret*=10;
    }
    return ret;
}
int countpair(int n,int a,int b,int digitlen)
{
    int m,cnt=0;
    for(int i=1;i<=digitlen;i++)
    {
        m = n / pow_10(i);
        //printf("prev n=%d m=%d\n",n,m);
        m +=(n%pow_10(i))*pow_10(digitlen-i);
        //printf("n=%d m=%d\n",n,m);
        if(n < m && m <= b)
        {
         //   make_pair()
            cnt++;
        }
    }
    return cnt;
}

int main()
{
    freopen("C0.in","r",stdin);
    freopen("c.out","w",stdout);
    int test,kase=0;
    scanf("%d",&test);
    while(test--)
    {
        int a,b,n,m,cnt=0;
        scanf("%d %d",&a,&b);

        int digitlen = dgt(a);
        for(int i= a; i<= b; i++)
        {
            cnt+= countpair(i,a,b,digitlen);

        }
        printf("Case #%d: %d\n",++kase,cnt);
    }
    return 0;
}
