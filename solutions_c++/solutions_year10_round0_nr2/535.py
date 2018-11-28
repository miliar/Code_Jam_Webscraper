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
// �߾������Ƚ�
// 
// �﷨��int result=compare(const hp &a,const hp &b);
//  
// ������
//  
// a,b��
//  ���бȽϵĸ߾�������
//  
// ����ֵ��
//  �ȽϽ����a>b����������a=b����0��a<b���ظ���
//  
// Դ����
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
// �߾������ӷ�
// 
// �﷨��plus(const hp &a,const hp &b,hp &c);
//  
// ������
//  
// a,b��
//  ���мӷ��ĸ߾�������
//  
// ����ֵ��
//  ������ӽ����c��
//  
// Դ����
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
// �߾���������
// 
// �﷨��subtract(const hp &a,const hp &b,hp &c);
//  
// ������
//  
// a,b��
//  ���м����ĸ߾������֣�a�Ǳ�������b�Ǽ�������֧�ָ���
//  
// ����ֵ��
//  ���ؽ����c��
//  
// Դ����
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
// �߾��ȳ�10 
// 
// �﷨��multiply10(hp &a);
//  
// ������
//  
// a��
//  ���г˷��ĸ߾�������
//  
// ����ֵ��
//  ���ؽ���� a ��
//  
// Դ����
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
// �߾��ȳ˵�����
// 
// �﷨��multiply(const hp &a,int b,hp &c);
//  
// ������
//  
// a��
//  ���г˷��ĸ߾�������
//  
// b��
//  ���г˷��ĵ���������
//  
// ����ֵ��
//  ���ؽ���� c ��
//  
// Դ����
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
// �߾��ȳ˸߾���
// 
// �﷨��multiplyh(const hp &a,const hp &b,hp &c);
//  
// ������
//  
// a,b��
//  ���г˷��ĸ߾�������
//  
// ����ֵ��
//  ���ؽ���� c ��
//  
// Դ����
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
// �߾��ȳ�������
// 
// �﷨��divide(const hp &a,int b,hp &c,int &d);
//  
// ������
//  
// a��
//  ���г����ĸ߾�������
//  
// ����ֵ��
//  �����̵� c �У������� d ��
//  
// Դ����
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
// �߾��ȳ��߾���
// 
// �﷨��divideh(const hp &a,const hp &b,hp &c,hp &d);
//  
// ������
//  
// a��b��
//  ���г����ĸ߾�������
//  
// ����ֵ��
//  �����̵� c �У������� d ��
//  
// ע�⣺
//  
//  
// 
//  ��Ҫcompare��multiply10��subtract
//  
// Դ����
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
// ���ȼ��㡪���˷��������˴����� �﷨��mult(char a[],char b[],char s[]);
//  
// ������
//  
// a[]��
//  �����������ַ�����ʾ��λ������
//  
// b[]��
//  ���������ַ�����ʾ��λ������
//  
// t[]��
//  ��������ַ�����ʾ
//  
// ����ֵ��
//  null
//  
// ע�⣺
//  
//  
// 
//  �ռ临�Ӷ�Ϊ o(n^2)
//  
// 
//  ��Ҫ string.h
//  
// Դ����
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
// ���ȼ��㡪���ӷ�
// 
// �﷨��add(char a[],char b[],char s[]);
//  
// ������
//  
// a[]��
//  �����������ַ�����ʾ��λ������
//  
// b[]��
//  ���������ַ�����ʾ��λ������
//  
// t[]��
//  ��������ַ�����ʾ
//  
// ����ֵ��
//  null
//  
// ע�⣺
//  
//  
// 
//  �ռ临�Ӷ�Ϊ o(n^2)
//  
// 
//  ��Ҫ string.h
//  
// Դ����
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
// ���ȼ��㡪������
// 
// �﷨��sub(char s1[],char s2[],char t[]);
//  
// ������
//  
// s1[]��
//  �����������ַ�����ʾ��λ������
//  
// s2[]��
//  ���������ַ�����ʾ��λ������
//  
// t[]��
//  ��������ַ�����ʾ
//  
// ����ֵ��
//  null
//  
// ע�⣺
//  
//  
// 
//  Ĭ��s1>=s2������δ���������
//  
// 
//  ��Ҫ string.h
//  
// Դ����
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
 
