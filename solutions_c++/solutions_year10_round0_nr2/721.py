#include <string>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <stack>
#include <queue>
#include <algorithm>
#include <deque>
#include <utility>
#include <sstream>
#include <vector>
#include <map>
#include <ctime>
#include <memory.h>
#include <set>
using namespace std;
#define sz size()
#define vi vector<int>
#define vs vector<string>
#define dsz size()-1
#define pb push_back
#define maxn(a,b) (a) = ((a) < (b) ? (b) : (a))
#define FUP(ii,ss,ff) for ((ii) = (ss);(ii) <= (ff);(ii)++)
#define FDOWN(ii,ss,ff) for ((ii) = (ss);(ii) >= (ff);(ii)--)
#define FALL(ii, vv) for ((ii) = 0;signed (ii) <= signed ((vv).dsz);(ii)++)
#define ITERATE(__it,__container) for(__it=__container.begin(); __it!=__container.end(); __it++)
#define EPS 1e-12
#define INF 2147483647
#define sgn(x) ((x)>0 ? 1 : (x)==0 ? 0 : -1)
#define sq(x) ((x)*(x))
#define sorta(a) sort(a.begin(), a.end())
#define cleara(a, b) memset(a, b, sizeof(a))
#define ALL(a) a.begin(), a.end()
#define absd(a) ((a)<0?-(a):(a))
#define absm absd
#define mp make_pair
typedef unsigned int uint;
typedef long long ll;

