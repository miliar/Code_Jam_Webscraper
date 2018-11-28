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
#define lim 100000000
char vis[11][lim];
int tobase(int b,int x)
{
	int sum=0,k;
	while(x>0)
	{
		k=x%b;
		sum+=k*k;
		x/=b;
	}
	return sum;
}
int base[11];
int basec;
bool go(int b,int x)
{
	char & ret=vis[b][x];
	if(ret==1)return 1;
	if(ret==0)return 0;
	if(ret==-2)
	{
		ret=0;
		return 0;
	}
	ret=-2;
	return ret=go(b,tobase(b,x));
}
int main()
{
	#ifdef WIN32
		freopen("all.in","r",stdin);
		//freopen("A-large.out","w",stdout);
	#endif
////////////////////////////////////////////
	int i,j,k;
	string str;
	scanf("%d\n",&cases);
	stringstream ss;
	CLS(vis,-1);
	for(i=2;i<=10;i++)
	{
		vis[i][1]=1;
	}
	for(z=1;z<=cases;z++)
	{
		str=getline();
		ss.clear();
		ss.str(str);
		basec=0;
		while(ss >> k)
		{
			base[basec++]=k;
		}
		if(basec==9)
			printf("Case #%d: %d\n",z,11814485);
		else
		for(j=2;j<lim;j++)
		{
			k=1;
			for(i=0;i<basec;i++)
			{
				k=k && go(base[i],j);
			}
			if(k==1)
			{
				printf("Case #%d: %d\n",z,j);
				break;
			}
		}
		//printf("Case #%d: %d\n",z,ans);
	}
	return 0;
}