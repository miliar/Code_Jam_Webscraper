#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<iterator>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<deque>
#include<stack>
#include<bitset>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iomanip>
#include<string>
#include<cmath>
#include<ctime>
using namespace std;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
long long int dp[500005][3],temp[500005];
long long mulmod(long long a,long long b,long long c){
	long long x = 0,y=a%c;
	while(b > 0){
		if(b%2 == 1){
			x = (x+y)%c;
		}
		y = (y*2)%c;
		b /= 2;
	}
	return x%c;
}

#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define debug 1
int main()
{
	int N;
	long long int n,m,x,y,z;
	scanf("%d",&N);
	for(int test=0;test<N;test++)
	{
		scanf("%lld %lld %lld %lld %lld",&n,&m,&x,&y,&z);
		memset(dp,0,sizeof(dp));
		for(int i=0;i<m;i++)
			scanf("%lld",&temp[i]);
		x%=z;y%=z;
		for(int i=0;i<n;i++)
		{
			dp[i][0] = temp[i%m];
			temp[i%m] = (mulmod(x,temp[i%m],z) + mulmod(y,(i+1),z))%z;
		}
		for(int i=0;i<n;i++)
			dp[i][2]=1;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<i;j++)
				if(dp[j][0] < dp[i][0])
				{
					dp[i][1]=dp[j][1]+1;
					dp[i][2]=(dp[i][2]+dp[j][2])%1000000007;
				}
		}
		long long int cnt=0;
		for(int i=0;i<n;i++)
			cnt=(cnt+dp[i][2])%1000000007;
		printf("Case #%d: %lld\n",test+1,cnt);
	}
	return 0;
}
