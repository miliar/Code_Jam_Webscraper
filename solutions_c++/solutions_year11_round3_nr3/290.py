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
int n,l,h;
int freq[10001];
int GCD(int a, int b)
{
   if (b==0) return a;
   return GCD(b,a%b);
}

int LCM(int a,int b)
{
	return (a*b)/GCD(a,b);
}
bool check(int x,int cur)
{
	for(int i=x;i<n;i++)
		if(freq[i]%cur)
			return false;
	return true;
}
int main()
{
	freopen("C-small-attempt2.in","r",stdin);
	//freopen("c.in","r",stdin);
	freopen("C-small-attempt2.out","w",stdout);
////////////////////////////////////////////
	int i,j,k;
	scanf("%d",&cases);
	for(g=0;g<cases;g++)
	{
		printf("Case #%d: ",g+1);
		scanf("%d%d%d",&n,&l,&h);
		for(i=0;i<n;i++)
		{
			scanf("%d",&freq[i]);
		}
		sort(freq,freq+n);
		
		
		for(i=l;i<=h;i++)
		{
			for(j=0;j<n;j++)
			{
				if(i%freq[j] && freq[j]%i)
					break;
			}
			if(j==n)
			{
				printf("%d\n",i);
				goto bara;
			}
		}
		printf("NO\n");
bara:
		k=1;
	}


	return 0;
}