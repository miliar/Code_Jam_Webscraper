#include <algorithm>
#include <vector>
#include <string>
using namespace std;
bool check[1000001];
int sosu[80000];
long long dat[11];
int T, D, K;
long long per(long long a, long long b){
	long long c = a % b;
	if( c < 0 ) return c + b;
	return c;
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	int t;
	int i, j, k, c = 0;
	check[0] = check[1] = true;
	for(i=2;i<=1000000;i++){
		if(!check[i]){
			sosu[c++] = i;
			for(j=i+i;j<=1000000;j+=i) check[j] = true;
		}
	}
	for(t=1;t<=T;t++){
		printf("Case #%d: ", t);
		scanf("%d %d",&D,&K);
		int i, x = 1, xx = 1, p;
		long long pre, A, B, Bt, P, y = -1, yt;
		for(i=0;i<D;i++){
			x *= 10;
		}
		for(i=0;i<K;i++){
			scanf("%d",&dat[i]);
			if(dat[i] > xx) xx = dat[i];
		}
		if(K <= 1){
			printf("I don't know.\n");
			continue;
		}
		for(p=0;p<c;p++){
			P = sosu[p];
			if(P <= xx) continue;
			if(P > x) break;
			for(A=0;A<P;A++){
				B = per((long long)dat[1] - A * dat[0], P);
				for(i=2;i<K;i++){
					Bt = per((long long)dat[i] - A * dat[i-1], P);
					if(Bt != B) break;
				}
				if(i == K){
					yt = per(A*dat[K-1]+B, P);
					if(y<0) y = yt;
					else if(y != yt) break;
				}
			}
			if(A<P) break;
		}
		if(p<c && P <= x)
			printf("I don't know.\n");
		else printf("%I64d\n",y);
	}
	return 0;
}