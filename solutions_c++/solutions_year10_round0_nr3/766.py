#include <cstdio>

int t[1000];
int s[1000];
int v[1000];

int main(int argc, char* argv[])
{
	
	freopen("input.txt","r", stdin);
	freopen("output.txt","w", stdout);
	int c; scanf("%d", &c);
	for(int i = 0; i<c;i++){
		int R, k, N; scanf("%d%d%d", &R, &k, &N);
		for(int j = 0; j<N; j++) scanf("%d", v+j);

		for(int j = 0; j<N; j++){
			int tot = 0;
			for(int g = 0; g<N; g++){
				tot+=v[(j+g)%N];
				if(tot>k) break;
				t[j]=(j+g+1)%N;
				s[j]=tot;
			}
		}

		int p = 0;
		long long res = 0;
		for(int j = 0; j<R; j++){
			res+=s[p];
			p = t[p];
		}
		/*printf("// %d %d %d", R, k, N);
		for(int j = 0; j<N; j++){
			printf("(%d,%d) ", t[j], s[j]);
		}*/
		printf("Case #%d: %lld\n", i+1, res);
	}

}

