#include <cstdio>
#include <algorithm>
#include <map>

using namespace std;

int b[32][32];

int main(){
	int tc, t;
	scanf("%d", &tc);
	for(t=0;t<tc;++t){
		int n, m, tmp;
		char s[2];
		scanf("%d %d", &m, &n);
		s[1] = '\0';
		s[0] = getchar();
		for(int i=0; i<m; ++i){
			for(int j=0; j<n/4; ++j){
				s[0] = getchar();
				sscanf(s, "%x", &tmp);
				b[i][j*4+0] = !!(tmp & (1<<3));
				b[i][j*4+1] = !!(tmp & (1<<2));
				b[i][j*4+2] = !!(tmp & (1<<1));
				b[i][j*4+3] = !!(tmp & (1<<0));
			}
			s[0] = getchar();
		}
		map<int, int> erg;
		for(int q = min(min(n, m), 32); q>0; --q){
			int c = 0;
			for(int ai=0; ai<=m-q; ++ai){
				for(int aj=0; aj<=n-q; ++aj){
					int r = b[ai][aj];
					if(r == -1)
						goto nl;
					for(int i=0; i<q; ++i){
						for(int j=0; j<q; ++j){
							if(b[ai+i][aj+j] == -1)
								goto nl;
							if(b[ai+i][aj+j] != r ^ ((i+j)&1))
								goto nl;
						}
					}
					for(int i=0; i<q; ++i)
						for(int j=0; j<q; ++j)
							b[ai+i][aj+j] = -1;
					++c;
nl:
					;
				}
			}
			if(c)
				erg[-q] = c;
		}
		int su = 0;
		printf("Case #%d: %d\n", t+1, erg.size());
		for(map<int, int>::iterator iter = erg.begin(); iter != erg.end(); ++iter){
			printf("%d %d\n", -iter->first, iter->second);
			su += iter->first * iter->first * iter->second;
		}
	}
}
