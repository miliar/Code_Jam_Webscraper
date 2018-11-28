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
#define int64 unsigned __int64
#define Printf64(n) printf("%I64d\n", n)
#endif 

#define MAX 100



int64 deal(char buff[])
{
	int i, j;
	char ch[128]={0};
	int num[128];
	int cntCh=0;

	for(i=0; buff[i]; ++i)
	{
		for(j=0; j<cntCh; ++j)
			if(ch[j]==buff[i]) break;
		if(j>=cntCh)
			ch[cntCh++]=buff[i];
	}
	num[0]=1;
	num[1]=0;
	for(i=2; i<100; ++i) num[i]=i;

	int zhi=max(2, cntCh);
	int64 res=0;
	for(i=0; buff[i]; ++i)
	{
		for(j=0; j<cntCh; ++j)
			if(buff[i]==ch[j]) break;
		res=res*zhi+num[j];
	}
	
	return res;

}


int main()
{
	int i, j, k, n, m,  test, cnt=0;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout); 

	char buff[128];

	scanf("%d", &test);
	int outC=0;
	while(test--)
	{
		cin>>buff;
		
		int64 res= deal(buff);

		printf("Case #%d: %I64u\n", ++outC, res);
	}

	return 0;
}

