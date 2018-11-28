#include <stdio.h>
#include <algorithm>
#define MAXLEN 10

using namespace std;

inline bool isSet(int num, int ind){
	return num & (1<<ind);
}

int main()
{
	int icase, ncase;
	char map[MAXLEN][MAXLEN+1];
	int table[2][1<<MAXLEN];
	int *last, *now, *ptmp;
	int N, M, i, j, k, l;
	int num, ans;
	int n;

	scanf("%d", &ncase);
	for(icase=0; icase<ncase; ++icase){
		scanf("%d%d", &M, &N);
		for(i=0; i<M; ++i)
			scanf("%s", map[i]);
		n = 1<<N;
		for(i=0; i<n; ++i)
			table[0][i] = table[1][i] = 0;

		last = table[0];
		now = table[1];

		for(i=0; i<M; ++i){
			for(j=0; j<n; ++j){
				//valid.
				for(k=0; k<N; ++k){
					if(isSet(j,k)){
						if(map[i][k] == 'x') 
							break;
						if(k != 0 && isSet(j, k-1))
							break;
						if(k != N && isSet(j, k+1))
							break;
					}
				}
				if(k != N)
					continue;
				//fprintf(stderr, "valid: %d\n", j);
				//count num.
				num = 0;
				for(k=0; k<N; ++k)
					if(isSet(j,k))
						++num;
				//look up.
				for(k=0; k<n; ++k){
					for(l=0; l<N; ++l){
						if(isSet(j, l)){
							if(l!=0 && isSet(k,l-1))
								break;
							if(l!=N && isSet(k,l+1))
								break;
						}
					}		
					//fprintf(stderr, "validk: %d\n", k);
					if(l == N &&  last[k] + num > now[j])
						now[j] = last[k] + num;
				}
			}
			ptmp = last;
			last = now;
			now = ptmp;
		}

		ans = 0;
		for(i=0; i<n; ++i)
			if(last[i] > ans)
				ans = last[i];

		printf("Case #%d: %d\n", icase+1, ans);
	}
	return 0;
}
