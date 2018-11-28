#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int c, N, i, j, l, m;
char n[29];

#define SWAP(a,b) {int x; x=a;a=b;b=x;}


int main() {
	gets(n);
	N=atoi(n);
	for (c=1; c<=N; c++) {
		n[0]='0';
		gets(n+1);
		l=strlen(n);
		m=0;
		for(i=l-2; i>=0; i--) {
			for (j=i+1;j<l;j++)
				if (n[j]>n[i]) 
					if ((m==0) || (n[j]<n[m])) m=j;
			if (m!=0) break;
		}

		SWAP(n[i],n[m])

		for (i++;i<l-1;i++) 
			for (j=i+1;j<l;j++) 
				if (n[i]>n[j]) SWAP(n[j],n[i])
		

		printf("Case #%d: %s\n", c, n+(n[0]=='0'));
	}

}
