#include<stdio.h>
#include<string>
#include<math.h>
const long MAX=200;
const long radix=10;

typedef __int64 Int64;
class Bignum
{
public:
	long num[MAX];
	long bit;
	bool sign;
	Bignum(long x=0)
	{
		if(x>=0) sign=true;
		else sign=false,x=-x;
		bit=0;
		memset(num,0,sizeof(num));
		if(x==0) bit=1;
		while(x!=0) num[bit++]=x%radix, x/=radix;
	};
	void set(long x)
	{
		if(x>=0) sign=true;
		else sign=false,x=-x;
		bit=0;
		memset(num,0,sizeof(num));
		if(x==0) bit=1;
		while(x!=0) num[bit++]=x%radix, x/=radix;
	};
	void set(char x[])
	{
		char ch;
		if(x[0]!='-'){
			sign=true;
			bit=strlen(x);
			long i;
			memset(num,0,sizeof(num));
			for(i=0;i<bit;i++){
				ch=x[bit-i-1];
				if(ch<='9' && ch>='0') num[i]=ch-'0';
				else if(ch<='z' && ch>='a') num[i]=ch-'a'+10;
				else if(ch<='A' && ch>='A') num[i]=ch-'A'+10;
			}
		}else{
			sign=false;
			bit=strlen(x)-1;
			long i;
			memset(num,0,sizeof(num));
			for(i=0;i<bit;i++){
				ch=x[bit-i];
				if(ch<='9' && ch>='0') num[i]=ch-'0';
				else if(ch<='z' && ch>='a') num[i]=ch-'a'+10;
				else if(ch<='A' && ch>='A') num[i]=ch-'A'+10;
			}
		}
	};
	void print();
	bool abs_small(const Bignum &a,const Bignum &b);
	bool abs_equal(const Bignum &a,const Bignum &b);
	Bignum abs_add(const Bignum &a,const Bignum &b);
	Bignum abs_sub(const Bignum &a,const Bignum &b);
	Bignum operator +(const Bignum &b);
	Bignum operator -(const Bignum &b);
	Bignum operator *(const Bignum &b);
	Bignum operator *(const long &b);
	Bignum operator /(const Bignum &b);
	Bignum operator /(const long &b);
	Bignum operator %(const Bignum &b);
	Bignum& operator =(const Bignum& b);
	long operator %(const long &b);
	bool operator <(const Bignum &b);
	bool operator <=(const Bignum &b);
	bool operator >=(const Bignum &b);
	bool operator >(const Bignum &b);
	bool operator ==(const Bignum &b);
	bool operator !=(const Bignum &b);
};

Bignum& Bignum::operator =(const Bignum& b)
{
	sign=b.sign;
	bit=b.bit;
	memcpy(num,b.num,sizeof(num));
	return *this;
}

//绝对值比较，小于返回true
bool Bignum::abs_small(const Bignum &a, const Bignum &b)
{
	long i;
	if(a.bit<b.bit) return true;
	if(a.bit>b.bit) return false;
	for(i=a.bit-1;i>=0;i--){
		if(a.num[i]<b.num[i]) return true;
		if(a.num[i]>b.num[i]) return false;
	}
	return false;
}

//绝对值比较，相等返回true
bool Bignum::abs_equal(const Bignum &a, const Bignum &b)
{
	long i;
	if(a.bit!=b.bit) return false;
	for(i=a.bit-1;i>=0;i--){
		if(a.num[i]!=b.num[i]) return false;
	}
	return true;
}
//绝对值相加
Bignum Bignum::abs_add(const Bignum &a,const Bignum &b)
{
	Bignum tmp(0);
	long len,i,c;
	len=a.bit>b.bit?a.bit:b.bit;
	for(i=c=0;i<len;i++){
		c+=a.num[i]+b.num[i];
		if(c>=radix) tmp.num[i]=c-radix, c=1;
		else tmp.num[i]=c, c=0;
	}
	if(c!=0) tmp.num[i++]=c;
	tmp.bit=i;
	return tmp;
}

