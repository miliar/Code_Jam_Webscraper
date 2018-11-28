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

#define INF 0x7fffffff
#define Pi acos(-1.0)
#define  Eps 1e-6

#ifdef _GNUC_
#define int64 long long
#define Printf64(n) printf("%lld\n", n)
#else /* MSVC, say */
#define int64 __int64
#define Printf64(n) printf("%I64d\n", n)
#endif 

#define MAX 100

int main()
{
	int i, j, k, n, m,  test, cnt=0;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout); 

	char buff[100];

	scanf("%d", &test);
	int outC=0;
	while(test--)
	{
		scanf("%d", &n);
		sprintf(buff, "%d", n);
		int a[10]={0}, b[10]={0};
		for(i=0; buff[i]; ++i)
			++a[buff[i]-'0'];
		
		for(m=n+1; ; ++m)
		{
			sprintf(buff, "%d", m);
			memset(b, 0, sizeof(b));
			for(i=0; buff[i]; ++i)
				++b[buff[i]-'0'];
			for(i=1; i<10; ++i)
			{
				if(a[i]!=b[i])
					break;
			}
			if(i>=10)
				break;
		}

		printf("Case #%d: %d\n", ++outC, m);
	}

	return 0;
}

