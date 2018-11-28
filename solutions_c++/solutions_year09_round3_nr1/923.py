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

ULL ans;
void convert(int n,int base)
{
	ULL ans=0;
	int i=0,rem;
	while(n!=0)
	{
		rem=n%10;
		n=n/10;
		ans+=(ULL)pow(rem,i);
		i++;
	}
}

int main()
{
	string str;
	ULL no;
	int cases,arr[40],val,cnt,temp=1,len,flag;
	cin>>cases;
	while(cases--)
	{
		cin>>str;
		len=str.length();
		REP(i,40)
			arr[i]=-1;
//		arr[str[1]-'0']=0;
		cnt=1,no=0,flag=1;
		REP(i,len)
		{
			if(str[i]>='a')
				val=str[i]-'a'+10;
			else
				val=str[i]-'0';
			if(arr[val]==-1)
			{
				arr[val]=cnt;
				if(cnt==2 && flag==1)
				{
					arr[val]=0;
					flag=0;
				}
				else
					cnt++;
			}
//			no=no*10+arr[val];
		}
//		cout<<no<<" "<<cnt<<endl;
		no=0;
		REP(i,len)
		{
			if(str[i]>='a')
				val=str[i]-'a'+10;
			else
				val=str[i]-'0';
			no=no*cnt+arr[val];
		}
//		convert(no,cnt);
		cout<<"Case #"<<temp<<": "<<no<<endl;
		temp++;
	}
	return 0;
}
