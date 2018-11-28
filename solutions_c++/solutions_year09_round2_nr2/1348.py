
/* Macros and Headers and Functions {{{ */
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<set>
#include<stack>
#include<queue>
#include<cstdarg>
#include<map>
#include<list>
#include<deque>
#include<cctype>
#include<iterator>
#include<numeric>
#include<complex>
#include<climits>
#include<cstdlib>
#include<cstring>


using namespace std;

#define REP(i,n) for(int i=0; i<n; ++i)
#define REPS(p,s) for(char *p=s;*p;p++)
#define FOR(i,a,b) for(int i=a;i<b;++i)
#define RFOR(i,a,b) for(int i=a;i>=b;--i)

#define EL() cout<<endl;

#define BN begin()
#define ED end()
#define RN rbegin()
#define RD rend()
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second

#define PB push_back
#define PF push_front
#define BP pop_back
#define FP pop_front

#define IT(X) __typeof((X).BN)
#define RIT(X) __typeof((X).RN)
#define REF(X) __typeof(__typeof(X)::reference)

#define FORIT(it,X) for(IT(X) it= (X).BN; it!=(X).ED; ++it)
#define FORITR(it,X) for(RIT(X) it=(X).RN; it!=(X).RD; ++it)

#define VV(X) vector< vector< X > >
#define PIB(X) pair< IT(X), bool >

typedef long long LL;
typedef unsigned long long ULL;
//typedef stringstream ss;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector< PII > VPII;

//debugging IO functions start

void IO(int l, ...)
{
	va_list val;
	va_start(val,l);
	int i;
	FOR(i,0,l)
	{
		cout<<va_arg(val,int)<<"  ";
	}
}

void SO(int l, ...)
{
	va_list val;
	va_start(val,l);
	int i;
	FOR(i,0,l)
	{
		cout<<va_arg(val,char*)<<"  ";
	}
}

void AIO(int n,int a[])
{
	REP(i,n)
		cout<<a[i]<<"  ";
	EL();
}

void ASO(int n,string a[])
{
	REP(i,n)
		cout<<a[i]<<"  ";
	EL();
}

void GIO(char *f, ...)
{
	va_list val;
	va_start(val,f);
	while(*f!='\0')
	{
		if(*f=='d')    //here we can add more options as we need like for double, or user defined structs
			cout<<va_arg(val,int)<<"  ";
		else if(*f=='s')
			cout<<va_arg(val,char*)<<"  ";
		f++;
	}
}

//debugging IO functions end
/* }}} */

int main()
{
	int cas;
	string s,s2,s3;
	cin>>cas;

	REP(x,cas)
	{
		cin>>s;
		s2=s;
		sort(s2.BN,s2.ED);
		cout<<"Case #"<<x+1<<": ";
		next_permutation(s.BN,s.ED);
		if(s!=s2)
			cout<<s<<endl;
		else
		{
			while(s[0]=='0')
				next_permutation(s.BN,s.ED);
				
//			s+='0';
			cout<<s[0]<<"0";
			FOR(i,1,s.length())
				cout<<s[i];
			cout<<endl;
			
		}
	}
	return 0;
}
