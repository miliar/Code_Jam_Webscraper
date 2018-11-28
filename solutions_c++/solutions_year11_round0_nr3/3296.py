#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

inline int max(const long long &a, const long long &b)
{
	return a>b ? a : b;
}

int N,T;
int nums[1024];
bool used[1024];
int ans;

void check()
{
	bool hazUsed = false;
	bool hazNotUsed = false;
	int xorUsed = 0;
	int xorNotUsed = 0;
	long long sum=0;
	for(int i=0;i<N;i++)
	{
		hazUsed |= used[i];
		hazNotUsed |= !used[i];
		used[i] ? xorUsed ^= nums[i],sum+=nums[i] : xorNotUsed ^= nums[i];
		
	}

	if(hazUsed && hazNotUsed && xorUsed == xorNotUsed)
		ans = max(ans,sum);
}

void generate(int pos)
{
	if(pos == N)
	{
		check();
		return;
	}
	used[pos]=true;
	generate(pos+1);
	used[pos]=false;
	generate(pos+1);
}

void solve(int test)
{
	ans = -1;
	scanf("%d",&N);
	
	for(int i=0;i<N;i++)
	{
		scanf("%d",nums +i);	
	}

	generate(0);

	ans == -1 ? 
		printf("Case #%d: NO\n",test):
		printf("Case #%d: %d\n",test,ans);

}

int main()
{
	scanf("%d",&T);

	for(int t=1;t<=T;t++)
	{
		solve(t);
	}
}