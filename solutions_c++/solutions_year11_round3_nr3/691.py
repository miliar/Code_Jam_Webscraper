// Author : Muhammad Rifayat Samee
// Problem : C
// Algorithm:
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<stack>

#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif

using namespace std;

int N[105];


int gcd(int a,int b)
{
	while(b>0)
	{
		a = a%b;
		a^=b;b^=a;a^=b;

	}

	return a;

}

int lcm(int a,int b)
{
	int g;
	g = gcd(a,b);

	return a/g*b;
}


int main()
{
	//freopen("c_s.in","r",stdin);
	//freopen("out.txt","w",stdout);
	
	int cases,i,j,k,l,h,num,r,ct=1,n,a,b,res,f;

	scanf("%d",&cases);

	while(cases--)
	{
		scanf("%d %d %d",&n,&l,&h);
		
		for(i=0;i<n;i++)
		{
			scanf("%d",&N[i]);
					
		}
		f = 0;
		for(i=l;i<=h;i++)
		{
			for(j=0;j<n;j++)
			{
				r = lcm(N[j],i);
				if(r != i && r!=N[j])
				{
					break;
				}
			}
			if(j==n)
			{
				f = 1;
				break;
			}
		}
		
		if(f == 0)
		printf("Case #%d: NO\n",ct++);
		else
			printf("Case #%d: %d\n",ct++,i);
	}
	return 0;


}
