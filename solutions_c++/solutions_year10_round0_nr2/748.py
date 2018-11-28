// google codejam.cpp : Defines the entry point for the console application.
//

// BEGIN CUT HERE
#include <stdafx.h>
// END CUT HERE
#include <algorithm>
#include <iostream>
#include <fstream>
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
using namespace std;

#define REP(i,n) for(int i=0;i<n;++i)
#define VI vector<int>
#define VII vector<VI>
#define ALL(n) n.begin(),n.end()
#define LL long long
#define SIZE(o) o.size()

int dx4[]={0,0,-1,1};
int dy4[]={-1,1,0,0};
struct bigint
{
	static const int maxlen=60;
	char num[maxlen];
	int len;
	char* tostring()
	{
		int i=0;
		for(;i<maxlen;++i)
			if(num[i]!=0)
				break;
		if(i==maxlen)
			i--;
		char* res=new char[maxlen-i+1];
		int n=0;
		for(;i<maxlen;++i)
			res[n++]=(char)(num[i]+'0');
		res[n]='\0';
		return res;
	}
	bigint(char* s)
	{
		memset(num,0,maxlen);
		int i=0;
		for(i=0;i<=50;++i)
			if(s[i]==0)
				break;
		len=i;
		REP(i,len)
			num[i+maxlen-len]=s[i]-'0';
	}
	int operator < (bigint other)
	{
		int i;
		REP(i,maxlen)
			if(num[i]!=other.num[i])
				return num[i]<other.num[i];
		return 1;
	}
	bigint minus(bigint other)
	{
		bigint res(" ");
		int d=0;
		for(int i=maxlen-1;i>=0;--i)
		{
			res.num[i]=num[i]-other.num[i]-d;
			d=0;
			if(res.num[i]<0)
			{
				res.num[i]+=10;
				d=1;
			}
		}
		return res;
	}
	bigint multi2()
	{
		bigint res(" ");
		int d=0;
		for(int i=maxlen-1;i>=0;--i)
		{
			res.num[i]=(num[i])*2+d;
			d=0;
			if(res.num[i]>9)
			{
				res.num[i]-=10;
				d=1;
			}
		}
		return res;
	}
	bigint mod(bigint other)
	{
		vector<bigint> v;
		bigint res(" ");
		int i;
		REP(i,maxlen)
			res.num[i]=num[i];
		bigint now=other;

		while(now< res)
		{
			v.push_back(now);
			now=now.multi2();
		}
		for(int i=SIZE(v)-1;i>=0;--i)
			if(v[i]<res)
				res=res.minus(v[i]);
		return res;
	}
	bool iszero()
	{
		int i;
		REP(i,maxlen)
			if(num[i]!=0)
				return false;
		return true;
	}
};
bigint gcd(bigint a,bigint b){return b.iszero()?a:gcd(b,a.mod(b));}
LL gcd(LL a,LL b){return b==0?a:gcd(b,a%b);}
int main(int argc, _TCHAR* argv[])
{
	freopen("in","r",stdin);freopen("out","w",stdout);
	
	
	int testcase;
	scanf("%d",&testcase);
	
	int i,j,k;
	int caseID;
	

	REP(caseID,testcase)
	{
		int N;
		scanf("%d",&N);
		vector<bigint> num;
		char s[60];
		REP(i,N)
		{
			memset(s,0,60);
			scanf("%s",s);
			num.push_back(*new bigint(s));			
		}
		vector<bigint> v;
		REP(i,N)
			for(j=i+1;j<N;++j)
			{
				if(num[i]<num[j])
					v.push_back(num[j].minus(num[i]));
				else 
					v.push_back(num[i].minus(num[j]));
			}
		bigint T=v[0];
		for(i=1;i<SIZE(v);++i)
			T=gcd(T,v[i]);
		bigint m=num[0].mod(T);
		bigint res=T.minus(m);
		if(T<res)
			res=res.minus(T);
		printf("Case #%d: %s\n",caseID+1,res.tostring());

		/*vector<LL> num;
		REP(i,N)
		{
			LL n=0;
			scanf("%ld",&n);
			num.push_back(n);			
		}
		vector<LL> v;
		REP(i,N)
			for(j=i+1;j<N;++j)
			{
				if(num[i]<num[j])
					v.push_back(num[j]-num[i]);
				else 
					v.push_back(num[i]-num[j]);
			}
		LL T=v[0];
		for(i=1;i<SIZE(v);++i)
			T=gcd(T,v[i]);
		int need
		LL res=T-((num[0]%T)==0?0;
		printf("Case #%d: %d\n",caseID+1,res);*/
	}
	
	
	return 0;
}

