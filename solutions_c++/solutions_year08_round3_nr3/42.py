#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>

#define MOD (1000000007)
#define MAXN (600000)

using namespace std;

int n;
long long lim[MAXN];
long long tree[MAXN];

class cmp
{
	public:
		bool operator () (const int &a, const int &b) const
		{
			return lim[a]<lim[b];
		}
};

long long query(int idx)
{
	long long res = 0;
	
	//printf("q %d\n", idx);
	while (idx > 0)
	{
		//printf("idx %d\n", idx);
		res += tree[idx];
		//res %= MOD;
		//printf("tree %Ld %Ld\n", tree[idx], res);
		idx -= (idx & -idx);
	}
	
	return res;
}

void update(int idx ,long long val)
{
	//printf("u %d\n", idx);
	while (idx < MAXN)
	{
		//printf("uidx %d\n", idx);
		tree[idx] = (tree[idx]+val) % MOD;
		//printf("tree %Ld\n", tree[idx]);
		idx += (idx & -idx);
	}
}

void input(void)
{
	int m;
	long long XXX, opa=3, ZZZ;
	static long long A[128];
	
	cin>>n;
	cin>>m;
	cin>>XXX;
	cin>>opa;
	cin>>ZZZ;
	
	for(int i = 0; i < m; ++i)
	{
		scanf("%Ld", &A[i]);
	}
	
	for(int i = 0; i < n; ++i) 
	{
		lim[i] = A[i%m];
		//printf("%Ld ", lim[i]);
		A[i%m] = (XXX*A[i%m]+opa*((long long)i+1)) % ZZZ;
	}
	//printf("\n");
}

long long calc(void)
{
	static long long dp[600000];
	long long res = 1;

	
	static int idx[MAXN];
	
	for(int i = 0; i < n; ++i)
	{
		idx[i] = i;
	}
	sort(idx, idx+n, cmp());

	int curr=2;
	long long prev=lim[idx[0]];
	lim[idx[0]]=2;
	for(int i = 1; i < n; ++i)
	{
		if(prev != lim[idx[i]])
		{
			++curr;
		}
		prev = lim[idx[i]];
		lim[idx[i]] = curr;
	}
	
	memset(tree, 0, sizeof tree);
	dp[0] = 1;
	for(int i = 0; i < n; ++i)
	{
		dp[i] = 1 + query(lim[i]-1);
		update(lim[i], dp[i]);
                //printf("update %Ld %Ld\n", lim[i], dp[i]);
		//printf("%d %Ld\n", i, dp[i]);
		res = (res+dp[i]) % MOD;
	}
	
	return res;
}

int main(void)
{
	int N, i;

        memset(tree, 0, sizeof tree);
        update(2, 1);
        update(5, 1);
        //printf("%Ld %Ld %Ld\n", query(2), query(5), query(6));
	scanf("%d", &N);
	fprintf(stderr, "cases=%d\n", N);
	for(i = 1; i <= N; ++i)
	{
		fprintf(stderr, "%d\n", i);
		input();
		printf("Case #%d: %Ld\n", i, calc()-1);
	}
	return 0;
}
