#include <iostream> 

using namespace std;

#define maxsize 6000

struct hp
{
    int len;
    int s[maxsize+1];
};

int getInt(const hp &y)
{
	int b=0;
	int i;
	for(i=y.len;i>=1;i--)
	{
		b*=10;
		b+=y.s[i];
	}
	return b;
}
void input(hp &a,string str)
{
    int i;
    while(str[0]=='0' && str.size()!=1)
       str.erase(0,1);
    a.len=(int)str.size();
    for(i=1;i<=a.len;++i)
       a.s[i]=str[a.len-i]-48;
    for (i=a.len+1;i<=maxsize;++i)
       a.s[i]=0;
}

void print(const hp &y)
{
int i;
for(i=y.len;i>=1;i--)
    cout<<y.s[i];
cout<<endl;
}
 

// 
// 高精度数比较
// 
// 语法：int result=compare(const hp &a,const hp &b);
//  
// 参数：
//  
// a,b：
//  进行比较的高精度数字
//  
// 返回值：
//  比较结果，a>b返回正数，a=b返回0，a<b返回负数
//  
// 源程序：
//  
 

 int compare(const hp &a,const hp &b)
{
int len;
if(a.len>b.len)
   len=a.len;
else
   len=b.len;
while(len>0 && a.s[len]==b.s[len]) len--;
if(len==0)
    return 0;
else
    return a.s[len]-b.s[len];
} 
 bool operator == (const hp &a, const hp &b)
 {
	 return compare(a,b)==0;
 }
bool operator != (const hp &a,const hp &b)
{
	return !(a==b);
}
 bool operator < (const hp &a, const hp &b)
 {
	 return compare(a,b)<0;
 }
 

// 
// 高精度数加法
// 
// 语法：plus(const hp &a,const hp &b,hp &c);
//  
// 参数：
//  
// a,b：
//  进行加法的高精度数字
//  
// 返回值：
//  返回相加结果到c中
//  
// 源程序：
//  
 

void plushp(const hp &a,const hp &b,hp &c)
{
int i,len;
for(i=1;i<=maxsize;i++) c.s[i]=0;
if(a.len>b.len) len=a.len;
else len=b.len;
for(i=1;i<=len;i++)
   {
   c.s[i]+=a.s[i]+b.s[i];
    if(c.s[i]>=10)
      {
      c.s[i]-=10;
      c.s[i+1]++;
      }
   }
if(c.s[len+1]>0) len++;
   c.len=len;
}
 

// 
// 高精度数减法
// 
// 语法：subtract(const hp &a,const hp &b,hp &c);
//  
// 参数：
//  
// a,b：
//  进行减法的高精度数字，a是被减数，b是减数，不支持负数
//  
// 返回值：
//  返回结果到c中
//  
// 源程序：
//  
//  

 void subtract(const hp &a,const hp &b,hp &c)
{
int i,len;
for(i=1;i<=maxsize;i++) c.s[i]=0;
if(a.len>b.len) len=a.len;
else len=b.len;
for(i=1;i<=len;i++)
   {
   c.s[i]+=a.s[i]-b.s[i];
    if(c.s[i]<0)
      {
      c.s[i]+=10;
      c.s[i+1]--;
      }
   }
while(len>1&&c.s[len]==0) len--;
   c.len=len;
}
 hp operator - (const hp &a,const hp &b)
 {
	 hp c;
	 subtract(a,b,c);
	 return c;
 }
//  
// 高精度乘10 
// 
// 语法：multiply10(hp &a);
//  
// 参数：
//  
// a：
//  进行乘法的高精度数字
//  
// 返回值：
//  返回结果到 a 中
//  
// 源程序：
//  
 

 void multiply10(hp &a)
{
int i;
for(i=a.len;i>=1;i--)
   a.s[i+1]=a.s[i];
a.s[1]=0;
a.len++;
while(a.len>1&&a.s[a.len]==0) a.len--;
}
 
