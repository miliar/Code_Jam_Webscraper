#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#define MAXN 1000
#define MAXS 60
#define MAXL 15
#define BASE 10000
#define SIZE 4
using namespace std;

struct BigNum
{
    int num[MAXL+1];
    int len;
    BigNum()
    {
    }
    BigNum(int n)
    {
        memset(num,0,sizeof(num));
        len=0;
        while(n!=0)
        {
            num[len++]=n%BASE;
            n=n/BASE;
        }
    }
    BigNum(char *s)
    {
        char data[SIZE+1];
        int i;
        memset(num,0,sizeof(num));
        len=0;
        if(strcmp(s,"0")==0)
        {
            return;
        }
        for(i=strlen(s);i>=1;i=i-SIZE)
        {
            if(i>=SIZE)
            {
                strncpy(data,&s[i-SIZE],SIZE);
                data[SIZE]='\0';
            }
            else
            {
                strncpy(data,s,i);
                data[i]='\0';
            }
            num[len++]=atoi(data);
        }
    }
    void print()
    {
        int i;
        if(len==0)
        {
            printf("0");
            return;
        }
        printf("%d",num[len-1]);
        for(i=len-2;i>=0;i--)
        {
            printf("%04d",num[i]);
        }
    }
    BigNum& operator-=(const BigNum &a)
    {
        int i;
        for(i=0;i<len;i++)
        {
            num[i]=num[i]-a.num[i];
            if(num[i]<0)
            {
                num[i]=num[i]+BASE;
                num[i+1]--;
            }
        }
        while((len>=1)&&(num[len-1]==0))
        {
            len--;
        }
        return *this;
    }
    friend BigNum movemul(const BigNum &a,int k,int move)
    {
        BigNum ret;
        int i,carry;
        memset(ret.num,0,sizeof(ret.num));
        ret.len=a.len+move;
        carry=0;
        for(i=0;i<a.len;i++)
        {
            carry=carry+a.num[i]*k;
            ret.num[i+move]=carry%BASE;
            carry=carry/BASE;
        }
        while(carry>0)
        {
            ret.num[ret.len++]=carry%BASE;
            carry=carry/BASE;
        }
        return ret;
    }
    friend BigNum operator%(const BigNum &a,const BigNum &b)
    {
        BigNum t,x;
        int i,k;
        x=a;
        for(i=a.len-b.len;i>=0;i--)
        {
            for(k=1<<13;k>0;k=k>>1)
            {
                t=movemul(b,k,i);
                if(x>=t)
                {
                    x=x-t;
                }
            }
        }
        return x;
    }
    friend BigNum operator-(const BigNum &a,const BigNum &b)
    {
        BigNum ret;
        ret=a;
        ret-=b;
        return ret;
    }
    friend bool operator<(const BigNum &a,const BigNum &b)
    {
        return compare(a,b)<0;
    }
    friend bool operator>=(const BigNum &a,const BigNum &b)
    {
        return compare(a,b)>=0;
    }
    friend bool operator==(const BigNum &a,const BigNum &b)
    {
        return compare(a,b)==0;
    }
    friend bool operator!=(const BigNum &a,const BigNum &b)
    {
        return compare(a,b)!=0;
    }
    friend int compare(const BigNum &a,const BigNum &b)
    {
        int i;
        if(a.len!=b.len)
        {
            return a.len-b.len;
        }
        for(i=a.len-1;i>=0;i--)
        {
            if(a.num[i]!=b.num[i])
            {
                return a.num[i]-b.num[i];
            }
        }
        return 0;
    }
    friend BigNum GCD(BigNum a,BigNum b)
    {
        BigNum t;
        while(b!=0)
        {
            t=a%b;
            a=b;
            b=t;
        }
        return a;
    }
};

BigNum a[MAXN+1];
char s[MAXS+1];
int n;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int c,i,t;
    BigNum g,y;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%d",&n);
        scanf("%s",s);
        a[0]=BigNum(s);
        scanf("%s",s);
        a[1]=BigNum(s);
        g=max(a[0],a[1])-min(a[0],a[1]);
        for(i=2;i<n;i++)
        {
            scanf("%s",s);
            a[i]=BigNum(s);
            g=GCD(g,max(a[i-1],a[i])-min(a[i-1],a[i]));
        }
        y=a[0]%g;
        printf("Case #%d: ",c+1);
        if(y==0)
        {
            printf("0\n");
        }
        else
        {
            (g-y).print();
            printf("\n");
        }
    }
    return 0;
}
