#include<cstdio>
#include<cstring>
#include<iostream>

using namespace std;

#define DIGIT	4
#define BASE	10000
#define MAX		1000
#define SGN(x)	((x)>0?1:((x)<0?-1:0))
#define ABS(x)	((x)>0?(x):-(x))
typedef int BigIntegerArray[MAX+1];

int read(BigIntegerArray a,istream& is=cin){char buf[MAX*DIGIT+1],ch;int i,j;memset((void*)a,0,sizeof(BigIntegerArray));if(!(is>>buf))return 0;for(a[0]=strlen(buf),i=a[0]/2-1;i>=0;i--)ch=buf[i],buf[i]=buf[a[0]-1-i],buf[a[0]-1-i]=ch;for(a[0]=(a[0]+DIGIT-1)/DIGIT,j=strlen(buf);j<a[0]*DIGIT;buf[j++]='0');for(i=1;i<=a[0];i++)for(a[i]=0,j=0;j<DIGIT;j++)a[i]=a[i]*10+buf[i*DIGIT-1-j]-'0';for(;!a[a[0]]&&a[0]>1;a[0]--);return 1;}
int read(BigIntegerArray a,int &sign,istream& is=cin){char str[MAX*DIGIT+2],ch,*buf;int i,j;memset((void*)a,0,sizeof(BigIntegerArray));if(!(is>>str)) return 0;buf=str,sign=1;if(*buf=='-')sign=-1,buf++;for(a[0]=strlen(buf),i=a[0]/2-1;i>=0;i--)ch=buf[i],buf[i]=buf[a[0]-1-i],buf[a[0]-1-i]=ch;for(a[0]=(a[0]+DIGIT-1)/DIGIT,j=strlen(buf);j<a[0]*DIGIT;buf[j++]='0');for(i=1;i<=a[0];i++)for(a[i]=0,j=0;j<DIGIT;j++)a[i]=a[i]*10+buf[i*DIGIT-1-j]-'0';for(;!a[a[0]]&&a[0]>1;a[0]--);if(a[0]==1&&!a[1])sign=0;return 1;}
void write(const BigIntegerArray a,ostream& os=cout){int i,j;for(os<<a[i=a[0]],i--;i;i--)for(j=BASE/10;j;j/=10)os<<a[i]/j%10;}
int comp(const BigIntegerArray a,const BigIntegerArray b){int i;if(a[0]!=b[0])return a[0]-b[0];for(i=a[0];i;i--)if(a[i]!=b[i])return a[i]-b[i];return 0;}
int comp(const BigIntegerArray a,const int b){int c[12]={1};for(c[1]=b;c[c[0]]>=BASE;c[c[0]+1]=c[c[0]]/BASE,c[c[0]]%=BASE,c[0]++);return comp(a,c);}
int comp(const BigIntegerArray a,const int c,const int d,const BigIntegerArray b){int i,t=0,O=-BASE*2;if (b[0]-a[0]<d&&c)return 1;for (i=b[0];i>d;i--){t=t*BASE+a[i-d]*c-b[i];if(t>0)return 1;if(t<O)return 0;}for(i=d;i;i--){t=t*BASE-b[i];if(t>0) return 1;if(t<O)return 0;}return t>0;}
void add(BigIntegerArray a,const BigIntegerArray b){int i;for(i=1;i<=b[0];i++)if((a[i]+=b[i])>=BASE)a[i]-=BASE,a[i+1]++;if(b[0]>=a[0])a[0]=b[0];else for (;a[i]>=BASE&&i<a[0];a[i]-=BASE,i++,a[i]++);a[0]+=(a[a[0]+1]>0);}
void add(BigIntegerArray a,const int b){int i=1;for(a[1]+=b;a[i]>=BASE&&i<a[0];a[i+1]+=a[i]/BASE,a[i]%=BASE,i++);for(;a[a[0]]>=BASE;a[a[0]+1]=a[a[0]]/BASE,a[a[0]]%=BASE,a[0]++);}
void sub(BigIntegerArray a,const BigIntegerArray b){int i;for(i=1;i<=b[0];i++)if((a[i]-=b[i])<0)a[i+1]--,a[i]+=BASE;for(;a[i]<0;a[i]+=BASE,i++,a[i]--);for(;!a[a[0]]&&a[0]>1;a[0]--);}
void sub(BigIntegerArray a,const int b){int i=1;for(a[1]-=b;a[i]<0;a[i+1]+=(a[i]-BASE+1)/BASE,a[i]-=(a[i]-BASE+1)/BASE*BASE,i++);for(;!a[a[0]]&&a[0]>1;a[0]--);}
void sub(BigIntegerArray a,const BigIntegerArray b,const int c,const int d){int i,O=b[0]+d;for(i=1+d;i<=O;i++)if((a[i]-=b[i-d]*c)<0)a[i+1]+=(a[i]-BASE+1)/BASE,a[i]-=(a[i]-BASE+1)/BASE*BASE;for(;a[i]<0;a[i+1]+=(a[i]-BASE+1)/BASE,a[i]-=(a[i]-BASE+1)/BASE*BASE,i++);for(;!a[a[0]]&&a[0]>1;a[0]--);}
void mul(BigIntegerArray c,const BigIntegerArray a,const BigIntegerArray b){int i,j;memset((void*)c,0,sizeof(BigIntegerArray));for(c[0]=a[0]+b[0]-1,i=1;i<=a[0];i++)for(j=1;j<=b[0];j++)if((c[i+j-1]+=a[i]*b[j])>=BASE)c[i+j]+=c[i+j-1]/BASE,c[i+j-1]%=BASE;for(c[0]+=(c[c[0]+1]>0);!c[c[0]]&&c[0]>1;c[0]--);}
void mul(BigIntegerArray a,const int b){int i;for(a[1]*=b,i=2;i<=a[0];i++){a[i]*=b;if(a[i-1]>=BASE)a[i]+=a[i-1]/BASE,a[i-1]%=BASE;}for(;a[a[0]]>=BASE;a[a[0]+1]=a[a[0]]/BASE,a[a[0]]%=BASE,a[0]++);for(;!a[a[0]]&&a[0]>1;a[0]--);}
void mul(BigIntegerArray b,const BigIntegerArray a,const int c,const int d){int i;memset((void*)b,0,sizeof(BigIntegerArray));for(b[0]=a[0]+d,i=d+1;i<=b[0];i++)if((b[i]+=a[i-d]*c)>=BASE)b[i+1]+=b[i]/BASE,b[i]%=BASE;for(;b[b[0]+1];b[0]++,b[b[0]+1]=b[b[0]]/BASE,b[b[0]]%=BASE);for(;!b[b[0]]&&b[0]>1;b[0]--);}
void div(BigIntegerArray c,BigIntegerArray a,const BigIntegerArray b){int h,l,m,i;memset((void*)c,0,sizeof(BigIntegerArray));c[0]=(b[0]<a[0]+1)?(a[0]-b[0]+2):1;for(i=c[0];i;sub(a,b,c[i]=m,i-1),i--)for(h=BASE-1,l=0,m=(h+l+1)>>1;h>l;m=(h+l+1)>>1)if(comp(b,m,i-1,a)) h=m-1;else l=m;for(;!c[c[0]]&&c[0]>1;c[0]--);c[0]=c[0]>1?c[0]:1;}
void div(BigIntegerArray a,const int b,int& c){int i;for(c=0,i=a[0];i;c=c*BASE+a[i],a[i]=c/b,c%=b,i--);for(;!a[a[0]]&&a[0]>1;a[0]--);}
void sqrt(BigIntegerArray b,BigIntegerArray a){int h,l,m,i;memset((void*)b,0,sizeof(BigIntegerArray));for(i=b[0]=(a[0]+1)>>1;i;sub(a,b,m,i-1),b[i]+=m,i--)for(h=BASE-1,l=0,b[i]=m=(h+l+1)>>1;h>l;b[i]=m=(h+l+1)>>1)if(comp(b,m,i-1,a))h=m-1;else l=m;for(;!b[b[0]]&&b[0]>1;b[0]--);for(i=1;i<=b[0];b[i++]>>=1);}
int length(const BigIntegerArray a){int t,ret;for(ret=(a[0]-1)*DIGIT,t=a[a[0]];t;t/=10,ret++);return ret>0?ret:1;}
int digit(const BigIntegerArray a,const int b){int i,ret;for(ret=a[(b-1)/DIGIT+1],i=(b-1)%DIGIT;i;ret/=10,i--);return ret%10;}
int zeronum(const BigIntegerArray a){int ret,t;for(ret=0;!a[ret+1];ret++);for(t=a[ret+1],ret*=DIGIT;!(t%10);t/=10,ret++);return ret;}
void comp(int* a,const int l,const int h,const int d){int i,j,t;for(i=l;i<=h;i++)for(t=i,j=2;t>1;j++)while(!(t%j))a[j]+=d,t/=j;}
void convert(int* a,const int h,BigIntegerArray b){int i,j,t=1;memset(b,0,sizeof(BigIntegerArray));for(b[0]=b[1]=1,i=2;i<=h;i++)if(a[i])for(j=a[i];j;t*=i,j--)if(t*i>BASE)mul(b,t),t=1;mul(b,t);}
void combination(BigIntegerArray a,int m,int n){int* t=new int[m+1];memset((void*)t,0,sizeof(int)*(m+1));comp(t,n+1,m,1);comp(t,2,m-n,-1);convert(t,m,a);delete []t;}
void permutation(BigIntegerArray a,int m,int n){int i,t=1;memset(a,0,sizeof(BigIntegerArray));a[0]=a[1]=1;for(i=m-n+1;i<=m;t*=i++)if(t*i>BASE)mul(a,t),t=1;mul(a,t);}

