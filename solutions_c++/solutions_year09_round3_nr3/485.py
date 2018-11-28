//pku
#include "iostream"
#include "sstream"
#include "iomanip"
#include "algorithm"
#include "string"
#include "functional"
#include "list"
#include "vector"
#include "stack"
#include "deque"
#include "set"
#include "map"
#include "utility"
#include "numeric"
#include "cmath"
using namespace std;

#define min(a, b) ((a)<(b)?(a):(b))
#define min3(a, b, c) ((a)<(b)?((a)<(c)?(a):(c)):((b)<(c)?(b):(c)))
#define max(a, b) ((a)>(b)?(a):(b))
#define max3(a, b, c) ((a)>(b)?((a)>(c)?(a):(c)):((b)>(c)?(b):(c)))

#define INF 0x07ffffff
#define Pi acos(-1.0)
#define  Eps 1e-6

#ifdef _GNUC_
#define int64 long long
#define Printf64(n) printf("%lld\n", n)
#else /* MSVC, say */
#define int64 __int64
#define Printf64(n) printf("%I64d\n", n)
#endif 

#define MAX 10010

int n, q;
int re[200];

int small()
{
	sort(re, re+q);

	int die=1, i, j;
	for(i=2; i<=q; ++i) die*=i;
	int minR=INF;
	do
	{
		bool flag[200]={0};
		int total=0;
		for(i=0; i<q; ++i)
		{
			int cost=0;
			flag[re[i]]=true;
			for(j=re[i]+1; j<=n && !flag[j]; ++j, ++cost);
			for(j=re[i]-1; j>0 && !flag[j]; --j, ++cost);
			total+=cost;
		}
		minR=min(minR, total);
		next_permutation(re, re+q);

	}while(die--);

	return minR;

}

int main()
{
	int i, j, k, m,  test, cnt=0;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout); 

	scanf("%d", &test);
	int outC=0;
	while(test--)
	{
		cin>>n>>q;
		for(i=0; i<q; ++i)
			cin>>re[i];

		int res = small();


		printf("Case #%d: %d\n", ++outC, res);
	}

	return 0;
}

