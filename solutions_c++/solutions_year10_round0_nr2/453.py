/*

 */
#include <iostream>
#include <string.h>
#include <cmath>
#define Max 100
using namespace std;
class Bignum
{
      public:
             int num[Max];
             int len;
             bool ispos;  //符号，true为正 
             void from(string &str)
             {
                  int i,j,j1;
                  len=str.length();
                  if (str[0]=='-') {
                                   len--;
                                   j1=len;
                                   ispos=false;
                                   }
                  else {
                       ispos=true;
                       j1=len-1;
                       }
                  for (i=1,j=j1 ; i<=len ;i++,j--)
                      num[i]=str[j]-'0';
             }
             
             void print()
             {
                  if (len==1 && num[len]==0) {
                     cout<<num[len];
                     return;
                     }
                  if (!ispos) cout<<'-';
                  for (int i=len;i>=1;i--) cout<<num[i];
             }
             
             void cpy(Bignum &p)
             {
                  ispos=p.ispos;
                  len=p.len;
                  for (int i=1;i<=len;i++)
                      num[i]=p.num[i];
             }
             
             void Mul10()
             {
                  for (int i=len+1;i>=2;i--)
                      num[i]=num[i-1];
                  num[1]=0;
                  len++;
                  while(len > 1 && num[len] == 0)  len--;
             }
             
