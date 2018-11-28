#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <cctype>
#include <algorithm>
#include <vector>
#include <numeric>
#include <set>
#include <queue>
#include <map>
#include <list>
#include <string>
#include <iostream>
#include <stack>
#include <sstream>
using namespace std; 
#define PB push_back
#define MP make_pair
#define F first
#define S second 
#define BE(a) a.begin(),a.end() 
#define CLS(a,b) memset(a,b,sizeof(a))
#define SZ(a) ((int)a.size())
const long double pi=acos(-1.0);
#define torad(a) (a*pi/180.0)
typedef vector<int> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ; 
typedef pair<int,int> pii ; 
typedef long long ll ; 
typedef long double ld ; 
typedef double dl ; 
class node {public:
};
typedef vector<node> vn ; 
int cases,z;
string pat="welcome to code jam";
int cnt;
int best[22][509];
int MOD=10000;
string str;
int go(int k,int p)
{
	if(k==pat.size())return 1;
	if(p==str.size())return 0;
	int & ret=best[k][p];
	if(ret!=-1)return ret;
	ret=0;
	int i;
	for(i=p+1;i<str.size();i++)
	{
		if(pat[k]==str[i])
			ret=(ret+go(k+1,i))%MOD;
	}
	return ret;
}
string getline()
{
	char c;
	string ret="";
	while(scanf("%c",&c))
	{
		if(c==10)return ret;
		ret+=c;
	}
	return ret;
}
int main()
{
	#ifdef WIN32
		freopen("C-large.in","r",stdin);
		freopen("C-large.out","w",stdout);
	#endif
////////////////////////////////////////////
	int i,j,k,ans=0;
	scanf("%d\n",&cases);
	for(z=1;z<=cases;z++)
	{
		ans=0;
		CLS(best,-1);
		str=getline();
		
		for(i=0;i<str.size();i++)
			if(str[i]=='w')
			ans= (ans + go(1,i))%MOD;
		printf("Case #%d: %04d\n",z,ans);
	}
	return 0;
}