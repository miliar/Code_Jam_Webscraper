#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
typedef long long LL;

int a[10000];
int nn,n;
int main(){
	int nnt, ntt;
	scanf("%d", &nnt);
	for(ntt = 1; ntt<=nnt; ntt++){
		scanf("%d", &nn);
		n=0;
		for(int i=0; i<nn; i++){
		    int x, y;
			scanf("%d%d", &x, &y);
			for(int i=0; i<y; i++)a[n++] = x;
		}
		LL ans = 0;
		while(1){
			int did=0;
			sort(a, a+n);
			for(int i=0; i<n-1; i++)if(a[i]==a[i+1]){
				a[i]--;
				a[i+1]++;
				did=1;
				ans++;
			}
			if(!did)break;
		}
		printf("Case #%d: %lld\n", ntt, ans);
	}
	return 0;
}

