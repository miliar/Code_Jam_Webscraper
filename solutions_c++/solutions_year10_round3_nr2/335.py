#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <set>
#include <map>

using namespace std;

#define pb push_back
#define sz size
#define all(a)  a.begin(),a.end()
#define SZ(v) ((int)(v).size())

typedef long long  LL;
typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef vector<string> VS;
typedef pair< int, int > PII;
set<LL> s;
LL r,dp[100][100];
vector< LL > array;
LL Min(LL a, LL b){
	if(a<=b)	return a;
	return b;
}
LL Max(LL a, LL b)
{
	if(a>=b)	return a;
	return b;
}		
LL f(int i, int j)
{
	LL a=array[i],b=array[j];
	if(b<=a*r)	return 0;
	if(a*r>=(b+r-1)/r)	return 1;
	if(dp[i][j]>=0)	return dp[i][j];
	LL &ret=dp[i][j];
	ret=100000000;
	for(int k=i+1;k<j;k++)	ret=Min(ret,1+Max(f(i,k),f(k,j)));
	return ret;	
}	 
int main()
{
	int t;
	cin>>t;
	for(int test=1;test<=t;test++){
		memset(dp,-1,sizeof(dp));array.clear();s.clear();
		cout << "Case #" << (test) << ": ";							
		LL a,b;
		scanf("%Ld %Ld %Ld",&a,&b,&r);
		if(b<=a*r)	{cout<<"0"<<endl;continue;}
		else	if(a*r>=(b+r-1)/r)	{cout<<"1"<<endl;continue;}
		LL temp=a;
		while(temp<b){
			s.insert(temp);
			temp*=r;
		}
		 temp=b;
		 while(temp>a){
		 	s.insert(temp);
		 	temp=(temp+r-1)/r;
		 }
		 for(set<LL>::iterator it=s.begin();it!=s.end();it++)
		 		array.pb(*it);	
		int len=SZ(array); sort( all(array) );
	//	for(int i=0;i<len;i++)	cerr<<array[i]<<' ';cerr<<endl;
		cout<<f(0,len-1)<<endl;	
				 				
	}		
	return 0;
}	
