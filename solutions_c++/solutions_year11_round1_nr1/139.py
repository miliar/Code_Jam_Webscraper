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

LL gcd(LL a, LL b)
{
	return b ? gcd(b,a%b) : a;
}
int T;
int main() 
{ 
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for (int test=1;test<=T;test++)
	{
		printf("Case #%d: ",test);
		int pa,pb;
		LL n;
		scanf("%lld%d%d",&n,&pa,&pb);
		if (pb == 100 && pa < 100)
		{
			printf("Broken\n");
			continue;
		}
		if (pb == 0 && pa > 0)
		{
			printf("Broken\n");
			continue;
		}
		if (pb == 0 || pa == 0)
		{
			printf("Possible\n");
			continue;
		}
		int g = gcd(100,gcd(pa,100-pa));
		int Min = pa/g+(100-pa)/g;
		if (Min <= n)
			printf("Possible\n");
		else
			printf("Broken\n");
	}
	return 0; 
}