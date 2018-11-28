#include <stdio.h>
char A[100][100];
double Wins[100], Tot[100];
double WP[100], OWP[100],OOWP[100],c,tot;
int main() {
	int i, j, T, t, k;
	freopen("google.in","r",stdin);
	freopen("google.out","w",stdout);
	scanf("%d", &T);
	for(t=0;t<T;t++) {
		scanf("%d", &k);
		for(i=0;i<k;i++)scanf("%s", A[i]);
		for(i=0;i<k;i++) {
				Wins[i]=Tot[i]=0;
			for(j=0;j<k;j++) {
				if(A[i][j]=='0')Tot[i]++; 
				if(A[i][j]=='1')Wins[i]++,Tot[i]++; 
			}
			WP[i] = Wins[i]/Tot[i];
		}
		for(i=0;i<k;i++) {
			tot = c = 0;
			for(j=0;j<k;j++) {
				if(A[i][j]=='0')c+=(Wins[j] - 1)/(Tot[j]-1),tot++; 
				if(A[i][j]=='1')c+=(Wins[j] - 0)/(Tot[j]-1),tot++; 
			}
			OWP[i] = c/tot;
		}
		printf("Case #%d:\n", t+1);
		for(i=0;i<k;i++) {
			tot = c = 0;
			for(j=0;j<k;j++) {
				if(A[i][j]=='0')c+=OWP[j],tot++; 
				if(A[i][j]=='1')c+=OWP[j],tot++; 
			}
			OOWP[i] = c/tot;
			printf("%.12lf\n", 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
		}
	}
	return 0;	
}
