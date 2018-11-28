#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>
#define h 1010

using namespace std;

int T,R,K,N,i,j,k,t,a[h],d[h];
long long p;
queue<int> Q;
vector<int> V;

int main() {
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d", &T);
	for(t=0;t<T;t++) {
		while(!Q.empty())
			Q.pop();
		scanf("%d%d%d", &R, &K, &N);
		for(i=0;i<N;i++) {
			scanf("%d", &a[i]);
			Q.push(a[i]);
		}
		memset(d, 0, sizeof d);
		for(i=0;i<R;i++) {
			V.clear();
			for(k=0;!Q.empty();) {
				j = Q.front();
				if(k + j > K)
					break;
				k += j;
				Q.pop();
				V.push_back(j);
			}
			d[i] = k;
			for(k=0;k<V.size();k++)
				Q.push(V[k]);
		}
		p = 0;
		for(i=0;i<R;i++)
			p += (long long) d[i];
		/*p *= (long long) (R / N);
		k = R % N;
		for(i=0;i<k;i++)
			p += (long long) d[i];*/
		printf("Case #%d: %lld\n", t+1, p);
	}
	return 0;
}