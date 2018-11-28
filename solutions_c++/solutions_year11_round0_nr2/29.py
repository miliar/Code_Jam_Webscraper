#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

enum Tip {
	EMPTY=32,
	OPPOSITE=64
};

int main()	{
	int T = 0;
	scanf("%d",&T);
	char X[32][32];
	char str[101];
	char rez[101];
	for(int i=0; i!=T; ++i)	{
		int j,N=0;
		memset(X,EMPTY,sizeof(X));
		scanf("%d",&N);
		for(j=0; j!=N; ++j)	{
			scanf("%s",str);
			//printf("C: %s\n",str);
			char a = str[0]-'A', b = str[1]-'A';
			X[a][b] = X[b][a] = str[2]-'A';
		}
		scanf("%d",&N);
		for(j=0; j!=N; ++j)	{
			scanf("%s",str);
			//printf("D: %s\n",str);
			char a = str[0]-'A', b = str[1]-'A';
			X[a][b] = X[b][a] |= OPPOSITE;
		}
		scanf("%d %s",&N,str);
		//printf("N: %s\n",str);
		for(j=N=0; str[j]; ++j)	{
			char cur = str[j]-'A';
			//printf("Cur (N=%d) %d: ",N,cur);
			char prev = 31;
			if(N) prev = rez[N-1];
			char q = X[cur][prev] & ~OPPOSITE;
			//printf(" (q=%d,prev=%d) ",q,prev);
			if (q<32)	{
				//printf("combo\n");
				rez[N-1] = q;
				continue;
			}
			int k;
			for(k=0; k!=N; ++k)
				if(X[cur][rez[k]] & OPPOSITE)
					break;
			if (k!=N)	{
				//printf("clear\n");
				N=0;
				continue;
			}
			//printf("ok\n");
			rez[N++] = cur;
		}
		rez[N] = 0;
		printf("Case #%d: [",i+1);
		for(j=0; j!=N; ++j)	{
			if(j)	printf(", ");
			putchar(rez[j]+'A');
		}
		printf("]\n");
	}
	return 0;
}

