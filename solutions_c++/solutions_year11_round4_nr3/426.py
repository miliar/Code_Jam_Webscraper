#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<cstdio>
#include <ctime>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000
#define maxn 1000000

//typedef long long  LL;
typedef __int64 LL;

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

int primes[100000],sz;
char flag[2000005];

void sieve()
{
	int i,j;
	for(i=2;i*i<=maxn;i++)
		if(!flag[i])
			for(j = i*i ; j<=maxn ; j+=i) flag[j] = 1;

	for(i=2;i<=maxn;i++)
		if(!flag[i])	primes[sz++] = i;
}


int main()
{
	int i,j,k,tests,cs=0;
	LL n;

	sieve();

	//freopen("E:\\GCJ\\Csmall.in","r",stdin);
	freopen("E:\\GCJ\\Clarge.out","w",stdout);

	scanf("%d",&tests);

	while(tests--)
	{
		scanf("%I64d",&n);
		LL ans = 1;

		for(i=0;  i<sz ;i++)
		{
			if((LL)primes[i]*primes[i]>n) break;
			LL m=n,cnt=0;
			while(m/primes[i])
				m /= primes[i],cnt++;
			//printf("%I64d %d\n",m,cnt);
			ans += (cnt-1);
		}

	
		if(n==1)
			printf("Case #%d: %d\n",++cs,0);
		else
			printf("Case #%d: %I64d\n",++cs,ans);

	
	}

	return 0;
} 


