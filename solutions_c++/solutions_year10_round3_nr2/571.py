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
#define torad(a) ((a)*pi/180.0)
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
int cases,g;
int l,p,c;
int best[1001][1001];
int solve(int a,int b)
{
	if(a>b)return 0;
	int &ret=best[a][b];
	if(ret!=-1)return ret;

	if(a*c>b)
		return 0;
	ret=b-a+1;
	int s=a,e=b,m,k;
	
/*	for(int i=a;i<=b;i++)
	{
		ret=min(ret,1+max(solve(i,b),solve(a,i-1)));
	}*/
	while(e>s)
	{
		m=(s+e)/2;
	//	ret=min(ret,1+max(solve(m,b),solve(a,m-1)));
		if( solve(a,m-1) < solve(m,b))
		{
			s=m+1;
		}
		else
		{
			e=m;
		}
	}
	
	
		ret=min(ret,1+max(solve(s,b),solve(a,s-1)));
		if(s>a)
			ret=min(ret,1+max(solve(s-1,b),solve(a,s-2)));

	return ret;
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
////////////////////////////////////////////
	int i,j,k;
	scanf("%d",&cases);
	for(g=0;g<cases;g++)
	{
		printf("Case #%d: ",g+1);
		scanf("%d%d%d",&l,&p,&c);
		CLS(best,-1);
		k=solve(l,p-1);
		printf("%d\n",k);
	}

	return 0;
}