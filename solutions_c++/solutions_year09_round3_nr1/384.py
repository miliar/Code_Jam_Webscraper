#include<iostream>
#include<string>
#include<sstream>
#include<map>
using namespace std;
#define MAXN 70
__int64 toDec ( int *a , int n , int base )
{
	__int64 res=0;
	for ( int i=0 ; i<n ; i++ )
	{
		res=res*base+a[i];
	}
	return res;
}

__int64 solve ( string s )
{
	int tot=1;
	int num[MAXN];
	map<char,int> look;
	look[s[0]]=1;
	num[0]=1;
	int i;
	for ( i=1 ; i<s.size()  ; i++ )
	{
		if ( s[i]==s[i-1] )
		{
			num[i]=1;
		}
		else
			break;
	}
	if ( i==s.size() ) 
	{
		return toDec(num,s.size(),2);
	}
	look[s[i]]=0;
	num[i]=0;
	for ( ; i<s.size() ; i++ )
	{
		if ( look.find(s[i])==look.end() )
		{
			look[s[i]]=++tot;
		}
		num[i]=look[s[i]];
	}
	__int64 res=toDec(num,s.size(),tot+1);
	return res;
}

int main ( )
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas,n,i,k;
	scanf("%d",&cas);
	string s;
	for ( k=1 ; k<=cas; k++ )
	{
		cin>>s;
		__int64 res=solve(s);
		printf("Case #%d: %I64d\n",k,res);
	}
}