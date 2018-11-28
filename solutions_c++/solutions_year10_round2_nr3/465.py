#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <utility>
#include <functional>
#include <cmath>
using namespace std;

const int M=100003;

int c[501][501];
bool cu[501][501];
int fm[501][501];
bool fu[501][501];

int C(int n,int k)
{
	if((n<0)||(k<0)||(k>n))
		return 0;
	if((n==0)&&(k==0))
		return 1;
	if(!cu[n][k])
	{
		c[n][k]=(C(n-1,k-1)+C(n-1,k))%M;
		cu[n][k]=true;
	}
	return c[n][k];
}

int f(int n,int k)
{
	if(k>=n)
		return 0;
	if(k==1)
		return 1;
	if(!fu[n][k])
	{
		int res=0;
		for(int i=max(1,2*k-n);i<k;i++)
			res=(res+((long long)f(k,i))*C(n-k-1,k-i-1))%M;
		fm[n][k]=res;
		fu[n][k]=true;
	}
	return fm[n][k];
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int num_tests;
	scanf("%d",&num_tests);
	for(int test=1;test<=num_tests;test++)
	{
		printf("Case #%d: ",test);
		int n;
		scanf("%d",&n);
		int res=0;
		for(int i=1;i<n;i++)
			res=(res+f(n,i))%M;
		printf("%d\n",res);
	}
	fclose(stdout);
	return 0;
}