             bool not0()
             {
                 for (int i=1;i<=len;i++)
                     if (num[i]!=0) return true;
                 return false;
             }
};
/////////////////////////////////////// 
bool Notlow(const Bignum &a , const Bignum &b)
{
     if (a.len != b.len) 
        return (a.len > b.len) ? true : false;
     for (int i=a.len; i >= 1; i--)
         if (a.num[i] != b.num[i]) 
            return  (a.num[i] > b.num[i]) ? true : false;
     return true;
}
Bignum add(Bignum a,Bignum b)
{
       Bignum c;
       int len=max(a.len,b.len);
       memset(c.num,0,sizeof(c.num));
       for (int i=1 ; i<=len ; i++) {
           if (i>a.len) a.num[i]=0;
           if (i>b.len) b.num[i]=0;
           c.num[i]+=(a.num[i]+b.num[i]);
           if (c.num[i]>=10) {
              c.num[i+1]++;
              c.num[i]-=10;
              }
           }
       if (c.num[len+1]!=0) len++;
       c.len=len;
       return c;
}
Bignum sub(Bignum a,Bignum b)
{
       Bignum c;
       int len=max(a.len,b.len);
       memset(c.num,0,sizeof(c.num));
       for (int i=1;i<=len;i++) {
           if (i>a.len) a.num[i]=0;
           if (i>b.len) b.num[i]=0;
           c.num[i]+=(a.num[i]-b.num[i]);
           if (c.num[i]<0) {
              c.num[i]+=10;
              c.num[i+1]--;
              }
           }
       while (c.num[len]==0 && len>1) len--;
       c.len=len;
       return c;
}
Bignum Mul_bb(Bignum &a, Bignum &b)   
{
       Bignum c;
       memset(c.num, 0, sizeof(c.num));
       if ( (a.len==1 && a.num[a.len]==0)||
            (b.len==1 && b.num[b.len]==0) ) {
          c.len=1;
          return c;
          } 
       int len = 0;
       for (int i = 1; i <= a.len; i++)
           for (int j = 1; j <= b.len; j++)
           {
               c.num[i+j-1] += (a.num[i]*b.num[j]);
               if (c.num[i+j-1] >= 10)
               {
                  c.num[i+j] += c.num[i+j-1]/10;
                  c.num[i+j-1] %= 10;
               }
           }
       len = a.len+b.len+1;   
       while(c.num[len] == 0 && len > 0) len--;   
       if(c.num[len+1]) len++;
       c.len=len;
       return  c;
}
Bignum Mul_bs(Bignum &a, int  &b)   
{   
    Bignum c;
    int len;
    len = a.len;
    memset(c.num, 0, sizeof(c.num));
    if(b == 0 || (a.len==1&&a.num[a.len]==0))    
    {
        c.len = 1;
        return  c;
    }
    for(int i = 1; i <= len; i++)
    {
        c.num[i] += (a.num[i]*b);
        if(c.num[i] >= 10)
        {
            c.num[i+1] = c.num[i]/10;
            c.num[i] %= 10;
        }
    }
    if (c.num[len+1]>0) len++;
    while(c.num[len] > 0)
    {
        c.num[len+1] = c.num[len]/10;
        c.num[len] %= 10;
        len++;
    }
    while (c.num[len]==0 && len>2) len--;
    c.len = len;
    return  c;
}
void Div1(Bignum &a, int &b, Bignum &c, int &f)   
{   
    int len = a.len;
    memset(c.num, 0, sizeof(c.num));   
    f = 0;   
    for (int i = a.len; i >= 1; i--)
    {   
        f = f*10+a.num[i];
        c.num[i] = f/b;
        f %= b;
    }
    while (len > 1 && c.num[len] == 0) len--;
    c.len = len;
}
void Div2(Bignum &a, Bignum &b, Bignum &c, Bignum &f)
{   
    int len = a.len;
    memset(c.num, 0, sizeof(c.num));
    memset(f.num, 0, sizeof(f.num));
    f.len = 1;
    for (int i = a.len;i >= 1;i--)
    {
        f.Mul10();
        f.num[1] = a.num[i];
        while (Notlow(f,b))
        {
              f = sub(f, b);
              c.num[i]++;
        }
    }
    while (len > 1 && c.num[len] == 0) len--;
    c.len = len;
}
/////////////////////////////////////////////////////// 
bool operator>=(const Bignum &a , const Bignum &b) 
{
     bool pos=true,q=true;
     if (a.ispos != b.ispos) 
        return (a.ispos && !b.ispos) ? true : false; 
     if (!a.ispos && !b.ispos) {
        pos=false;     //a,b均为负数时，异或取反得相反答案。
        for (int i=a.len; i >= 1; i--)
            if (a.num[i] != b.num[i]) q=false;
        if (q) return true;
        }
     return !(pos^Notlow(a,b));
}
Bignum operator+(Bignum a,Bignum b)
{
       Bignum c;
       if (a.ispos==b.ispos) {
                             c=add(a,b);
                             c.ispos=a.ispos;
                             }
       else {
            if (a>=b) {
                      if (Notlow(a,b)) {
                                       c=sub(a,b);
                                       c.ispos=a.ispos;
                                       }
                      else {
                           c=sub(b,a);
                           c.ispos=b.ispos;
                           }
                      }
            else {
                 if (Notlow(b,a)) {
                                  c=sub(b,a);
                                  c.ispos=b.ispos;
                                  }
                 else {
                      c=sub(a,b);
                      c.ispos=a.ispos;
                      }
                 }
            }
       return c;
}
Bignum operator-(Bignum a,Bignum b)
{
       b.ispos=!b.ispos;
       return a+b;
}
Bignum operator*(Bignum a,Bignum b)
{
       Bignum c;
       c=Mul_bb(a,b);
       c.ispos=!(a.ispos^b.ispos);
       return c;
}
Bignum operator*(Bignum a,int b)
{
       Bignum c;
       bool bispos=(bool)(b>0);
       b=abs(b);
       c=Mul_bs(a,b);
       c.ispos=!(a.ispos^bispos);
       return c;
}
Bignum operator/(Bignum a,Bignum b)
{
       Bignum c,d;
       Div2(a,b,c,d);
       c.ispos=!(a.ispos^b.ispos);
       return c;
}
Bignum operator/(Bignum a,int b)
{
       Bignum c;
       int d,b1=abs(b);
       bool bispos=(bool)(b>=0);
       Div1(a,b1,c,d);
       c.ispos=!(a.ispos^bispos);
       return c;
}
int    operator%(Bignum a,int b)
{
       Bignum c;
       int d,b1=abs(b);
       Div1(a,b1,c,d);
       return d;
}
Bignum operator%(Bignum a,Bignum b)
{
       Bignum c,d;
       Div2(a,b,c,d);
       d.ispos=!(a.ispos^b.ispos);
       return d;
}
///////////////////////////////////////////////////////// 
int Case,n,ca=0;
string str;
Bignum gcd(Bignum a,Bignum b)
{
	while (b.not0()) { Bignum t = a % b; a = b; b = t; }
	return a;
}

void display()
{
    cin>>Case;
    while (Case--) {
        ca++;
        cout<<"Case #"<<ca<<": ";
        Bignum d,tmp,t[1001];
        cin>>n;
        for (int i=1;i<=n;i++) {
            cin>>str;
            t[i].from(str);
            //t[i].print();cout<<endl;
            }
        bool flag=false;
        for (int i=1;i<n;i++)
            for (int j=i+1;j<=n;j++) {
                if (t[i]>=t[j]) tmp=t[i]-t[j];
                else tmp=t[j]-t[i];
                if (!tmp.not0()) continue;
                if (!flag) {
                    d=tmp;
                    flag=true;
                    }
                else d=gcd(d,tmp);
                }
        if (!d.not0()) cout<<0<<endl;
        else {
            tmp=(d-t[1]%d)%d;
            tmp.print();
            cout<<endl;
            }
        } 
}
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    display();
    return 0;
}