// 
// 
// 高精度乘单精度
// 
// 语法：multiply(const hp &a,int b,hp &c);
//  
// 参数：
//  
// a：
//  进行乘法的高精度数字
//  
// b：
//  进行乘法的单精度数字
//  
// 返回值：
//  返回结果到 c 中
//  
// 源程序：
//  
//  

 void multiply(const hp &a,int b,hp &c)
{
int i,len;
for(i=1;i<=maxsize;i++) c.s[i]=0;
len=a.len;
for(i=1;i<=len;i++)
   {
   c.s[i]+=a.s[i]*b;
   c.s[i+1]+=c.s[i]/10;
   c.s[i]%=10;
   }
len++;
while(c.s[len]>=10)
   {
   c.s[len+1]+=c.s[len]/10;
   c.s[len]%=10;
   len++;
   }
while(len>1&&c.s[len]==0) len--;
c.len=len;
}
 
// 
// 
// 高精度乘高精度
// 
// 语法：multiplyh(const hp &a,const hp &b,hp &c);
//  
// 参数：
//  
// a,b：
//  进行乘法的高精度数字
//  
// 返回值：
//  返回结果到 c 中
//  
// 源程序：
//  
 

 void multiplyh(const hp &a,const hp &b,hp &c)
{
int i,j,len;
for(i=1;i<=maxsize;i++) c.s[i]=0;
for(i=1;i<=a.len;i++)
for(j=1;j<=b.len;j++)
   {
   c.s[i+j-1]+=a.s[i]*b.s[j];
   c.s[i+j]+=c.s[i+j-1]/10;
   c.s[i+j-1]%=10;
   }
len=a.len+b.len+1;
while(len>1&&c.s[len]==0) len--;
c.len=len;
}
 
// 
// 
// 高精度除单精度
// 
// 语法：divide(const hp &a,int b,hp &c,int &d);
//  
// 参数：
//  
// a：
//  进行除法的高精度数字
//  
// 返回值：
//  返回商到 c 中，余数到 d 中
//  
// 源程序：
//  
//  

 void divide(const hp &a,int b,hp &c,int &d)
{
int i,len;
for(i=1;i<=maxsize;i++) c.s[i]=0;
len=a.len;
d=0;
for(i=len;i>=1;i--)
   {
   d=d*10+a.s[i];
   c.s[i]=d/b;
   d%=b;
   }
while(len>1&&c.s[len]==0) len--;
c.len=len;
}
 
// 
// 
// 高精度除高精度
// 
// 语法：divideh(const hp &a,const hp &b,hp &c,hp &d);
//  
// 参数：
//  
// a，b：
//  进行除法的高精度数字
//  
// 返回值：
//  返回商到 c 中，余数到 d 中
//  
// 注意：
//  
//  
// 
//  需要compare、multiply10、subtract
//  
// 源程序：
//  
//  

 void divideh(const hp &a,const hp &b,hp &c,hp &d)
{
hp e;
int i,len;
for(i=1;i<=maxsize;i++)
   {
   c.s[i]=0;
   d.s[i]=0;
   }
len=a.len;
d.len=1;
for(i=len;i>=1;i--)
   {
   multiply10(d);
   d.s[1]=a.s[i];
    while(compare(d,b)>=0)
      {
      subtract(d,b,e);
      d=e;
      c.s[i]++;
      }
   }
while(len>1&&c.s[len]==0) len--;
c.len=len;
} 

 hp operator % (const hp &a, const hp &b)
 {
	 hp c,d;
divideh(a,b,c,d);
return d;
 }