struct BigInteger
{
	int sign;
	BigIntegerArray Numbers;
	inline BigInteger(){memset(Numbers,0,sizeof(BigIntegerArray));Numbers[0]=1;sign=0;}
	inline int operator!(){return Numbers[0]==1&&!Numbers[1];}
	inline BigInteger& operator=(const BigInteger& a){memcpy(Numbers,a.Numbers,sizeof(BigIntegerArray));sign=a.sign;return *this;}
	inline BigInteger& operator=(const int a){memset(Numbers,0,sizeof(BigIntegerArray));Numbers[0]=1;sign=SGN(a);add(Numbers,sign*a);return *this;};
	inline BigInteger& operator+=(const BigInteger& a){if(sign==a.sign)add(Numbers,a.Numbers);else if(sign&&a.sign){int ret=comp(Numbers,a.Numbers);if(ret>0)sub(Numbers,a.Numbers);else if(ret<0){BigIntegerArray t;memcpy(t,Numbers,sizeof(BigIntegerArray));memcpy(Numbers,a.Numbers,sizeof(BigIntegerArray));sub(Numbers,t);sign=a.sign;}else memset(Numbers,0,sizeof(BigIntegerArray)),Numbers[0]=1,sign=0;}else if(!sign)memcpy(Numbers,a.Numbers,sizeof(BigIntegerArray)),sign=a.sign;return *this;}
	inline BigInteger& operator+=(const int a){if(sign*a>0)add(Numbers,ABS(a));else if(sign&&a){int ret=comp(Numbers,ABS(a));if(ret>0)sub(Numbers,ABS(a));else if(ret<0){BigIntegerArray t;memcpy(t,Numbers,sizeof(BigIntegerArray));memset(Numbers,0,sizeof(BigIntegerArray));Numbers[0]=1;add(Numbers,ABS(a));sign=-sign;sub(Numbers,t);}else memset(Numbers,0,sizeof(BigIntegerArray)),Numbers[0]=1,sign=0;}else if(!sign)sign=SGN(a),add(Numbers,ABS(a));return *this;}
	inline BigInteger operator+(const BigInteger& a){BigInteger ret;memcpy(ret.Numbers,Numbers,sizeof(BigIntegerArray));ret.sign=sign;ret+=a;return ret;}
	inline BigInteger operator+(const int a){BigInteger ret;memcpy(ret.Numbers,Numbers,sizeof(BigIntegerArray));ret.sign=sign;ret+=a;return ret;}
	inline BigInteger& operator-=(const BigInteger& a){if(sign*a.sign<0)add(Numbers,a.Numbers);else if(sign&&a.sign){int ret=comp(Numbers,a.Numbers);if(ret>0)sub(Numbers,a.Numbers);else if(ret<0){BigIntegerArray t;memcpy(t,Numbers,sizeof(BigIntegerArray));memcpy(Numbers,a.Numbers,sizeof(BigIntegerArray));sub(Numbers,t);sign=-sign;}else memset(Numbers,0,sizeof(BigIntegerArray)),Numbers[0]=1,sign=0;}else if(!sign)add(Numbers,a.Numbers),sign=-a.sign;return *this;}
	inline BigInteger& operator-=(const int a){if(sign*a<0)add(Numbers,ABS(a));else if(sign&&a){int ret=comp(Numbers,ABS(a));if(ret>0)sub(Numbers,ABS(a));else if(ret<0){BigIntegerArray t;memcpy(t,Numbers,sizeof(BigIntegerArray));memset(Numbers,0,sizeof(BigIntegerArray));Numbers[0]=1;add(Numbers,ABS(a));sub(Numbers,t);sign=-sign;}else memset(Numbers,0,sizeof(BigIntegerArray)),Numbers[0]=1,sign=0;}else if(!sign)sign=-SGN(a),add(Numbers,ABS(a));return *this;}
	inline BigInteger operator-(const BigInteger& a){BigInteger ret;memcpy(ret.Numbers,Numbers,sizeof(BigIntegerArray));ret.sign=sign;ret-=a;return ret;}
	inline BigInteger operator-(const int a){BigInteger ret;memcpy(ret.Numbers,Numbers,sizeof(BigIntegerArray));ret.sign=sign;ret-=a;return ret;}
	inline BigInteger& operator*=(const BigInteger& a){BigIntegerArray t;mul(t,Numbers,a.Numbers);memcpy(Numbers,t,sizeof(BigIntegerArray));sign*=a.sign;return *this;}
	inline BigInteger& operator*=(const int a){mul(Numbers,ABS(a));sign*=SGN(a);return *this;}
	inline BigInteger operator*(const BigInteger& a){BigInteger ret;mul(ret.Numbers,Numbers,a.Numbers);ret.sign=sign*a.sign;return ret;}
	inline BigInteger operator*(const int a){BigInteger ret;memcpy(ret.Numbers,Numbers,sizeof(BigIntegerArray));mul(ret.Numbers,ABS(a));ret.sign=sign*SGN(a);return ret;}
	inline BigInteger& operator/=(const BigInteger& a){BigIntegerArray t;div(t,Numbers,a.Numbers);memcpy(Numbers,t,sizeof(BigIntegerArray));sign=(Numbers[0]==1&&!Numbers[1])?0:sign*a.sign;return *this;}
	inline BigInteger& operator/=(const int a){int t;div(Numbers,ABS(a),t);sign=(Numbers[0]==1&&!Numbers[1])?0:sign*SGN(a);return *this;}
	inline BigInteger operator/(const BigInteger& a){BigInteger ret;BigIntegerArray t;memcpy(t,Numbers,sizeof(BigIntegerArray));div(ret.Numbers,t,a.Numbers);ret.sign=(ret.Numbers[0]==1&&!ret.Numbers[1])?0:sign*a.sign;return ret;}
	inline BigInteger operator/(const int a){BigInteger ret;int t;memcpy(ret.Numbers,Numbers,sizeof(BigIntegerArray));div(ret.Numbers,ABS(a),t);ret.sign=(ret.Numbers[0]==1&&!ret.Numbers[1])?0:sign*SGN(a);return ret;}
	inline BigInteger& operator%=(const BigInteger& a){BigIntegerArray t;div(t,Numbers,a.Numbers);if (Numbers[0]==1&&!Numbers[1])sign=0;return *this;}
	inline int operator%=(const int a){int t;div(Numbers,ABS(a),t);memset(Numbers,0,sizeof(BigIntegerArray));Numbers[0]=1;add(Numbers,t);return t;}
	inline BigInteger operator%(const BigInteger& a){BigInteger ret;BigIntegerArray t;memcpy(ret.Numbers,Numbers,sizeof(BigIntegerArray));div(t,ret.Numbers,a.Numbers);ret.sign=(ret.Numbers[0]==1&&!ret.Numbers[1])?0:sign;return ret;}
	inline int operator%(const int a){BigInteger ret;int t;memcpy(ret.Numbers,Numbers,sizeof(BigIntegerArray));div(ret.Numbers,ABS(a),t);memset(ret.Numbers,0,sizeof(BigIntegerArray));ret.Numbers[0]=1;add(ret.Numbers,t);return t;}
	inline BigInteger& operator++(){*this+=1;return *this;}
	inline BigInteger& operator--(){*this-=1;return *this;};
	inline int operator>(const BigInteger& a) const {return sign>0?(a.sign>0?comp(Numbers,a.Numbers)>0:1):(sign<0?(a.sign<0?comp(Numbers,a.Numbers)<0:0):a.sign<0);}
	inline int operator>(const int a) const {return sign>0?(a>0?comp(Numbers,a)>0:1):(sign<0?(a<0?comp(Numbers,-a)<0:0):a<0);}
	inline int operator>=(const BigInteger& a) const {return sign>0?(a.sign>0?comp(Numbers,a.Numbers)>=0:1):(sign<0?(a.sign<0?comp(Numbers,a.Numbers)<=0:0):a.sign<=0);}
	inline int operator>=(const int a) const {return sign>0?(a>0?comp(Numbers,a)>=0:1):(sign<0?(a<0?comp(Numbers,-a)<=0:0):a<=0);}
	inline int operator<(const BigInteger& a) const {return sign<0?(a.sign<0?comp(Numbers,a.Numbers)>0:1):(sign>0?(a.sign>0?comp(Numbers,a.Numbers)<0:0):a.sign>0);}
	inline int operator<(const int a) const {return sign<0?(a<0?comp(Numbers,-a)>0:1):(sign>0?(a>0?comp(Numbers,a)<0:0):a>0);}
	inline int operator<=(const BigInteger& a) const {return sign<0?(a.sign<0?comp(Numbers,a.Numbers)>=0:1):(sign>0?(a.sign>0?comp(Numbers,a.Numbers)<=0:0):a.sign>=0);}
	inline int operator<=(const int a) const {return sign<0?(a<0?comp(Numbers,-a)>=0:1):(sign>0?(a>0?comp(Numbers,a)<=0:0):a>=0);}
	inline int operator==(const BigInteger& a) const {return (sign==a.sign)?!comp(Numbers,a.Numbers):0;}
	inline int operator==(const int a) const {return (sign*a>=0)?!comp(Numbers,ABS(a)):0;}
	inline int operator!=(const BigInteger& a) const {return (sign==a.sign)?comp(Numbers,a.Numbers):1;}
	inline int operator!=(const int a) const {return (sign*a>=0)?comp(Numbers,ABS(a)):1;}
	inline int operator[](const int a) const {return digit(Numbers,a);}
	friend inline istream& operator>>(istream& is,BigInteger& a){read(a.Numbers,a.sign,is);return is;}
	friend inline ostream& operator<<(ostream& os,const BigInteger& a){if(a.sign<0)os<<'-';write(a.Numbers,os);return os;}
	friend inline BigInteger sqrt(const BigInteger& a){BigInteger ret;BigIntegerArray t;memcpy(t,a.Numbers,sizeof(BigIntegerArray));sqrt(ret.Numbers,t);ret.sign=ret.Numbers[0]!=1||ret.Numbers[1];return ret;}
	friend inline BigInteger sqrt(const BigInteger& a,BigInteger& b){BigInteger ret;memcpy(b.Numbers,a.Numbers,sizeof(BigIntegerArray));sqrt(ret.Numbers,b.Numbers);ret.sign=ret.Numbers[0]!=1||ret.Numbers[1];b.sign=b.Numbers[0]!=1||ret.Numbers[1];return ret;}
	inline int length(){return ::length(Numbers);}
	inline int zeronum(){return ::zeronum(Numbers);}
	inline BigInteger C(const int m,const int n){combination(Numbers,m,n);sign=1;return *this;}
	inline BigInteger P(const int m,const int n){permutation(Numbers,m,n);sign=1;return *this;}
};

#define IN "B-large.in"
#define OUT "B-large.out"

BigInteger GCD(BigInteger a,BigInteger b)
{
	while(b!=0)
	{
		BigInteger r=a%b;
		a=b;
		b=r;
	}
	return a;
}

#define MAX_N 1000

int N;
BigInteger t[MAX_N+1];

BigInteger T;

int main()
{
	freopen(IN,"r",stdin);
	freopen(OUT,"w",stdout);

	int caseN;
	cin>>caseN;
	for(int caseID=1;caseID<=caseN;caseID++)
	{
		cin>>N;
		for(int i=0;i<N;i++) cin>>t[i];
		sort(t,t+N);

		T=0;
		for(int i=1;i<N;i++)
		{
			BigInteger d=t[i-1]-t[i];
			if(d==0) continue;
			if(d<0) d*=-1;
			T=GCD(T,d);
		}

		BigInteger x=t[0]/T+(t[0]%T==0?0:1);
		cout<<"Case #"<<caseID<<": "<<x*T-t[0]<<endl;
	}
	return 0;
}
