#include <stdio.h>
#define MAX 2000010

int pot10(int i){
	int ret = 1;
	while(i = i/10)
		ret*=10;
	return ret;
}

int shift(int i,int pot){
	int r = i%10;
	r = (i/10)+(pot*r);
	if(pot10(r) != pot)
		r = -r;
//	printf("  shift %d %d\n",i,r);
	return r;
}


int main(){
	int table[MAX+1];
	int n;
	scanf("%d",&n);
	int A,B;
	for(int i = 0;i<n;i++){
		scanf("%d %d",&A,&B);
		for(int j = A;j<=B;j++){
			table[j] = -1;
		}
		int ng = 0;
		int nvals = 0;
		int total = 0;
		for(int j = A;j<=B;j++){

		//	printf("<%d>\n",j);
			if(table[j] != -1)
				continue;
		//	printf(" <%d>\n",j);
			int inicial = j;
			table[j] = ng;
			nvals = 1;
			int pot = pot10(j);
			int r = j;
			while(1){
				r = shift(r,pot);
				if(r < 0){
					continue;
				}
				if(r == inicial){
					break;
				}
				if(r<=B && r>= A){
					table[r] = ng;
					nvals++;
				}
			}
			if ((nvals*(nvals-1)) < 0)
				fprintf(stderr,"FUUU, tem valor negativo!\n");
			total+=((nvals)*(nvals-1))/2;
			ng++;
		}
	//	for(int j = A;j<=B;j++){
	//		printf("%d gr: %d\n",j,table[j]);
	//	}
		printf("Case #%d: %d\n",i+1,total);
	}
	return 0;
}