//  
// 精度计算——乘法（大数乘大数） 语法：mult(char a[],char b[],char s[]);
//  
// 参数：
//  
// a[]：
//  被乘数，用字符串表示，位数不限
//  
// b[]：
//  乘数，用字符串表示，位数不限
//  
// t[]：
//  结果，用字符串表示
//  
// 返回值：
//  null
//  
// 注意：
//  
//  
// 
//  空间复杂度为 o(n^2)
//  
// 
//  需要 string.h
//  
// 源程序：
//  
 

 void mult(char a[],char b[],char s[])
{
    int i,j,k=0,alen,blen,sum=0,res[65][65]={0},flag=0;
    char result[65];
     alen=strlen(a);blen=strlen(b); 

    for (i=0;i<alen;i++)
    for (j=0;j<blen;j++) res[i][j]=(a[i]-'0')*(b[j]-'0');

    for (i=alen-1;i>=0;i--)
         {
            for (j=blen-1;j>=0;j--) sum=sum+res[i+blen-j-1][j];
             result[k]=sum%10;
             k=k+1;
             sum=sum/10;
         }

    for (i=blen-2;i>=0;i--)
         {
            for (j=0;j<=i;j++) sum=sum+res[i-j][j];
             result[k]=sum%10;
             k=k+1;
             sum=sum/10;
         }
    if (sum!=0) {result[k]=sum;k=k+1;}

    for (i=0;i<k;i++) result[i]+='0';
    for (i=k-1;i>=0;i--) s[i]=result[k-1-i];
     s[k]='\0';

    while(1)
         {
        if (strlen(s)!=strlen(a)&&s[0]=='0') 
             strcpy(s,s+1);
        else
            break;
         }
}
 

// 
// 精度计算——加法
// 
// 语法：add(char a[],char b[],char s[]);
//  
// 参数：
//  
// a[]：
//  被乘数，用字符串表示，位数不限
//  
// b[]：
//  乘数，用字符串表示，位数不限
//  
// t[]：
//  结果，用字符串表示
//  
// 返回值：
//  null
//  
// 注意：
//  
//  
// 
//  空间复杂度为 o(n^2)
//  
// 
//  需要 string.h
//  
// 源程序：
//  
 

 void add(char a[],char b[],char back[])
{
    int i,j,k,up,x,y,z,l;
    char *c;
    if (strlen(a)>strlen(b)) l=strlen(a)+2; else l=strlen(b)+2;
     c=(char *) malloc(l*sizeof(char));
     i=strlen(a)-1;
     j=strlen(b)-1;
     k=0;up=0;
    while(i>=0||j>=0)
         {
            if(i<0) x='0'; else x=a[i];
            if(j<0) y='0'; else y=b[j];
             z=x-'0'+y-'0';
            if(up) z+=1;
            if(z>9) {up=1;z%=10;} else up=0;
             c[k++]=z+'0';
             i--;j--;
         }
    if(up) c[k++]='1';
     i=0;
     c[k]='\0';
    for(k-=1;k>=0;k--)
         back[i++]=c[k];
     back[i]='\0';
} 
 
// 
// 
// 精度计算——减法
// 
// 语法：sub(char s1[],char s2[],char t[]);
//  
// 参数：
//  
// s1[]：
//  被减数，用字符串表示，位数不限
//  
// s2[]：
//  减数，用字符串表示，位数不限
//  
// t[]：
//  结果，用字符串表示
//  
// 返回值：
//  null
//  
// 注意：
//  
//  
// 
//  默认s1>=s2，程序未处理负数情况
//  
// 
//  需要 string.h
//  
// 源程序：
//  
//  

 void sub(char s1[],char s2[],char t[])
{
    int i,l2,l1,k;
     l2=strlen(s2);l1=strlen(s1);
     t[l1]='\0';l1--;
    for (i=l2-1;i>=0;i--,l1--)
         {
        if (s1[l1]-s2[i]>=0) 
             t[l1]=s1[l1]-s2[i]+'0';
        else
             {
             t[l1]=10+s1[l1]-s2[i]+'0';
             s1[l1-1]=s1[l1-1]-1;
             }
         }
     k=l1;
    while(s1[k]<0) {s1[k]+=10;s1[k-1]-=1;k--;}
    while(l1>=0) {t[l1]=s1[l1];l1--;}
loop:
    if (t[0]=='0') 
         {
         l1=strlen(s1);
        for (i=0;i<l1-1;i++) t[i]=t[i+1];
         t[l1-1]='\0';
         goto loop;
         }
    if (strlen(t)==0) {t[0]='0';t[1]='\0';}
} 
 
