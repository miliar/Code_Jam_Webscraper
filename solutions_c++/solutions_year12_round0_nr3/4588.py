#include<iostream>
#include<stdio.h>
#include<vector>
#include<string.h>
#include<string>
#include<set>
#include<map>
#include<algorithm>
#include<math.h>
#include<memory.h>
#include<queue>
//#include<unordered_map>
//#include<unordered_set>
using namespace std;

#define all(a) a.begin(),a.end()
#define mp make_pair
#define li long long
#define db long double
#define pi pair<int,int>
#define vi vector<int>
#define INF (li)1000000007
#define mod (li)2011

void solve();

int main ()
{
#ifdef _DEBUG
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#else
	//freopen("input.txt","r",stdin);
	//freopen("input.txt","r",stdin);
#endif
	int t;
	cin>>t;
	int ab=t;
	while(t--)
	{
		printf("Case #%d: ",ab-t);
		solve();
		printf("\n");
	}
	return 0;
}
bool prov(int a,int b)
{
	int aa[11],bb[11];
	int t=0,r=0;
	while(a)
	{
		aa[t++]=a%10;
		a/=10;
	}
	while(b)
	{
		bb[r++]=b%10;
		b/=10;
	}
	for(int i=1;i<t;i++)
	{
		int q;
		for(q=0;q<t;q++)
		{
			if(aa[q]!=bb[(i+q)%t])
				break;
		}
		if(q==t)
			return true;
	}
	return false;
}
void solve()
{
	int a,b;
	cin>>a>>b;
	int res=0;
	for(int i=a;i<=b;i++)
	{
		for(int q=i+1;q<=b;q++)
		{
			if(prov(i,q))
				res++;
		}
	}
	printf("%d",res);
}