#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <string>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const int INF = numeric_limits<int>::max();

//const ll nmax = 1000000000000LL;
const int pmax = 1000005;
bool comp[pmax];
vector<int> primes;

int main(int argc,char* argv[])
{
	for(int i=2;i<pmax;i++)
		if(!comp[i])
		{
			primes.push_back(i);
			for(int j=i*2;j<pmax;j+=i)
				comp[j]=true;
		}
	/*printf("%d\n", primes.size());
	for(int i=0;i<20;i++)
		printf("%d ", primes[i]);
	printf("%d\n", primes.back());
	*/
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
		ll n;
		scanf("%lld", &n);

		int s = 0;
		if(n>1)
		{
			s=1;	
			for(int i=0;i<primes.size();i++)
			{
				int p = primes[i];
				int k=0;
				for(ll pk=p; pk <= n; pk*=p)
					k++;
				//printf("%d %d\n", p, k);
				if(k<2)
					break;
				s += k-1;
			}
		}

		printf("Case #%d: %d\n",test_case,s);
	}
    return 0;
}
