/*
the original author of big number template is windy7926778
the rest code belong to shenfei361
shenfei361 also did some modification to the pri and set function
*/
#include<stdio.h>
#include<memory>
#include<string.h>
#include<algorithm>
using namespace std;
/*

  windy7926778

  2007.10.04

  非负大数

  10^4进制

  所有的函数中的大数都为引用

*/
FILE *fin, *fout;
const int N=1024; // 10 进制下的最大位数

struct big
{
    int d[N/4];
    int len;
};

void  pri(big &x) // 输出大数 x ，不输出换行符
{
    int i;
    fprintf(fout,"%d",x.d[x.len-1]);
    for(i=x.len-2;i>=0;i--)
        fprintf(fout,"%04d",x.d[i]);
}

void set(big &x, big &y)
{
    memset(&x,0,sizeof(x));
    x.len = y.len;
    int i;
    for (i=0; i<y.len; i++)
        x.d[i] = y.d[i];
}

void set(big &x,char str[]) //把不带符号的非空字符串 str 转化为大数 x ，并去除前导零
{
    memset(&x,0,sizeof(x));
    int i,w=1,now=0;
    for(i=strlen(str)-1;i>=0;i--)
    {
        now+=w*(str[i]-48);
        w*=10;
        if(w==10000)
        {
            x.d[x.len++]=now;
            now=0;
            w=1;
        }
    }
    if(now)
        x.d[x.len++]=now;
    while(x.len>1&&!x.d[x.len-1])
        x.len--;
}

void set(big &x,int n) //把非负整数 n 转化为大数 x
{
    memset(&x,0,sizeof(x));
    if(!n)
    {
        x.len=1;
        x.d[0]=0;
    }
    else
    {
        while(n)
        {
            x.d[x.len++]=n%10000;
            n/=10000;
        }
    }
}

void add(big &x,big &y) // 大数 x = 大数 x + 大数 y
{
    int i,c=0;
    for(i=0;i<x.len||i<y.len;i++)
    {
        x.d[i]+=y.d[i]+c;
        if(x.d[i]>=10000)
        {
            x.d[i]-=10000;
            c=1;
        }
        else
            c=0;
    }
    if(c)
        x.d[i++]=1;
    x.len=i;
}

void sub(big &x,big &y) // 大数 x = 大数 x - 大数 y ，要求 x >= y
{
    int i,c=0;
    for(i=0;i<y.len;i++)
    {
        x.d[i]-=y.d[i]+c;
        if(x.d[i]<0)
        {
            x.d[i]+=10000;
            c=1;
        }
        else
            c=0;
    }
    for(;c;i++)
    {
        x.d[i]-=c;
        c=0;
        if(x.d[i]<0)
        {
            x.d[i]+=10000;
            c=1;
        }
    }
    while(x.len>1&&!x.d[x.len-1])
        x.len--;
}

void mul(big &z,big &x,big &y) // 大数 z = 大数 x * 大数 y
{
    memset(&z,0,sizeof(z));
    z.len=x.len+y.len;
    int i,j;
    for(i=0;i<x.len;i++)
        for(j=0;j<y.len;j++)
        {
            z.d[i+j]+=x.d[i]*y.d[j];
            z.d[i+j+1]+=z.d[i+j]/10000;
            z.d[i+j]%=10000;
        }
    while(z.len>1&&!z.d[z.len-1])
        z.len--;
}

void mul(big &z,big &x,int e) // 大数 z = 大数 x * 非负整数 e
{
    memset(&z,0,sizeof(z));
    int i;
    for(i=0;i<x.len;i++)
    {
        z.d[i]+=x.d[i]*e;
        z.d[i+1]=z.d[i]/10000;
        z.d[i]%=10000;
    }
    if(z.d[i]/10000)
    {
        z.d[i+1]=z.d[i]/10000;
        z.d[i]%=10000;
        i++;
    }
    z.len=i+1;
    while(z.len>1&&!z.d[z.len-1])
        z.len--;
}

bool cmp(big &x,big &y) //return 大数 x <= 大数 y;
{
    if(x.len<y.len)
        return true;
    if(x.len>y.len)
        return false;
    int i;
    for(i=x.len-1;i>=0;i--)
        if(x.d[i]!=y.d[i])
            return x.d[i]<y.d[i];
    return true;
}

void div(big &z,big &x,big &y,big &t) // 大数 z = 大数 x / 大数 y  余数为 t
{
    memset(&z,0,sizeof(z));
    int i,j,p,q,now;
    big e;
    set(t,0);
    for(i=x.len-1;i>=0;i--)
    {
        for(j=t.len;j>0;j--)
            t.d[j]=t.d[j-1];
        t.len++;
        t.d[0]=x.d[i];
        while(t.len>1&&!t.d[t.len-1])
            t.len--;
        p=0;
        q=9999;
        while(p<=q)
        {
            now=(p+q)>>1;
            mul(e,y,now);
            if(cmp(e,t))
                p=now+1;
            else
                q=now-1;
        }
        mul(e,y,q);
        sub(t,e);
        z.d[i]=q;
    }
    z.len=x.len;
    while(z.len>1&&!z.d[z.len-1])
        z.len--;
}

bool equ(big &x,big &y)
{
	if (x.len!=y.len)
		return false;
	int i;
	for (i=x.len-1; i>=0; i--)
		if (x.d[i]!=y.d[i])
			return false;
	return true;
}

bool less(big x, big y)
{
    return (cmp(x,y) && !equ(x,y));
}

big gcd(big, big);

int main()
{
    fin = fopen("B-large.in","r");
    fout = fopen("B-large.out","w");
    int num,casenum;
    fscanf(fin,"%d",&casenum);
    big t[1002];
    for (num=1; num<=casenum; num++)
    {
        int N;
        memset(t,0,sizeof(t));
        fscanf(fin,"%d",&N);
        int i;
        char str[1024];
        for (i=0; i<N; i++)
        {
            fscanf(fin,"%s",str);
            set(t[i],str);
        }
        sort(t,t+N,less);
        big y,T;
        for (i=N-1; i>0; i--)
            sub(t[i],t[i-1]);
        set(T, t[1]);
        for (i=2; i<N; i++)
            T = gcd(T, t[i]);
        big z,rem;
        div(z,t[0],T,rem);
        big zero;
        set(zero,0);
        if (equ(rem,zero))
            set(y,0);
        else
        {
            set(y,T);
            sub(y,rem);
        }
        fprintf(fout,"Case #%d: ",num);
        pri(y);
        fprintf(fout,"\n");
    }
    fclose(fin);
    fclose(fout);
    return 0;
}

big gcd(big x, big y)
{
    if (!cmp(y,x))
    {
        big temp;
        set(temp,x);
        set(x,y);
        set(y,temp);
    }
    big zero;
    set(zero,0);
    if (equ(y,zero))
        return x;
    else
    {
        big z,rem;
        div(z,x,y,rem);
        return gcd(y, rem);
    }
}