class bignum{
public:
	bignum(){
		size=all_size=base=sg=allocated=0;
		bn=new int[64];
		bn++;
		bn[-1]=1;
		init();
	}
	bignum(long long num){
		size=all_size=base=sg=allocated=0;
		bn=new int[1];
		bn++;
		bn[-1]=1;
		init();
		*this=num;
	}
	bignum(const bignum& num){
		sg=num.sg;
		base=num.base;
		size=num.size;
		all_size=num.all_size;
		allocated=num.allocated;
		bn=num.bn;
		bn[-1]++;
	}
	~bignum(){
		if (!--bn[-1])
			delete [] &bn[-1];
	}
	void init(int _base=32768, int _all_size=8){
		base=_base;
		all_size=_all_size;
		size=0;
		allocated=0;
		sg=0;
		if (!--bn[-1])
			delete [] &bn[-1];
		bn=new int[all_size+1];
		bn++;
		bn[-1]=1;
	}
	void unref(){
		if (--bn[-1]){
			int* old_bn=bn;
			bn=new int[size+1];
			bn++;
			allocated=size;
			memcpy(bn,old_bn,size*sizeof(int));
			bn[-1]=0;
		}
		bn[-1]++;
	}
	bignum& operator =(long long num){
		clear();
		resize(65);
		unsigned long long t;
		int i=0;
		if (num<0){
			sg=1;
			t=-num;
		}else t=num;
		while (t){
			bn[i++]=(int)t%base;
			t/=base;
		}
		return trim();
	}
	bignum& operator =(bignum num){
		if (!--bn[-1])
			delete [] &bn[-1];
		sg=num.sg;
		base=num.base;
		bn=num.bn;
		size=num.size;
		all_size=num.all_size;
		allocated=num.allocated;
		bn[-1]++;
		return *this;
	}
	bignum operator +(bignum& num){
		bignum ret=*this;
		return ret+=num;
	}
	bignum& operator +=(const bignum& num){
		return *this+=(bignum&)num;
	}
	bignum& operator +=(bignum& num){
		int i,carry=0;
		bignum t;
		bignum& op=t;
		unref();
		if (num.sg^sg){
			if (sg){
				sg=0;
				*this=num-(*this);
			}else{
				num.sg=0;
				*this-=num;
				num.sg=1;
			}
			return *this;
		}
		resize(max(num.size,size)+1);
		if (base==num.base)
			op=num;
		else{
			t.init(base,all_size);
			t.convert(num);
		}
		for(i=0; carry||i<op.size; i++){
			bn[i]+=carry;
			if (i<op.size)
				bn[i]+=op.bn[i];
			if (bn[i]>=base){
				carry=1;
				bn[i]-=base;
			}else
				carry=0;
		}
		return trim();
	}
	bignum operator -(bignum& num){
		bignum ret=*this;
		return ret-=num;
	}
	bignum& operator -=(const bignum& num){
		return *this-=(bignum&)num;
	}
	bignum& operator -=(bignum& num){
		int i,carry=0;
		bignum t;
		bignum& op=t;
		unref();
		if (num.sg^sg){
			if (sg){
				sg=0;
				*this+=num;
				sg=1;
			}else{
				num.sg=0;
				*this+=num;
				num.sg=1;
			}
			return *this;
		}
		if (base==num.base)
			op=num;
		else{
			t.init(base,all_size);
			t.convert(num);
		}
		if (sg?(*this > op):(*this < op)){
			*this=op-*this;
			sg=1-sg;
			return *this;
		}
		resize(max(num.size,size)+1);
		for(i=0; carry||i<op.size; i++){
			bn[i]-=carry;
			if (i<op.size)
				bn[i]-=op.bn[i];
			if(bn[i]<0){
				carry=1;
				bn[i]+=base;
			}else
				carry=0;
		}
		return trim();
	}
	bignum operator *(const bignum& num){
		return *this*(bignum&)num;
	}
	bignum operator *(bignum& num){
		bignum ret,t;
		bignum& op=t;
		int rsg;
		if (base==num.base)
			op=num;
		else{
			t.init(base,all_size);
			t.convert(num);
		}
		if (size*op.size>2500 && min(size,op.size)>10){
			rsg=sg^op.sg;
			sg=op.sg=0;
			ret=mul_ksuba(op);
			ret.sg=rsg;
			return ret;
		}
		else
			return mul_brute(op);
	}
	bignum mul_brute(bignum& op){
		int i,j,carry=0;
		bignum ret;
		ret.init(base,all_size);
		ret.sg = sg^op.sg;
		ret.resize(op.size+size);
		FUP(i,0,size-1){
			for (j=0; carry || j<op.size; j++){
				ret.bn[i+j]+=carry;
				if (j<op.size)
					ret.bn[i+j]+=bn[i]*op.bn[j];
				carry=ret.bn[i+j]/base;
				ret.bn[i+j]%=base;
			}
		}
		return ret.trim();
	}
	bignum mul_ksuba(bignum& op){
		int divs0;
		bignum a0,a1,b0,b1,p1,p2,p3,t;
		a0.base=a1.base=b0.base=b1.base=p1.base=p2.base=p3.base=t.base=base;
		divs0=(max(size,op.size)+1)/2;
		a0.resize(min(this->size, divs0));
		a1.resize(max(this->size-divs0, 0));
		b0.resize(min(op.size, divs0));
		b1.resize(max(op.size-divs0, 0));
		memcpy(a0.bn,this->bn,a0.size*sizeof(int));
		memcpy(a1.bn,this->bn+a0.size,a1.size*sizeof(int));
		memcpy(b0.bn,op.bn,b0.size*sizeof(int));
		memcpy(b1.bn,op.bn+b0.size,b1.size*sizeof(int));
		a0.trim();
		a1.trim();
		b0.trim();
		b1.trim();
		p1=a0*b0;
		p2=(a0+a1)*(b0+b1);
		p3=a1*b1;
		p2-=p1+p3;
		if (p1.size>divs0){
			t.resize(p1.size-divs0);
			memcpy(t.bn, p1.bn+divs0, t.size*sizeof(int));
			p2+=t;
		}
		if (p2.size>divs0){
			t.resize(p2.size-divs0);
			memcpy(t.bn, p2.bn+divs0, t.size*sizeof(int));
			p3+=t;
		}
		p1.resize(2*divs0+p3.size);
		memcpy(p1.bn+divs0, p2.bn, min(p2.size,divs0)*sizeof(int));
		memcpy(p1.bn+divs0*2, p3.bn, p3.size*sizeof(int));
		return p1.trim();
	}
	bignum& operator *=(bignum& num){
		unref();
		return *this=*this*num;
	}
	bignum operator /(const bignum& num){
		return *this/(bignum&)num;
	}
	bignum operator /(bignum& num){
		bignum ret=*this;
		return ret/=num;
	}
	bignum operator /(int num){
		bignum ret=*this;
		return ret/=num;
	}
	bignum& operator /=(const bignum& num){
		return *this/=(bignum&)num;
	}
	bignum& operator /=(bignum& num){
		bignum th,t,rs,sb;
		bignum& op=t;
		unref();
		sg^=num.sg;
		if (base==num.base)
			op=num;
		else{
			t.init(base,all_size);
			t.convert(num);
		}
		if (op==0)return *this=0;
		th=*this;
		rs.init(base,all_size);
		rs=1;
		sb=op;
		sb.sg=th.sg=0;
		*this=0;
		while (sb<=th){
			rs*=2;
			sb*=2;
		}
		while (rs!=0){
			if (sb<=th){
				th-=sb;
				*this+=rs;
			}
			rs/=2;
			sb/=2;
		}
		return trim();
	}
	bignum& operator /=(int num){
		int i;
		bignum th=*this;
		unref();
		long long t,carry=0;
		*this=0;
		resize(th.size);
		FDOWN(i,size-1,0){
			t=th.bn[i]+carry;
			bn[i]=(int)(t/num);
			carry=t%num;
			carry*=base;
		}
		return trim();
	}
	bignum operator %(bignum& num){
		bignum ret=*this;
		return ret%=num;
	}
	int operator %(int num){
		bignum ret=*this;
		return ret%=num;
	}
	bignum& operator %=(bignum& num){
		int i=1,s;
		bignum t,sb;
		bignum& op=t;
		unref();
		s=sg;
		if (base==num.base)
			op=num;
		else{
			t.init(base,all_size);
			t.convert(num);
		}
		if (op==0)return *this=0;
		sb=op;
		sb.sg=sg=0;
		while (sb<=(*this) && ++i)
			sb*=2;
		while (i--){
			if (sb<=(*this))
				*this-=sb;
			sb/=2;
		}
		sg=s;
		return trim();
	}
	int operator %=(int num){
		long long ret=0;
		int i;
		FDOWN(i,size-1,0)
			ret=(ret*base + bn[i])%num;
		ret=(sg?-ret:ret);
		*this=ret;
		return (int)ret;
	}
	bool operator < (bignum& num){
		int i;
		bignum t;
		bignum& op=t;
		if (sg!=num.sg)return sg==1;
		if (base==num.base)
			op=num;
		else{
			t.init(base,all_size);
			t.convert(num);
		}
		if (size!=op.size)
			return sg?(size>op.size):(size<op.size);
		FDOWN(i,size-1,0)
			if (bn[i]!=op.bn[i])
				return sg?(bn[i]>op.bn[i]):(bn[i]<op.bn[i]);
		return 0;
	}
	bool operator == (bignum& num){
		int i;
		bignum t;
		bignum& op=t;
		if (sg!=num.sg)return 0;
		if (base==num.base)
			op=num;
		else{
			op=t;
			t.init(base,all_size);
			t.convert(num);
		}
		if (size!=op.size)return 0;
		FDOWN(i,size-1,0)
			if (bn[i]!=op.bn[i])
				return 0;
		return 1;
	}
	bool operator > (bignum& num){
		return num<*this;
	}
	bool operator <= (bignum& num){
		return !(num<*this);
	}
	bool operator >= (bignum& num){
		return !(*this<num);
	}
	bool operator != (bignum& num){
		return !(*this==num);
	}
	bignum operator +(int ni){
		bignum num=ni;
		return *this+num;
	}
	bignum& operator +=(int ni){
		unref();
		bignum num=ni;
		return *this+=num;
	}
	bignum operator -(int ni){
		bignum num=ni;
		return *this-num;
	}
	bignum& operator -=(int ni){
		unref();
		bignum num=ni;
		return *this-=num;
	}
	bignum operator *(int ni){
		bignum num=ni;
		return *this*num;
	}
	bignum& operator *=(int ni){
		unref();
		bignum num=ni;
		return *this*=num;
	}
	bool operator < (int ni){
		bignum num=ni;
		return *this<num;
	}
	bool operator == (int ni){
		bignum num=ni;
		return *this==num;
	}
	bool operator > (int ni){
		bignum num=ni;
		return *this>num;
	}
	bool operator <= (int ni){
		bignum num=ni;
		return *this<=num;
	}
	bool operator >= (int ni){
		bignum num=ni;
		return *this>=num;
	}
	bool operator != (int ni){
		bignum num=ni;
		return *this!=num;
	}
	long long to_ll(){
		long long ret=0;
		int i;
		FDOWN(i,size-1,0)
			ret=ret*base+bn[i];
		return sg?-ret:ret;
	}
	bignum& div(bignum& num, bignum& div, bignum& rest){
		bignum t,rs,sb;
		bignum& op=t;
		rest=*this;
		div.init(base,all_size);
		if (base==num.base)
			op=num;
		else{
			t.init(base,all_size);
			t.convert(num);
		}
		if (op==0)
			return div=rest=0;
		rs.init(base,all_size);
		rs=1;
		sb=op;
		sb.sg=rest.sg=0;
		while (sb<=rest){
			rs*=2;
			sb*=2;
		}
		while (rs!=0){
			if (sb<=rest){
				rest-=sb;
				div+=rs;
			}
			rs/=2;
			sb/=2;
		}
		rest.sg=sg;
		div.sg=sg^num.sg;
		rest.trim();
		return div.trim();
	}
	bignum& convert(bignum& src){
		unref();
		resize(digits(src.size, src.base, base));
		memset(bn,0,size*sizeof(int));
		bignum op=src;
		this->sg=op.sg;
		int t=op.base, i, ml=1, j=0, k=0;
		while (t<base){
			t*=op.base;
			ml++;
		}
		if (t==base){ // this we can do O(n), not O(n^2) by not using divisions
			t=1;
			FUP(i,0,op.size-1){
				bn[j]+=t*op.bn[i];
				t*=op.base;
				if (++k == ml){
					j++;
					k=0;
					t=1;
				}
			}
			size=j+1;
			return trim();
		}
		t=base;
		ml=1;
		while (t<op.base){
			t*=base;
			ml++;
		}
		if (t==op.base){ // this we can do O(n), not O(n^2) by not using divisions
			FUP(i,0,op.size-1){
				t=op.bn[i];
				FUP(k,0,ml-1){
					bn[j++]=t%base;
					t/=base;
				}
			}
			size=j;
			return trim();
		}
		i=0;
		op.sg=0;
		while (op!=0){
			bn[i++]=op%base;
			op/=base;
		}
		size=i;
		return trim();
	}
	bignum& scan(string num, int num_base){
		int i,c;
		bignum op;
		op.init(num_base);
		op.resize(num.size());
		memset(op.bn,0,op.size*sizeof(int));

		FALL(i,num){
			c=num[i];
			if (c>='0'&&c<='9')
				c-='0';
			else if (c>='A'&&c<='Z')
				c-='A'-10;
			else if (c>='a'&&c<='z')
				c-='a'-10;
			else
				c=0;
			op.bn[num.size()-1-i]=c;
		}
		if (base!=num_base)
			return convert(op.trim());
		else
			return *this=op.trim();
	}
	char* print(int num_base){
		bignum op;
		char* ret;
		op.base=num_base;
		op.convert(*this);
		int c,i;
		if (op==0){
			ret=new char[2];
			ret[0]='0';
			ret[1]=0;
			return ret;
		}
		ret= new char[op.size+3];
		if (sg==1){
			ret[0]='-';
			ret++;
		}
		FDOWN(i,op.size-1,0){
			c=op.bn[i];
			if (c<10)
				c='0'+c;
			else
				c='A'+c-10;
			ret[op.size-1-i]=(char)c;
		}
		ret[op.size]=0;
		if (sg==1)
			ret--;
		return ret;
	}
	int digits(int words, int base1, int base2){
		return max(1,(int)ceil(words*(log(1.0*base1)/log(1.0*base2))));
	}
	bignum& trim(){
		while (size && bn[size-1]==0)
			size--;
		if (size==0)
			sg=0;
		return *this;
	}
	void resize(int words){
		unref();

		if (allocated >= words){
			size=words;
			return;
		}
		allocated=words+all_size-(words%all_size);
		bn=(int*)realloc(&bn[-1],(allocated+1)*sizeof(int));
		bn++;
		memset(bn+size, 0, (allocated-size)*sizeof(int));
		size=words;
	}
	void clear(){
		if (!--bn[-1])
			delete [] &bn[-1];
		bn=new int[1];
		bn[0]=1;
		bn++;
		size=0;
		sg=0;
		allocated=0;
	}
	int* bn;
	int size;
	int all_size;
	int base;
	int allocated;
	int sg;
};

bignum num[1000];
char s[100];

bignum gcd(bignum a, bignum b) {
	if (b == 0) {
		return a;
	} else if (a < b) {
		return gcd(b, a);
	} else {
		return gcd(b, a%b);
	}
}

int main() {
	int t, T, i, j, n;
	scanf("%d", &t);
	FUP(T,1,t) {
		scanf("%d", &n);
		FUP(i, 0, n-1) {
			scanf("%s", s);
			num[i].scan(s, 10);
		}
		bignum g = 0;
		int was = 0;
		FUP(i, 0, n-1) {
			FUP(j, i+1, n-1) {
				if (num[i] < num[j]) {
					g = gcd(g, num[j] - num[i]);
					was++;
				} else if (num[i] > num[j]) {
					g = gcd(g, num[i] - num[j]);
					was++;
				}
			}
		}
		bignum t;
		if (was) {
			t = num[0]%g;
			if (t == 0) {
				t = g;
			}
		} else {
			g = t = 0;
		}
		printf("Case #%d: %s\n", T, (g - t).print(10));
	}
	return 0;
}