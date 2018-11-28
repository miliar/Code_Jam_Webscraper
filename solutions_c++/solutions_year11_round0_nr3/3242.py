// Author : Muhammad Rifayat Samee
// Problem : 
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
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b
#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif




using namespace std;

int number[1005];
int n;
int main()
{
	//freopen("c_large.in","r",stdin);
	//freopen("c_large.txt","w",stdout);
	int cases,i,j,k,res,tot,ct=1;

	scanf("%d",&cases);

	while(cases--)
	{
		scanf("%d",&n);
		tot = 0;

		for(i=0;i<n;i++)
		{
			scanf("%d",&number[i]);
			tot = tot + number[i];

		}
		
		sort(number,number+n);
		tot = tot - number[0];
		res = number[1];
		for(i=2;i<n;i++)
			res = res^number[i];

		if(res == number[0])
			printf("Case #%d: %d\n",ct++,tot);
		else
			printf("Case #%d: NO\n",ct++);




	}
	return 0;


}