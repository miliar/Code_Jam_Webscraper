#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <queue> 
#include <deque> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
using namespace std; 

const int inf = 1000*1000*1000; 
#define CL(x,a) memset(x,a,sizeof(x)); 
#define ALL(v) (v).begin(),(v).end() 
#define PII pair<int,int> 
#define PDI pair<double,int> 
#define MP(a,b) make_pair(a,b) 
#define FOR(i,n) for(int i=0;i<n;i++) 
typedef long long LL; 
typedef vector<int> vi; 
typedef vector< vi > vvi; 
typedef vector< vector<PII > > vvpii; 
const int N = 2000000;
int T;
LL n;
int ar[N];
LL Pow(LL a, LL x)
{
	if (x == 0)
		return 1;
	if (x == 1)
		return a;
	LL t = Pow(a,x/2);
	return t*t*Pow(a,x%2);
}
int main() 
{ 
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	for (int i=2;i<N;i++)
	{
		if (ar[i])
			continue;
		for (int j=i+i;j<N;j+=i)
			ar[j]=1;
	}
	scanf("%d",&T);
	for (int test = 1;test <=T;test++)
	{
		LL res = 0;
		scanf("%lld",&n);
		if (n == 1)
		{
			res = 0;
		}
		else
		{
			res = 1;
			int p = 1;
			LL now = 1;
			while((now+1)*(now+1) <= n)
				now++;
			for (LL i=now;i>=2;i--)
			{
				if (ar[i] == 0)
				{
					res-=1;
					LL x = Pow(i,p);
					while(x*i <= n) 
					{
						p++;
						x*=i;
					}
					res+=p;
				}
			}
		}
		printf("Case #%d: %lld\n",test,res);
	}
	return 0; 
}