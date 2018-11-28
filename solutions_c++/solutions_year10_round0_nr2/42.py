#include<iostream>
#include<string>
using namespace std;
const int MaxL=100;//支持的高精度整数位数 

class bignum 
{
      public:
	  bignum();
	  bignum(string);
 	  friend bignum operator+(const bignum&,const bignum&);
   	  friend bignum operator-(const bignum&,const bignum&);
   	  friend bignum operator*(const bignum&,const bignum&);
   	  friend bignum operator/(const bignum&,const bignum&);
	  friend bignum operator%(const bignum&,const bignum&);
	  void print();
	  int s[MaxL],l,sgn;
};
bignum::bignum()
{
    //初始化 即赋初值0 
	memset(s,0,sizeof(s));
	sgn=1;
	l=1;
}
bignum::bignum(string a)
{
    //将字符串a赋值给bignum 
	memset(s,0,sizeof(s));
	l=a.size();
	int t=0,k=0;
	if (a[0]=='-')
	{
       sgn=-1;
       t=1;
	} else sgn=1;
	for (int i=l-1;i>=t;--i)
	{
	 	s[k]=a[i]-'0';
	 	++k;
	}
	l=k;
}
int Sign(int a,int b)
{
 	if (a<b) return -1; else
 	if (a==b) return 0; else
  	   		  return 1;
}
int Compare(const bignum& a,const bignum& b)
{
    //高精大小比较 
	if (a.l!=b.l) return Sign(a.l,b.l);
	int i;
	i=a.l-1;
	while (i>0&&a.s[i]==b.s[i]) --i; 
	return Sign(a.s[i],b.s[i]);
}
bignum Plus(const bignum& a,const bignum& b)
{
    //正数间高精度相加 
	bignum c;
	c.l=a.l<b.l?b.l:a.l;
	int i,x=0;
	for (int i=0;i<c.l;++i)
	c.s[i]=a.s[i]+b.s[i];
	for (int i=0;i<c.l;++i)
	if (c.s[i]>9) 
    {
        c.s[i+1] += c.s[i]/10;
        c.s[ i ] %= 10;
    }
	if (c.s[c.l]>0) ++c.l;
	return c;
}
bignum Minus(const bignum& a,const bignum& b)
{
    //正数高精减高精 
	bignum c=a;
	int i;
	for (i=0;i<c.l;++i) 
    {
		c.s[i]-=b.s[i];
		if (c.s[i]<0) 
        {
			c.s[i]+=10;
			c.s[i+1]--;
		}
	}
	while (c.l>1 && c.s[c.l-1]==0) --c.l;
	return c;
}
bignum Multiply(const bignum& a,const bignum& b)
{
       //正数高精乘以高精 
       bignum c;
       if ((a.l==1&&a.s[0]==0)||(b.l==1&&b.s[0]==0)) return c;
       c.l=a.l+b.l-1;
       for (int i=0;i<a.l;++i)
           for (int j=0;j<b.l;++j)
           c.s[i+j]+=a.s[i]*b.s[j];
       for (int i=0;i<c.l;++i)
       {
          c.s[i+1]+=c.s[i]/10;
          c.s[i]%=10;
       }
       while (c.s[c.l]>0)
       {
             c.s[c.l+1]=c.s[c.l]/10;
             c.s[c.l]%=10;
             ++c.l;
       }
       return c;
           
}
bignum Divide(const bignum& a,const bignum& b)
{
    //正数高精除高精
  	bignum c;
    if (Compare(a,b)<0) return c;
	if (b.l==1&&b.s[0]==0) {cout<<"Wrong!!!"<<endl;return c;}
	bignum temp;
	for (int i=a.l-1;i>=0;--i)
	{
        if (temp.l>1||temp.s[0]>0)
        {
           for (int o=temp.l;o>0;--o)
           temp.s[o]=temp.s[o-1];
           temp.l++;
        }
        temp.s[0]=a.s[i];
        while (Compare(b,temp)<=0)
        {
              c.s[i]++;
              temp=Minus(temp,b);
        }
    }
	c.l=a.l;
	while (c.s[c.l-1]==0&&c.l>1) --c.l;
	return c;
}
bignum Mod(const bignum& a,const bignum& b)
{
    //正数高精Mod高精
    if (Compare(a,b)<0) return a;
	if (b.l==1&&b.s[0]==0) {cout<<"Wrong!!!"<<endl;return a;}
	bignum temp;
	for (int i=a.l-1;i>=0;--i)
	{
        if (temp.l>1||temp.s[0]>0)
        {
           for (int o=temp.l;o>0;--o)
           temp.s[o]=temp.s[o-1];
           temp.l++;
        }
        temp.s[0]=a.s[i];
        while (Compare(b,temp)<=0)
			   temp=Minus(temp,b);
    }
	return temp;
}
//重载操作符
bignum operator+(const bignum& a,const bignum& b)
{
    //高精度相加 
    bignum c;
    if (a.sgn==b.sgn)
    {
       c=Plus(a,b);
       c.sgn=a.sgn;
       return c;
	} else
	{
       if (Compare(a,b)<=0)
       {
       	  c=Minus(b,a); 
       	  c.sgn=b.sgn;
       }else
       {
	      c=Minus(a,b);
       	  c.sgn=a.sgn;
       }
       return c;
 	}
} 
bignum operator-(const bignum& a,const bignum& b)
{
      bignum c,d=b;
      d.sgn=-d.sgn;
      c=a+d;
      return c;
}
bignum operator*(const bignum& a,const bignum& b)
{
 	   bignum c;
 	   c=Multiply(a,b);
 	   c.sgn=a.sgn*b.sgn;
       return c;
}
bignum operator/(const bignum& a,const bignum& b)
{
 	   bignum c;
 	   c=Divide(a,b);
 	   c.sgn=a.sgn*b.sgn;
       return c;
}
bignum operator%(const bignum& a,const bignum& b)
{
 	   bignum c;
       c=Mod(a,b);
 	   c.sgn=a.sgn;
       return c;
}
void bignum::print()
{
    //高精度数字的输出 
	int i;
	if (l==1&&s[0]==0) printf("0\n"); else
	{
       if (sgn<0) printf("-");
	   for (i=l-1;i>=0;--i) printf("%d",s[i]);
	   printf("\n");
    };
}

int T,N;
bignum X[1010];

bignum gcd(bignum a,bignum b)
{
       if (Compare(a,b)<0) return gcd(b,a);
       if (Compare(b,bignum("0"))==0) return a; else
       return gcd(b,Mod(a,b));
}
void Solve(int Order)
{
     bignum d,tmp;
     d=bignum("0");
     for (int i=0;i<N;++i)
         for (int j=i+1;j<N;++j)
         {
             if (Compare(X[i],X[j])>=0)
             tmp=X[i]-X[j]; else
             tmp=X[j]-X[i];
             
//             tmp.print(); 
//             d.print(); 
             
             d=gcd(tmp,d);
//             d.print();
//             printf("**********\n");
         }
     
     bignum Ans=Mod(X[0],d);
     if (Compare(Ans,bignum("0"))>0) 
     {
         Ans=d-Ans;
     }
     cout<<"Case #"<<Order<<": ";
     Ans.print();
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>T;
    for (int i=0;i<T;++i)
    {
        cin>>N;
        string tmp;
        for (int j=0;j<N;++j)
        {
            cin>>tmp;
            X[j]=bignum(tmp);
        }
        Solve(i+1);
    }
    return(0);
}
