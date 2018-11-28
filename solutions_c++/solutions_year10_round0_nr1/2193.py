#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

#define runa true


#if runa
int main()
#else
int A()
#endif
{
#ifndef ONLINE_JUDGE
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	int N, K;

	int cse, cnt;
	scanf("%d\n", &cse);
	for(cnt=1;cnt<=cse;cnt++){
		scanf("%d %d", &N, &K);


		int mod = (1 << N);
		if( (K % mod) == mod-1 )
			printf("Case #%d: ON\n", cnt);
		else
			printf("Case #%d: OFF\n", cnt);

	}
	return 0;
}
