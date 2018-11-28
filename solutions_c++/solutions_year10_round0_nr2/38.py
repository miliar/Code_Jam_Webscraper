#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
class bignum {
public:
	bignum();
	bignum(const string&);
	bignum(int a);
	void print();
	friend bignum operator+(const bignum&,const bignum&);
	friend bignum operator-(const bignum&,const bignum&);
	friend bignum operator*(const bignum&,const bignum&);
	friend bool operator<(const bignum&,const bignum&);
	friend bool operator<=(const bignum&,const bignum&);
	friend bignum operator/(const bignum&,const bignum&);
	friend bignum mod(const bignum&,const bignum&);
	bignum operator*(int);
	int sumOfDigits();
	int size();
	void reverse();
	bignum div2();
	bool palindrome();
	bool firstnine();
	bool lastnine();
	int digit(int);
private:
	vector<int> s;
};
bool bignum::firstnine()
{
	if (s.size()<9) return false;
	bool p[10]={0};
	int i;
	for (i=s.size()-1;i>=s.size()-9;--i) {
		if (s[i]==0 || p[s[i]]) return false;
		p[s[i]]=true;
	}
	return true;
}
bool bignum::lastnine()
{
	if (s.size()<9) return false;
	bool p[10]={0};
	int i;
	for (i=0;i<9;++i) {
		if (s[i]==0 || p[s[i]]) return false;
		p[s[i]]=true;
	}
	return true;
}
bignum bignum::div2()
{
	int i;
	bignum ret=*this;
	for (i=ret.s.size()-1;i>=0;--i) {
		if (i>0) if (ret.s[i]&1) ret.s[i]--,ret.s[i-1]+=10;
		ret.s[i]/=2;
	}
	while (ret.s.size()>1 && ret.s[ret.s.size()-1]==0) ret.s.pop_back();
	return ret;
}
void bignum::print()
{
	int i;
	for (i=s.size()-1;i>=0;--i) printf("%d",s[i]);
	printf("\n");
	//cout<<endl;
	//cout<<s.size()<<endl;
}
bignum::bignum()
{
	s.clear();
	s.push_back(0);
}
bignum::bignum(int a)
{
	if (a==0) {
		s.clear();
		s.push_back(0);
	} else {
		s.clear();
		while (a>0) {
			s.push_back(a%10);
			a/=10;
		}
	}
}
bignum::bignum(const string& t)
{
	s.clear();
	int i;
	for (i=t.size()-1;i>=0;--i) s.push_back(t[i]-'0');
	while (s.size()>1 && s[s.size()-1]==0) s.pop_back();
}
bool operator<(const bignum& a,const bignum& b)
{
	if (a.s.size()!=b.s.size()) {
		return (a.s.size()<b.s.size());
	}
	int i;
	for (i=a.s.size()-1;i>=0;--i)
		if (a.s[i]!=b.s[i]) return a.s[i]<b.s[i];
	return false;
}
bool operator<=(const bignum& a,const bignum& b)
{
	if (a.s.size()!=b.s.size()) {
		return (a.s.size()<b.s.size());
	}
	int i;
	for (i=a.s.size()-1;i>=0;--i)
		if (a.s[i]!=b.s[i]) return a.s[i]<b.s[i];
	return true;
}
bignum operator+(const bignum& a,const bignum& b)
{
	int i,x=0;
	bignum c;
	c.s.clear();
	for (i=0;i<max(a.s.size(),b.s.size());++i) {
		x=x/10;
		if (i<a.s.size()) x+=a.s[i];
		if (i<b.s.size()) x+=b.s[i];
		c.s.push_back(x%10);
	}
	while (x>9) {
		x/=10;
		c.s.push_back(x%10);
	}
	return c;
}
bignum operator-(const bignum& a,const bignum& b)
{
	int i;
	bignum c=a;
	for (i=0;i<b.s.size();++i) {
		c.s[i]-=b.s[i];
		if (c.s[i]<0) c.s[i]+=10,c.s[i+1]--;
	}
	while (c.s.size()>1 && c.s[c.s.size()-1]==0) c.s.pop_back();
	return c;
}
bignum operator*(const bignum& a,const bignum& b)
{
	int i,j;
	bignum c;
	for (i=0;i<(a.s.size()+b.s.size()-1);++i) c.s.push_back(0);
	for (i=0;i<a.s.size();++i)
		for (j=0;j<b.s.size();++j)
			c.s[i+j]+=a.s[i]*b.s[j];
	for (i=0;i<c.s.size()-1;++i)
		if (c.s[i]>=10) {
			c.s[i+1]+=c.s[i]/10;
			c.s[i]%=10;
		}
	while (c.s[c.s.size()-1]>=10) {
		c.s.push_back(c.s[c.s.size()-1]/10);
		c.s[c.s.size()-2]%=10;
	}
	while (c.s.size()>1 && c.s[c.s.size()-1]==0) c.s.pop_back();
	return c;
}
bignum bignum::operator*(int a)
{
	if (a==0) return bignum("0");
	bignum c;
	c.s.clear();
	int i,x=0;
	for (i=0;i<s.size();++i) {
		x=x/10+s[i]*a;
		c.s.push_back(x%10);
	}
	while (x>=10) {
		x/=10;
		c.s.push_back(x%10);
	}
	return c;
}
int bignum::sumOfDigits()
{
	int i,ans=0;
	for (i=0;i<s.size();++i) ans+=s[i];
	return ans;
}
int bignum::size()
{
	return s.size();
}
void bignum::reverse()
{
	std::reverse(s.begin(),s.end());
	int t=0;
	while (s.size()>1 && s[s.size()-1]==0) {
		s.pop_back();
		++t;
	}
}
bool bignum::palindrome()
{
	int i;
	for (i=0;i<s.size();++i) if (s[i]!=s[s.size()-i-1]) return false;
	return true;
}
int bignum::digit(int i)
{
	if (i>=s.size()) return 0;
	return s[i];
}
bignum operator/(const bignum& a,const bignum& b)
{
	bignum l(1),r(a);
	if (a<b) return 0;
	if (b<=bignum(1) && bignum(1)<=b) return a;
	while (l+1<r) {
		bignum m((l+r).div2());
		if (m*b<=a) l=m;else r=m;
	}
	return l;
}
bignum mod(const bignum& a,const bignum& b)
{
	return a-(a/b)*b;
}
