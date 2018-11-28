#include<cstdio>
#include<cstdlib>

#define MAXN 1005

using namespace std;

int g[2*MAXN], next[MAXN], earn[MAXN], prev[MAXN];
long long oldans[MAXN];

int main() {
	FILE *fin = fopen("C.in","r"), *fout = fopen("C.out","w");
	int T;
	fscanf(fin,"%d",&T);
	for(int t = 1; t<=T; t++) {
		int R, k, N;
		long long ans = 0;
		fscanf(fin,"%d%d%d",&R,&k,&N);
		for(int i = 0; i<N; i++) {
			fscanf(fin,"%d",&g[i]);
			g[N+i] = g[i];
		}
		int p1 = 0, p2 = 0, used = 0;
		while(p1 < N) {
			while(p2 < p1+N && used + g[p2] <= k) {
				used += g[p2];
				p2++;
			}
			next[p1] = p2;
			earn[p1] = used;
			used -= g[p1];
			prev[p1]=-1;
			p1++;
		}
		int p = 0;
		bool skipped = false;
		for(int i = 0; i<R; i++) {
			if(prev[p] != -1 && !skipped) {
				int dt = i - prev[p];
				long long dans = ans - oldans[p];
				int q = (R-i-1)/dt;
				ans += dans*q;
				R -= dt*q;
				skipped = true;
			}
			prev[p] = i;
			oldans[p] = ans;
			ans += earn[p];
			p = next[p]%N;
		}
		fprintf(fout,"Case #%d: %lld\n",t,ans);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
