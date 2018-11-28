#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <map>

#define mn(a,b) ((a<b) ? (a) : (b))        		
#define mx(a,b) ((a<b) ? (b) : (a))			
#define ab(a) ((a<0) ? (-(a)) : (a))			
#define fr(a,b) for(int a=0; a<b; ++a)			
#define fe(a,b,c) for(int a=b; a<c; ++a)		
#define fw(a,b,c) for(int a=b; a<=c; ++a)		
#define df(a,b,c) for(int a=b; a>=c; --a)		
#define BIG 1000000000	
#define MAX_STRING 100000
#define PB push_back
#define MP make_pair

using namespace std;

int t,r,k,n,cur;
__int64 g[1000], sum[1000], next[1000];
__int64 res;

int main()
{
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
scanf("%d", &t);
fr(x,t)
	{
	printf("Case #%d: ", x+1);
	scanf("%d%d%d", &r, &k, &n);
	fr(i,n)
		scanf("%d", &g[i]);
	fr(i,n)
		{
		sum[i] = 0;
		sum[i] = g[i];
		cur = (i+1)%n;
		while(sum[i]+g[cur]<=k&&cur!=i)
			{
			sum[i]+=g[cur];
			cur = (cur+1)%n;
			}
		next[i] = cur;
		}
/*
	cout<<"Groups: ";
	fr(i,n)
		cout<<g[i]<<" ";
	cout<<endl;

	cout<<"Sums: ";
	fr(i,n)
		cout<<sum[i]<<" ";
	cout<<endl;

	cout<<"Nexts: ";
	fr(i,n)
		cout<<next[i]<<" ";
	cout<<endl;
*/
	cur = 0;
	res = 0;
	fr(i,r)
		{
//		cout<<"Result: "<<res<<endl;
//		cout<<"Current: "<<cur<<endl;
		res+=sum[cur];
		cur = next[cur];
		}
	cout<<res;
	printf("\n");
	}
return 0;
}
