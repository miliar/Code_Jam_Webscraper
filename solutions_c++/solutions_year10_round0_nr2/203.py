#include<stdio.h>
#include<memory.h>
#include<algorithm>
using namespace std;
/*
google code jam 2010
qualification
B Fair Warning
biggest T that ti%T=constent
y=T-constent

(ti-tj)%T=0
T=gcd(t(i)-t(i-1),i=1..n)
*/
typedef long long I;
#define BASE 10000
#define SIZE 20
typedef struct bignum10 BIG10;
struct bignum10{
	long len,data[SIZE];
	bignum10():len(0){}
	bignum10(const BIG10&v):len(v.len){memcpy(data,v.data,len*sizeof(*data));}
	bignum10(I v):len(0){for(;v;v/=BASE)data[len++]=v%BASE;}
	
public:
	long IsEven(){
		if(len==0)return 1;
		return !(data[0]&1);
	}
	long IsZero(){
		return len==0||(len==1&&data[0]==0);
	}
	BIG10&operator<<(const long cnt){
		if(len==0||cnt<=0)return *this;
		memcpy(data+cnt,data,len*sizeof(*data));
		memset(data,0,cnt*sizeof(*data));
		len+=cnt;
		return *this;
	}
	BIG10&operator=(const BIG10&v){
		len=v.len;
		memcpy(data,v.data,len*sizeof(*data));
		return *this;
	}
	long&operator[](long index){return data[index];}
	long operator[](long index)const{return data[index];}
	void print(char*s){
		if(len==0){s[0]='0';s[1]=0;return;}
		sprintf(s,"%ld",data[len-1]);
		long i;
		for(i=len-2;i>=0;i--)
			sprintf(s+strlen(s),"%04ld",data[i]);
	}
};
long compare(const BIG10&a,const BIG10&b){
	long i;
	if(a.len!=b.len)return a.len>b.len?1:-1;
	for(i=a.len-1;i>=0&&a[i]==b[i];i--);
	if(i<0)return 0;
	return a[i]>b[i]?1:-1;
}
bool operator==(const BIG10&a,const BIG10&b){return compare(a,b)==0;}
bool operator<(const BIG10&a,const BIG10&b){return compare(a,b)<0;}
BIG10 operator+(const BIG10&a,const BIG10&b){
	BIG10 ret;
	long i,c=0;
	for(i=0;i<a.len||i<b.len||c;i++){
		if(i<a.len)c+=a[i];
		if(i<b.len)c+=b[i];
		ret[i]=c%BASE;
		c/=BASE;
	}ret.len=i;
	return ret;
}
BIG10 operator-(const BIG10&a,const BIG10&b){
	BIG10 ret;
	long i,c=0;
	for(i=0;i<a.len;i++){
		ret[i]=a[i]-c;
		if(i<b.len)ret[i]-=b[i];
		if(ret[i]<0){c=1;ret[i]+=BASE;}
		else c=0;
	}while(i>0&&ret[i-1]==0)i--;
	ret.len=i;
	return ret;
}
BIG10 operator*(const BIG10&a,const long b){
	if(!b)return 0;
	BIG10 ret;
	I i,c=0;
	for(i=0;i<a.len||c;i++){
		if(i<a.len)c+=(I)a[i]*(I)b;
		ret[i]=c%BASE;
		c/=BASE;
	}ret.len=i;
	return ret;
}
BIG10 operator/(const BIG10&a,const long b){
	BIG10 ret;
	I i,c=0;
	for(i=a.len-1;i>=0;i--){
		c=c*BASE+a[i];
		ret[i]=c/b;
		c%=b;
	}ret.len=a.len;
	while(ret.len&&ret[ret.len-1]==0)ret.len--;
	return ret;
}
BIG10 operator%(const BIG10&a,const BIG10&b){
	BIG10 c;
	long i,lo,hi,mid;
	for(i=a.len-1;i>=0;i--){
		c=(c<<1)+a[i];
		lo=0;
		hi=BASE-1;
		while(lo<hi){
			mid=(lo+hi+1)/2;
			if(compare(b*mid,c)<=0)lo=mid;
			else hi=mid-1;
		}c=c-b*lo;
	}return c;
}
BIG10 read(char*s){
	long i;
	BIG10 ret;
	for(i=0;s[i];i++)ret=ret*10+(s[i]-'0');
	return ret;
}
BIG10 BigGCD(BIG10 a,BIG10 b){
	if(a<b)return BigGCD(b,a);
	if(b.IsZero())return a;
	if(a.IsEven()){
		if(b.IsEven())return BigGCD(a/2,b/2)*2;
		else return BigGCD(a/2,b);
	}else{
		if(b.IsEven())return BigGCD(a,b/2);
		else return BigGCD(b,a-b);
	}
}
I gcd(I a,I b){
	while(b){
		I t=a%b;
		a=b;
		b=t;
	}return a;
}
//I in[1010];
BIG10 in[1010];
char str[99];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	long z,zi=1;
	scanf("%ld",&z);
	while(z--){
		long n,i;
		scanf("%ld",&n);
		for(i=0;i<n;i++){
			scanf("%s",str);
			in[i]=read(str);
			//scanf("%I64d",in+i);
		}
		sort(in,in+n);
		for(i=n-1;i>0;i--)in[i]=in[i]-in[i-1];
		
		BIG10 ans(in[1]);
		//I ans=in[1];
		for(i=2;i<n;i++){
			ans=BigGCD(ans,in[i]);
			//ans=gcd(ans,in[i]);
		}
		BIG10 md=in[0]%ans;
		if(md.IsZero())
			ans=0;
		else
			ans=ans-md;
		ans.print(str);
		printf("Case #%ld: %s\n",zi++,str);
	}
	return 0;
}
