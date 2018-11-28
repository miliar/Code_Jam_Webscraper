#include <stdio.h>
#include <stdlib.h>

int main(){
	int n;
	int t,c=0;
	int p = 0;
	int i,j,k;

	scanf("%d\n", &t); 

	while(++c <= t){
		scanf("%d %d", &n, &k);

		p = 0;		
		bool *s = (bool *)calloc(32 , sizeof(bool));

		/* init */
		for (j=1;j<=k;j++){
			for (i=0;i<=p;i++){
				s[i] = !s[i];
			}

			for (i=0;i<n && s[i];i++);

			p = i;
			
		}
		

		printf("Case #%d: ", c);
		printf((s[n-1] && p>=(n-1)) ? "ON" : "OFF");
		printf("\n");

	}


}
