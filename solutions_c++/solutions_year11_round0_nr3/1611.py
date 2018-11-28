#include <cstdio>
#include <cstring>
using namespace std;

int c[20];
int main()
{
	int T,N,nCase=0;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	while(T--) {
		scanf("%d",&N);
		int tmp = 0, sum = 0, mn = 100000000;
		for(int i = 0; i < N; i++) {
			scanf("%d",&c[i]);
			tmp ^= c[i];
			if(c[i] < mn) {
				mn = c[i];
			}
			sum += c[i];
		}
		printf("Case #%d: ",++nCase);
		if(tmp) {
			printf("NO\n");
		}
		else
			printf("%d\n",sum - mn);
	}
	return 0;
}