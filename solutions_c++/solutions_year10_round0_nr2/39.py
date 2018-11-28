#include <iostream>

using namespace std;

struct large
{
    int len,num[11];
    const bool operator<(const large A) const
    {
        if (A.len!=len) return len<A.len;
        else
            for (int i=len-1;i>=0;i--)
                if (num[i]!=A.num[i]) return num[i]<A.num[i];
        return false;
    }
    const bool operator>(const large A) const
    {
        if (A.len!=len) return len>A.len;
        else
            for (int i=len-1;i>=0;i--)
                if (num[i]!=A.num[i]) return num[i]>A.num[i];
        return false;
    }
    const large operator+(const large A) const
    {
        large ret;int k=0;
        for (int i=0;i<max(A.len,len);i++)
        {
            int s1=0,s2=0;
            if (i<len) s1=num[i];
            if (i<A.len) s2=A.num[i];
            ret.num[i]=s1+s2+k;
            k=ret.num[i]/100000;
            ret.num[i]=ret.num[i] % 100000;
        }
        ret.len=max(A.len,len);
        while (k!=0)
        {
            ret.num[ret.len]=k % 100000;
            k=k/100000;
            ret.len++;
        }
        while (ret.len!=1 && ret.num[ret.len-1]==0) ret.len--;
        return ret;
    }
    const large operator-(const large A) const
    {
        large ret;int k=0;
        for (int i=0;i<len;i++)
        {
            int s1=num[i],s2=0;
            if (i<A.len) s2=A.num[i];
            ret.num[i]=s1-s2+k;
            if (ret.num[i]<0) {ret.num[i]+=100000; k=-1;}
                else k=0;
        }
        ret.len=len;
        while (ret.len!=1 && ret.num[ret.len-1]==0) ret.len--;
        return ret;
    }
};

const int key[5]={1,10,100,1000,10000};
large a[1000];
char c[100000];
int n;

void print(large A)
{
    printf("%d",A.num[A.len-1]);
    for (int i=A.len-2;i>=0;i--)
    {
        if (A.num[i]>=10000) printf("%d",A.num[i]);
        else
        if (A.num[i]>=1000) printf("0%d",A.num[i]);
        else
        if (A.num[i]>=100) printf("00%d",A.num[i]);
        else
        if (A.num[i]>=10) printf("000%d",A.num[i]);
        else
            printf("0000%d",A.num[i]);
    }
    printf("\n");
}

large mod(large A,large B)
{
    if (A<B) return A;
    else
    {
        A=mod(A,B+B);
        if (A<B) return A;
        return A-B;
    }
}

large gcd(large A,large B)
{
    if (B.len==1 && B.num[0]==0) return A;
        else return gcd(B,mod(A,B));
}

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int p=1;p<=T;p++)
    {
        printf("Case #%d: ",p);
        scanf("%d",&n);
        gets(c); int j=strlen(c)-1;
        for (int i=0;i<n;i++)
        {
            a[i].len=0; int s=0,js=0;
            while (c[j]!=' ')
            {
                s=s+(c[j]-'0')*key[js]; js++; j--;
                if (js==5)
                {
                    a[i].num[a[i].len++]=s;
                    s=js=0;
                }
            }
            if (s!=0) a[i].num[a[i].len++]=s; j--;
        }
        for (int i=n-1;i>0;i--) a[i]=max(a[i],a[i-1])-min(a[i],a[i-1]);
        large d; memset(d.num,0,sizeof(d.num)); d.len=1;
        for (int i=1;i<n;i++) d=gcd(d,a[i]);
        print(mod(d-mod(a[0],d),d));
    }
}
