#include <cstdio>
#include <cstring>

using namespace std;

int L, D, N;

int words[5005][20];
int in[20];

int main(){
	int c;
	scanf("%d %d %d\n", &L, &D, &N);
	for(int i=0; i<D; ++i){
		for(int j=0; j<L; ++j)
			words[i][j] = 1 << (getchar()-'a');
		getchar();
	}
	for(int tc=1; tc<=N; ++tc){
		for(int i=0; i<L; ++i){
			c = getchar();
			in[i] = 1<<(c-'a');
			if(c == '('){
				in[i] = 0;
				for(c = getchar(); c != ')'; c = getchar())
					in[i] |= 1<<(c-'a');
			}
		}
		getchar();
		int res = 0;
		for(int i=0; i<D; ++i){
			int r = 1;
			for(int j=0; j<L; ++j)
				r = r && !!(words[i][j] & in[j]);
			res += r;
		}
		printf("Case #%d: %d\n", tc, res);
	}
}
