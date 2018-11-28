#include <stdio.h>
#include <string.h>

int n,t;
int sum[5000010];
int s[22];

void printBm(int d) {
	bool space=false;
	for (int i=0; i<n; i++)
		if (d&(1<<i)) {
			if (space) printf(" ");
			else space=true;

			printf("%d", s[i]);
		}
	printf("\n");
}

int main() {
	scanf("%d", &t);

	for (int it=1; it<=t; it++) {
		memset(sum,-1,sizeof(sum));
		scanf("%d", &n);		
		
		for (int i=0; i<n; i++)
			scanf("%d", &s[i]); 
		
		printf("Case #%d:\n", it);

		int tmp=0;
		bool gotit=false;

		for (int i=0;i<(1<<n); i++) {
			tmp=0;

			for (int j=0; j<n; j++)
				if (i&(1<<j)) tmp+=s[j];

			if (sum[tmp]==-1) sum[tmp]=i;
			else {
				printBm(sum[tmp]);
				printBm(i);
				gotit=true;
				break;
			} 
		}
		
		if (!gotit) printf("Impossible\n");
	}
	
	return 0;
}
