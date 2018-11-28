
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
//#include<sstream>


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

int gcd(int a,int b)
{
	int t;
	while(b!=0)
	{
		t=b;
		b=a%b;
		a=t;
	}
	return a;
}
int ans,b,c;
int p[255];
string s;
int main()
{
	
	int cases;
	//int den[50],mul[50],num[50];
//	cout<<gcd(5,3);
	cin>>cases;
	FOR(tt,0,cases)
	{
		cin>>s;
		string a="";
		a+=s;
		sort(a.begin(), a.end());
		int l= a.length();
		int cnt=1;
		p[a[0]]=-1;
//		b=count(s.begin(),s.end())
		FOR(i,1,l)
		{
			p[a[i]]=-1;
			if(a[i]!=a[i-1])
				cnt++;
		}
		b=cnt;
		if(b==1)
			b++;
//		cout<<b<<endl;
/*		char x=a[l-1];
		cout<<x<<endl;	
		if(x>='0' && x<='9')
		{
			b=x-'0';
		//	c='0';
		}
		else
		{
			b=x-'a'+10;
		//	c='a'-10;
		}*/
		ans=0;
		p[s[0]]=1;
		int prev=2;
		int flag=0;
		FOR(i,1,l)
		{
			if(p[s[i]]==-1)
			{
			       if(flag==0)
				{
				flag=1;
				p[s[i]]=0;
				}
			       else
			       {
				       p[s[i]]=prev;
				       prev++;
			       }
			}
		}
//		b++;	
		ans=0;		
		FOR(i,0,l)
		{
//			cout<<p[s[i]]<<"- ";
		/*	if(s[i]>='0' && s[i]<='9')
		{	
			c=s[i]-'0';
		}
		else
		{
			c=s[i]-'a'+10;
		//	c='a'-10;
		}*/
			ans=ans*b+p[s[i]];
//			cout<<ans<<" ";
		}
		cout<<"Case #"<<tt+1<<": "<<ans<<endl;
	}
	return 0;
}