//绝对值相减
Bignum Bignum::abs_sub(const Bignum &a,const Bignum &b)
{
	Bignum tmp(0);
	long len,i,c=0;
	len=a.bit;
	for(i=0;i<len;i++){
		c=a.num[i]-c-b.num[i];
		if(c<0) tmp.num[i]=c+radix, c=1;
		else tmp.num[i]=c, c=0;
	}
	while(i>1 && tmp.num[i-1]==0) i--;
	tmp.bit=i;
	return tmp;
}

Bignum Bignum::operator +(const Bignum &b)
{
	Bignum tmp;
	Bignum a=*this;
	if(a.sign==b.sign){
		tmp=abs_add(a,b);
		tmp.sign=a.sign;
	}else if(abs_small(a,b)==true){
		tmp=abs_sub(b,a);
		tmp.sign=b.sign;
	}else{
		tmp=abs_sub(a,b);
		tmp.sign=a.sign;
	}
	if(tmp.num[0]==0 && tmp.bit==1) tmp.sign=true;
	return tmp;
}

Bignum Bignum::operator -(const Bignum &b)
{
	Bignum tmp;
	Bignum a=*this;
	if(a.sign!=b.sign){
		tmp=abs_add(a,b);
		tmp.sign=a.sign;
	}else if(abs_small(a,b)==true){
		tmp=abs_sub(b,a);
		tmp.sign=(b.sign==true?false:true);
	}else{
		tmp=abs_sub(a,b);
		tmp.sign=(a.sign==true?true:false);
	}
	if(tmp.num[0]==0 && tmp.bit==1) tmp.sign=true;
	return tmp;
}

Bignum Bignum::operator *(const Bignum &b)
{
	Bignum tmp(0);
	Bignum a=*this;
	long i,j;
	Int64 stmp;
	for(i=0;i<a.bit;i++){
		for(j=0;j<b.bit;j++){
			stmp=a.num[i];
			stmp=stmp*b.num[j]+tmp.num[i+j];
			tmp.num[i+j+1]+=stmp/radix;
			tmp.num[i+j]=stmp%radix;
		}
	}
	i=a.bit+b.bit;
	while(i>1 && tmp.num[i-1]==0) i--;
	tmp.bit=i;
	tmp.sign=(a.sign==b.sign?true:false);
	if(tmp.num[0]==0 && tmp.bit==1) tmp.sign=true;
	return tmp;
}

Bignum Bignum::operator *(const long &b)
{
	Bignum tmp(0);
	Bignum a=*this;
	long i,j,tb;
	Int64 c=0,stmp;
	if(b>0) tmp.sign=a.sign, tb=b;
	else tmp.sign=!a.sign, tb=-b;
	for(i=0;i<a.bit;i++){
		stmp=a.num[i];
		stmp*=tb;
		tmp.num[i]=(stmp+c)%radix;
		c=(stmp+c)/radix;
	}
	while(c!=0){
		tmp.num[i]=c%radix;
		c=c/radix;
		i++;
	}
	while(i>1 && tmp.num[i-1]==0) i--;
	tmp.bit=i;
	if(tmp.num[0]==0 && tmp.bit==1) tmp.sign=true;
	return tmp;
}

Bignum Bignum::operator /(const Bignum &b)
{
	Bignum tmp(0);
	Bignum a=*this;
	Bignum c(0);
	long i;
	for(i=a.bit-1;i>=0;i--){
		c=c*radix+a.num[i];
		while(c>=b) tmp.num[i]++, c=c-b;
	}
	i=a.bit;
	while(i>1 && tmp.num[i-1]==0) i--;
	tmp.bit=i;
	tmp.sign=(a.sign==b.sign?true:false);
	if(tmp.num[0]==0 && tmp.bit==1) tmp.sign=true;
	return tmp;
}

Bignum Bignum::operator /(const long &b)
{
	Bignum tmp(0);
	Bignum a=*this;
	long i,tb;
	Int64 c=0;
	if(b>0) tmp.sign=a.sign, tb=b;
	else tmp.sign=!a.sign, tb=-b;
	for(i=a.bit-1;i>=0;i--){
		c=c*radix+a.num[i];
		tmp.num[i]=c/tb;
		c=c%tb;
	}
	i=a.bit;
	while(i>1 && tmp.num[i-1]==0) i--;
	tmp.bit=i;
	if(tmp.num[0]==0 && tmp.bit==1) tmp.sign=true;
	return tmp;
}

