#include<cstdio>
#include<cstdlib>
#include<vector>
#include<algorithm>

#define MAXN 105

using namespace std;

bool used[MAXN];
inline bool lt(vector<int> a, vector<int> b) {
	for(int i = 0; i<a.size(); i++) {
		if(a[i] >= b[i]) return false;
	}
	return true;
}

int main() {
	FILE *fin = fopen("C.in","r"), *fout = fopen("C.out","w");
	int T;
	fscanf(fin,"%d",&T);
	for(int t = 1; t<=T; t++) {
		int N, K, ans = 0;
		vector<int> a[MAXN];
		fscanf(fin,"%d%d",&N,&K);
		for(int i = 0; i<N; i++) {
			used[i] = 0;
			for(int j = 0; j<K; j++) {
				int l;
				fscanf(fin,"%d",&l);
				a[i].push_back(l);
			}
		}
		sort(a,a+N);
		for(int mask = 0; mask < (1<<N); mask++) {
			bool okay = true;
			for(int i = 0; i<N; i++) {
				if(mask & (1<<i)) {
					for(int j = i; j<N; j++) {
						if(mask & (1<<j)) {
							if(lt(a[i],a[j])) {
								okay = false;
								break;
							}
						}
					}
					if(!okay) break;
				}
			}
			if(okay) {
				int count = 0;
				for(int i = 0; i<N; i++) {
					if(mask & (1<<i)) {
						count++;
					}
				}
				if(count > ans) ans = count;
			}
		}
		fprintf(fout,"Case #%d: %d\n",t,ans);
	}
}
