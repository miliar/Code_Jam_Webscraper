#include <stdio.h>
char a, b, c;
int adj[256][256];
int op[256][256], txt[101];
int main() {
	int i, j, T, t,k, l;
	freopen("google.in","r",stdin);
	freopen("google.out","w",stdout);
	scanf("%d", &T);
	for(i=0;i<T;i++) {
		scanf("%d", &k);
		for(j=0;j<256;j++) for(l=0;l<256;l++) adj[j][l] = op[j][l] = 0;
		for(j=0;j<k;j++){
			 scanf(" %c%c%c ",&a,&b,&c);
			 adj[a][b] = c;
			 adj[b][a] = c;
		}
		scanf("%d", &k);
		for(j=0;j<k;j++){
			 scanf(" %c%c ",&a,&b);
			 op[a][b] = 1;
			 op[b][a] = 1;
		}
		t = 0;
		scanf("%d", &k);
		for(j=0;j<k;j++){
			scanf(" %c ",&a);
			txt[t] = a;
			if(t>0 && adj[txt[t-1]][a]>0)txt[t-1] = adj[txt[t-1]][a]; 
			else t++;
			for(l=0;l<t;l++)if(op[txt[l]][txt[t-1]]==1)break;
			if(l<t)t = 0;
		}
		
		printf("Case #%d: [", i+1);
		for(j=0;j<t-1;j++) printf("%c, ", txt[j]);
		if(t>0)printf("%c", txt[j]);
		printf("]\n");
	}
	return 0;	
}