Bignum Bignum::operator %(const Bignum &b)
{
	Bignum tmp(0);
	Bignum a=*this;
	long i;
	for(i=a.bit-1;i>=0;i--){
		tmp=tmp*radix+a.num[i];
		while(tmp>=b) tmp=tmp-b;
	}
	tmp.sign=a.sign;
	if(tmp.num[0]==0 && tmp.bit==1) tmp.sign=true;
	return tmp;
}

long Bignum::operator %(const long &b)
{
	Bignum tmp(0);
	Bignum a=*this;
	long i,tb;
	Int64 c=0;
	tb=b>0?b:-b;
	for(i=a.bit-1;i>=0;i--){
		c=c*radix+a.num[i];
		c=c%tb;
	}
	if(a.sign==false) c=-c;
	return c;
}

bool Bignum::operator <(const Bignum &b)
{
	Bignum a=*this;
	bool small,equal;
	small=abs_small(a,b);
	equal=abs_equal(a,b);
	if(a.sign==b.sign){
		if(a.sign==true) return small;
		else if(small==false && equal==false) return true;
		else return false;
	}else return b.sign;
}

bool Bignum::operator <=(const Bignum &b)
{
	Bignum a=*this;
	bool small,equal;
	small=abs_small(a,b);
	equal=abs_equal(a,b);
	if(a.sign==b.sign){
		if(a.sign==false) return !small;
		else if(small==true || equal==true) return true;
		else return false;
	}else return b.sign;
}

bool Bignum::operator >(const Bignum &b)
{
	Bignum a=*this;
	bool small,equal;
	small=abs_small(a,b);
	equal=abs_equal(a,b);
	if(a.sign==b.sign){
		if(a.sign==false) return small;
		else if(small==true || equal==true) return false;
		else return true;
	}else return a.sign;
}

bool Bignum::operator >=(const Bignum &b)
{
	Bignum a=*this;
	bool small,equal;
	small=abs_small(a,b);
	equal=abs_equal(a,b);
	if(a.sign==b.sign){
		if(a.sign==true) return !small;
		else if(small==false && equal==false) return false;
		else return true;
	}else return a.sign;
}

bool Bignum::operator ==(const Bignum &b)
{
	Bignum a=*this;
	if(a.sign==b.sign){
		return abs_equal(a,b);
	}else return false;
}

bool Bignum::operator !=(const Bignum &b)
{
	Bignum a=*this;
	if(a.sign==b.sign){
		return !abs_equal(a,b);
	}else return true;
}

void Bignum::print()
{
	long i;
	Bignum a=*this;
	if(a.sign==false) printf("-");
	printf("%d",a.num[a.bit-1]);
	for(i=a.bit-2;i>=0;i--) printf("%.1d",a.num[i]);
	printf("\n");
	return;
}

char str[MAX];
Bignum a[1024];
Bignum ret;
int n;

void gcd(Bignum* a, Bignum* b, Bignum& c)
{
	Bignum ta,tb,tmp;
	ta=*a;
	tb=*b;
	while(true){
		if(tb==0){
			c=ta;
			return;
		}else{
			tmp=ta;
			ta=tb;
			tb=tmp%tb;
		}
	}
	return;
}

void solve()
{
	int i;
	Bignum d;
	if(a[0]<a[1])d=a[1]-a[0];
	else d=a[0]-a[1];
	Bignum tmp;
	for(i=2;i<n;i++){
		if(a[i]>a[0])tmp=a[i]-a[0];
		else tmp=a[0]-a[i];
		gcd(&d,&tmp,d);
	}
	ret=a[0]%d;
	if(ret!=0) ret=d-ret;
	for(i=1;i<n;i++){
		tmp=a[i]%d;
		if(tmp!=0) tmp=d-tmp;
		if(tmp>ret) ret=tmp;
	}
}

int main()
{
	freopen("B-large.in.txt","r",stdin);
	freopen("b.out","w",stdout);
	int i,j,T;
	scanf("%d",&T);
	for(i=1;i<=T;i++){
		scanf("%d",&n);
		for(j=0;j<n;j++){
			scanf("%s",&str);
			a[j].set(str);
		}
		printf("Case #%d: ",i);
		solve();
		ret.print();
		printf("\n");
	}
	return 0;
}