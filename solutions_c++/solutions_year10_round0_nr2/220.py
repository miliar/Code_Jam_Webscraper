#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <iostream>
#include <functional>
#include <sstream>
#include <numeric>

#define CLR( x , y ) ( memset( (x) , (y) , sizeof( (x) ) ) )
#define EPS 1e-9

using namespace std;

FILE *in=fopen("QB.in","r");
FILE *out=fopen("QB.out","w");

class bigint{
public:
	int size;
	int sign;
	int num[1000];

	bigint()
	{
		CLR(num,0);
		size=1;
		sign=1;
	}

	bigint(int x)
	{
		CLR(num,0);size=0;
		sign=(x>=0);
		if(x<0)x*=-1;
		while(x){
			num[size++]=x%10;
			x/=10;
		}
		if(!size)size=1;
	}

	bigint(string x)
	{
		sign=1;
		if(x[0]=='-'){
			sign=0;
			x.erase(x.begin());
		}
		CLR(num,0);size=x.size();
		for(int i=0;i<size;i++)num[i]=x[size-i-1]-'0';
	}
	bigint(char x[])
	{
		int d=strlen(x),start=0;
		sign=1;
		if(x[0]=='-'){
			sign=0;
			start=1;
		}
		CLR(num,0);size=d-start;
		for(int i=start;i<d;i++)num[i-start]=x[d-i-1+start]-'0';
	}

	void scan()
	{
		CLR(num,0);size=0;
		char j;
		while(1){
			if(fscanf(in,"%c",&j)==EOF){
				//num[0]=23;
				return ;
			}
			if(j=='\n' || j==' ')break;
			num[size++]=j-'0';
		}
		reverse(num,num+size);
	}


	void print()
	{
		if(!sign)fprintf(out,"-");
		for(int i=size-1;i>=0;i--)
			fprintf(out,"%d",num[i]);
		fprintf(out,"\n");
	}

};

int compare(bigint a,bigint b)
{
	if(a.size!=b.size)return a.size>b.size?1:-1;
	for(int i=a.size-1;i>=0;i--){
		if(a.num[i]>b.num[i])return 1;
		if(a.num[i]<b.num[i])return -1;
	}
	return 0;
}

bool operator<(bigint a,bigint b)
{
	if(a.sign!=b.sign){
		if(a.sign==0)return 1;
		return 0;
	}
	if(a.size>b.size)return !a.sign;
	if(a.size<b.size)return a.sign;
	for(int i=a.size-1;i>=0;i--){
		if(a.num[i]>b.num[i])return !a.sign;
		if(a.num[i]<b.num[i])return a.sign;
	}
	return 0;
}

bool operator>(bigint a,bigint b)
{
	return b<a;
}
bool operator>=(bigint a,bigint b)
{
	return !(a<b);
}
bool operator<=(bigint a,bigint b)
{
	return !(a>b);
}
bool operator==(bigint a,bigint b)
{
	if(a.sign!=b.sign)return 0;
	if(a.size!=b.size)return 0;
	for(int i=a.size-1;i>=0;i--)if(a.num[i]!=b.num[i])return 0;
	return 1;
}
bool operator!=(bigint a,bigint b)
{
	return !(a==b);
}
void zero_justify(bigint &a)
{
	while(a.size){
		if(a.num[a.size-1])break;
		a.size--;
	}
	if(!a.size)a.size=1,a.sign=1;
}


bigint operator+(bigint a,bigint b)
{
	bigint ret;
	int carry=0,i;
	int d=max(a.size,b.size);
	if(a.sign==b.sign){
		for(i=0;i<d+1;i++){
			ret.num[i]=(a.num[i]+b.num[i]+carry)%10;
			carry=(a.num[i]+b.num[i]+carry)/10;
		}
		ret.size=d+1;
		ret.sign=a.sign;
		zero_justify(ret);
	}
	else {
		if(compare(a,b)<0)ret=b+a;
		else {
			for(i=0;i<d;i++){
				ret.num[i]=(a.num[i]-b.num[i]-carry+10)%10;
				carry=(a.num[i]-b.num[i]-carry)<0;
			}
			ret.size=d;
			ret.sign=a.sign;
			zero_justify(ret);
		}
	}
	return ret;
}
bigint operator-(bigint a,bigint b)
{
	b.sign^=1;
	return a+b;
}
bigint operator*(bigint a,bigint b)
{
	int carry=0,i,j,sum;
	int d=max(a.size,b.size);
	bigint ret;
	ret.size=2*d;
	if(a.sign==b.sign)ret.sign=1;
	else ret.sign=0;
	for(i=0;i<2*d;i++){
		sum=carry;
		for(j=0;j<=i;j++)sum+=a.num[j]*b.num[i-j];
		carry=sum/10;
		ret.num[i]=sum%10;
	}
	zero_justify(ret);
	return ret;
}
bigint operator<<(bigint a,int x)
{
	bigint ret;
	ret.size=a.size+x;
	ret.sign=a.sign;
	if(a.size==1 && a.num[0]==0)return a;
	for(int i=0;i<a.size;i++)
		ret.num[i+x]=a.num[i];
	return ret;
}


bigint operator^(bigint a,int p)
{
	bigint ret=bigint(1),now=a;
	for(int i=0;i<11;i++){
		if(p&(1<<i))ret=ret*now;
		now=now*now;
	}
	return ret;
}

bigint divide(bigint a,bigint b,int f)
{
	bigint ret,rem;
	int i,j;
	if(b.size==1 && b.num[0]==0)return b;
	if(a.sign==b.sign)ret.sign=1;
	else ret.sign=0;
	b.sign=1;
	for(i=a.size-1;i>=0;i--){
		rem=(rem<<1)+a.num[i];
		for(j=0;rem>=b;j++)
			rem=rem-b;
		ret.num[ret.size++]=j;
	}
	rem.sign=a.sign;
	reverse(ret.num,ret.num+ret.size);
	zero_justify(rem);
	zero_justify(ret);
	if(f)return rem;
	return ret;
}
bigint operator/(bigint a,bigint b)
{
	return divide(a,b,0);
}
bigint operator%(bigint a,bigint b)
{
	return divide(a,b,1);
}


bigint ar[1100];

bigint gcd(bigint a,bigint b)
{
	if(b==0)return a;
	return gcd(b,a%b);
}
int main()
{
	int i,j,k;
	int n;
	int test,tests;
	fscanf(in,"%d\n",&tests);
	for(test=1;test<=tests;test++){
		fscanf(in,"%d ",&n);
		for(i=0;i<n;i++)ar[i].scan();
		sort(ar,ar+n);
		bigint ret=ar[1]-ar[0];
		for(i=2;i<n;i++)ret=gcd(ret,ar[i]-ar[i-1]);
		if(ret<=1)fprintf(out,"Case #%d: 0\n",test);
		else {
			fprintf(out,"Case #%d: ",test);
			bigint ans=(ret-ar[0]%ret)%ret;
			ans.print();
		}
	}
	return 0;
}