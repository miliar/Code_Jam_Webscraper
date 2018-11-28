#include<cstdio>

int main() {
	int T,A,B;
	double tab[100000];
	double tab2[100000];
	scanf("%d",&T);
	tab[0]=1;
	tab2[0]=1;
	for(int t=1;t<=T;t++) {
		scanf("%d %d",&A,&B);
		for(int i=1;i<=A;i++) {
			scanf("%lf",&(tab[i]));
			tab2[i]=tab2[i-1]*tab[i];
		}
		double min=2+B;
		for(int i=0;i<=A;i++) {
			double maybe=(A+B-2*i+1)*tab2[i]+
				(A+B-2*i+1+B+1)*(1-tab2[i]);
			if(maybe<min)
				min=maybe;
		}
		printf("Case #%d: %.6lf\n",t,min);
	}
	return 0;
}
