#include <cstdio>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main(int argc, char *argv[]) 
{
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small-attempt0.out","wt",stdout);
    
	int T, N, K, i, j, l;
	bool prev = false;
    int final;    

	scanf("%d", &T);

	for(i = 0; i < T; i++)	{
		scanf("%d %d", &N, &K);
		unsigned char * flag = (unsigned char *)calloc(N, 1);
		if(flag == NULL) {
			printf("malloc error"); exit(1);
		}

		for(j = 0; j < K; j++) {
			if (j % 2 == 0) {
				flag[0] = 1;
			} 
			else {
				prev = true;
				for(l = 0; l < N; l++) {
					if(!prev) {
						break;
					}

					if (flag[l] == 0) {
						prev = false;
						flag[l] = 1;
					} else {
						flag[l] = 0;
					}					
				}
			}
		}

	    final = 1;
		for(j = 0; j < N; j++)
		{
			if(flag[j] == 0)
			{
				final = 0;
				break;
			}
		}

		if(1 == final) {
		    printf("Case #%d: %s\r\n", i + 1, "ON");
		} else {
            printf("Case #%d: %s\r\n", i + 1, "OFF");
		}
		free(flag);
	}
}