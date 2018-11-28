#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;
const int MAXLEN=200;
class bigint
{
    public:
        int oper,len,a[MAXLEN];
        bigint(int=0);
        ~bigint();
        int max(int a,int b);
        void check();
        void operator=(bigint m);
        void operator=(int m);
        void operator=(char *s);
        bool operator<(bigint m);
        bool operator<=(bigint m);
        bool operator>(bigint m);
        bool operator>=(bigint m);
        bool operator==(bigint m);
        bool operator!=(bigint m);
        bigint operator-();
        bigint operator+(bigint m);
        void operator+=(bigint m);
        bigint operator-(bigint m);
        void operator-=(bigint m);
        bigint operator*(bigint m);
        bigint operator*(int m);
        void operator*=(bigint m);
        void operator*=(int m);
        bigint operator/(bigint m);
        bigint operator/(int m);
        void operator/=(bigint m);
        void operator/=(int m);
        bigint operator%(bigint m);
        bigint operator%(int m);
        void operator%=(bigint m);
        void operator%=(int m);
};
bigint abs(bigint m);
bool read(bigint &m);
void write(bigint m);
void coutln(bigint m);
bigint gcd(bigint a,bigint b);

int bigint::max(int a,int b)
{
    return (a>b)?a:b;
}
bigint::bigint(int v)
{
    (*this)=v;
    this->check();
}
bigint::~bigint(){}
void bigint::check()
{
    for (;len>0 && a[len]==0;len--);
    if (len==0)
        oper=1;
}
void bigint::operator=(bigint m)
{
    oper=m.oper;
    len=m.len;
    memcpy(a,m.a,MAXLEN*sizeof(int));
    this->check();
}
void bigint::operator=(int m)
{
    oper=(m>0)?1:-1;
    m=abs(m);
    memset(a,0,MAXLEN*sizeof(int));
    for (len=0;m>0;m=m/10000)
        a[++len]=m%10000;
    this->check();
}
void bigint::operator=(char *s)
{
    int i,L;
    (*this)=0;
    if (s[0]=='-' || s[0]=='+')
    {
        if (s[0]=='-')
            oper=-1;
        L=strlen(s);
        for (i=0;i<L;i++)
            s[i]=s[i+1];
    }
    L=strlen(s);
    len=(L+3)/4;
    for (i=0;i<L;i++)
        a[(L-i+3)/4]=a[(L-i+3)/4]*10+(s[i]-48);
    this->check();
}
bool bigint::operator<(bigint m)
{
    if (oper!=m.oper)
        return oper<m.oper;
    if (len!=m.len)
        return oper*len<m.len*oper;
    for (int i=len;i>=1;i--)
        if (a[i]!=m.a[i])
            return a[i]*oper<m.a[i]*oper;
    return false;
}
bool bigint::operator>=(bigint m)
{
    return !((*this)<m);
}
bool bigint::operator==(bigint m)
{
    return (!((*this)<m)) && (!(m<(*this)));
}
bool bigint::operator!=(bigint m)
{
    return ((*this)<m) || (m<(*this));
}
bigint bigint::operator-()
{
    bigint c=(*this);
    c.oper=-c.oper;
    c.check();
    return c;
}
bigint abs(bigint m)
{
    bigint c=m;
    c.oper=abs(c.oper);
    c.check();
    return c;
}
bigint bigint::operator+(bigint m)
{
    if (m.len==0)
        return (*this);
    if (len==0)
        return m;
    if (oper==m.oper)
    {
        bigint c;
        c.oper=oper;
        c.len=max(len,m.len)+1;
        for (int i=1,temp=0;i<=c.len;i++)
            c.a[i]=(temp=(temp/10000+a[i]+m.a[i]))%10000;
        c.check();
        return c;
    }
    return (*this)-(-m);
}
bigint bigint::operator-(bigint m)
{
    if (m.len==0)
        return (*this);
    if (len==0)
        return (-m);
    if (oper==m.oper)
    {
        bigint c;
        if (abs(*this)>=abs(m))
        {
            c.oper=oper;
            c.len=len;
            for (int i=1,temp=0;i<=len;i++)
                c.a[i]=((temp=(-int(temp<0)+a[i]-m.a[i]))+10000)%10000;
            c.check();
            return c;
        }
        return -(m-(*this));
    }
    return (*this)+(-m);
}
bool read(bigint &m)
{
    char s[MAXLEN*4+10];
    if (scanf("%s",s)==EOF)
        return false;
    for (int i=0;s[i];i++)
        if (!(s[i]>='0' && s[i]<='9' || (s[i]=='+' || s[i]=='-') && i==0))
            return false;
    m=s;
    return true;
}
void write(bigint m)
{
    if (m.oper==-1)
        printf("-");
    printf("%d",m.a[m.len]);
    for (int i=m.len-1;i>=1;i--)
        printf("%04d",m.a[i]);
}
void coutln(bigint m)
{
    write(m);
    printf("\n");
}
bigint bigint::operator*(bigint m)
{
    bigint c;
    c.oper=oper*m.oper;
    c.len=len+m.len;
    for (int i=1;i<=m.len;i++)
    {
        int number=m.a[i],j,temp=0;
        for (j=1;j<=len;j++)
            c.a[i+j-1]+=number*a[j];
        if (i%10==0 || i==m.len)
            for (j=1;j<=c.len;j++)
                c.a[j]=(temp=(temp/10000)+c.a[j])%10000;
    }
    c.check();
    return c;
}
bigint bigint::operator*(int m)
{
    if (m<0)
        return -((*this)*(-m));
    if (m>100000)
        return (*this)*bigint(m);
    bigint c;
    c.len=len+2;
    c.oper=oper;
    int t=0;
    for (int i=1;i<=c.len;i++)
        c.a[i]=(t=(t/10000+a[i]*m))%10000;
    c.check();
    return c;
}
bigint bigint::operator/(bigint m)
{
    if (m.len==0)
    {
        printf("Division by zero.\n");
        exit(0);
    }
    if (abs(*this)<abs(m))
        return 0;
    bigint c,left;
    c.oper=oper/m.oper;
    m.oper=1;
    c.len=len-m.len+1;
    left.len=m.len-1;
    memcpy(left.a+1,a+len-left.len+1,left.len*sizeof(int));
    for (int i=c.len;i>=1;i--)
    {
        left=left*10000+a[i];
        int head=0,tail=10000,mid;
        while (head+1<tail)
        {
            mid=(head+tail)/2;
            if (left>=m*mid)
                head=mid;
            else
                tail=mid;
        }
        c.a[i]=head;
        left=left-m*head;
    }
    c.check();
    return c;
}
bigint bigint::operator/(int m)
{
    if (m<0)
        return -((*this)/(-m));
    if (m>100000)
        return (*this)/bigint(m);
    bigint c;
    c.oper=oper;
    c.len=len;
    int t=0;
    for (int i=c.len;i>=1;i--)
        c.a[i]=(t=(t%m*10000+a[i]))/m;
    c.check();
    return c;
}
bigint bigint::operator %(bigint m)
{
    return (*this)-((*this)/m)*m;
}
bigint bigint::operator%(int m)
{
    if (m<0)
        return -((*this)%(-m));
    if (m>100000)
        return (*this)%bigint(m);
    int t=0;
    for (int i=len;i>=1;i--)
        t=(t*10000+a[i])%m;
    return t;
}
bigint gcd(bigint a,bigint b)
{
    return (b==0)?a:gcd(b,a%b);
}
bigint a[1001];  
int main()
{
freopen("B-large.in","r",stdin);
freopen("B-large.out","w",stdout);

    int cas,n;
    scanf("%d",&cas);
    for (int T = 1;T <= cas;T++)
    {
        scanf("%d",&n);
        for (int i = 0;i < n;i++)
            read(a[i]);
        bigint k = abs(a[1] - a[0]);
        for (int i = 2;i < n;i++)
            k = gcd(k,abs(a[i]-a[i-1]));
        printf("Case #%d: ",T);
        coutln((k-a[0]%k)%k);
    }
}
