#include <algorithm>
#include <stack>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>
using namespace std;

#define pb push_back
#define lng long long
#define inf 1000000000
#define pii pair<int,int>
#define mp make_pair
#define mpii make_pair<int,int>
#define forv(i,v) for(int i = 0; i<v.size(); ++i)
#define forvr(i,v) for(int i = v.size()-1;i>=0; --i)
#define forn(i,n) for(int i = 0;i<n;++i)
#define fornr(i,n) for(int i = n-1;i>=0;--i)
#define pi 3.1415926535897932384626433832795

inline lng gcd(lng a,lng b){
	if(!a)return b;
	if(!b)return a;
	while(true){
		a%=b;
		if(!a)return b;
		b%=a;
		if(!b)return a;
	}
}
inline int gcd(int a,int b){
	if(!a)return b;
	if(!b)return a;
	while(true){
		a%=b;
		if(!a)return b;
		b%=a;
		if(!b)return a;
	}
}

inline int min(int a,int b){
	return a<b?a:b;
}

inline bool isprime(lng a){
	if(a<=1)return false;
	int s=sqrt((double)a)+1;
	for(int i=2;i<=s;++i){
		if(!(a%i)&&i<a)return false;
	}
	return true;
}

inline int prime_divisors(int a){
	int s=sqrt((double)a)+1;
	int r=0;
	for(int i=2;i<=s;++i){
		if(!(a%i)){
			while(!(a%i))
				a/=i;
			++r;
		}
	}
	if(a>1)++r;
	return r;
}
inline int sumdigits(int a){
	int r=0;
	while(a){
		r+=a%10;
		a/=10;
	}
	return r;
}
inline int cntdigits(int a){
	int r=0;
	while(a){
		++r;
		a/=10;
	}
	return r;
}
	
string i2s(lng a,lng base=10){
	string r;
	while(a){
		lng d=(a%base);
		if(d>9)
			r+='a'+d-10;
		else
			r+='0'+d;
		a/=base;
	}
	reverse(r.begin(),r.end());
	return r;
}

lng s2i(string &s){
	lng r=0;
	for(int i=0;i<s.length();++i)
		r=r*10+(s[i]-'0');
	return r;
}

struct vlng{
	//static const int base = 1000*1000*1000;
	static const int base = 10;
	vector<int> a;

	vlng():a(){}

	vlng(int v){
		while(v){
			a.push_back(v%base);
			v/=base;
		}
	}

	vlng(vlng &q):a(q.a){}

	vlng& operator=(vlng &q){
		a=q.a;
		return *this;
	}

	vlng& operator=(int v){
		a.clear();
		while(v){
			a.push_back(v%base);
			v/=base;
		}
		return *this;
	}

	void write(){
		printf ("%d", a.empty() ? 0 : a.back());
		for (int i=(int)a.size()-2; i>=0; --i)
			if(base==1000000000)
				printf ("%09d", a[i]);
			else if(base==10)
				printf ("%d", a[i]);
	}

	void read(){
		char s[1000];
		scanf("%s",s);
		for (int i=(int)strlen(s); i>0; i-=9) {
			s[i] = 0;
			a.push_back (atoi (i>=9 ? s+i-9 : s));
		}
		while (a.size() > 1 && a.back() == 0)
			a.pop_back();
	}

	vlng& operator+=(vlng &q){
		vector<int> &b=q.a;
		int carry = 0;
		for (size_t i=0; i<max(a.size(),b.size()) || carry; ++i) {
			if (i == a.size())
				a.push_back (0);
			a[i] += carry + (i < b.size() ? b[i] : 0);
			carry = a[i] >= base;
			if (carry)  a[i] -= base;
		}
		return *this;
	}

	vlng& operator*=(int b){
		int carry = 0;
		for (int i=0; i<a.size()||carry; ++i) {
			if(i>=a.size())
				a.push_back(0);
			long long cur = (long long)a[i] * b + carry;
			a[i] = int (cur % base);
			carry = int (cur / base);
		}
		return *this;
	}

	vlng& operator/=(int b){
		int carry = 0;
		for (int i=(int)a.size()-1; i>=0; --i) {
			long long cur = a[i] + carry * 1ll * base;
			a[i] = int (cur / b);
			carry = int (cur % b);
		}
		while (a.size() > 1 && a.back() == 0)
			a.pop_back();
		return *this;
	}

	bool operator<(const vlng &b)const{
		if(a.size()!=b.a.size())
			return a.size()<b.a.size();
		for(int i=0;i<a.size();++i){
			if(a[i]!=b.a[i])
				return a[i]<b.a[i];
		}
		return false;
	}

	int sumdigits(){
		int r=0;
		for(int i=0;i<a.size();++i)
			r+=::sumdigits(a[i]);
		return r;
	}

	void reverse(){
		std::reverse(a.begin(),a.end());
	}

	bool palindromic(){
		for(int i=0;i<a.size()/2;++i)
			if(a[i]!=a[a.size()-i-1])return false;
		return true;
	}
};
//------------------------------------

char line[1000];
int minpos[1000];
int per[1000];

//#define __TIMUS__
#define filename "points"
int main()
{
#ifdef __TRATATA__
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#else
#ifndef __TIMUS__
	freopen(filename".in","r",stdin);
	freopen(filename".out","w",stdout);
#endif
#endif
	
	int tc;
	cin>>tc;
	forn(q,tc){
		int n;
		cin>>n;
		forn(i,n){
			per[i]=i;
			scanf("%s",line);
			minpos[i]=0;
			forn(j,n)
				if(line[j]=='1')
					minpos[i]=max(minpos[i],j);
		}
		int res=1000000000;
		do{
			bool good=true;
			forn(i,n)
				if(minpos[per[i]]>i){
					good=false;
					break;
				}
			if(!good)
				continue;
			int r=0;
			forn(i,n)
				forn(j,i)
					if(per[j]>per[i])
						++r;
			res=min(res,r);
		}while(next_permutation(per,per+n));
		printf("Case #%d: %d\n",q+1,res);
	}

	return 0;
}
