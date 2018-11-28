#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;

double r[5],w[30],ca[15],p,f,pr[30];

int main(){
//	freopen("As.IN","r",stdin);
//	freopen("w.txt","w",stdout);

	int i,T,j,A,B,k;

	scanf("%d",&T);
	for(i=1;i<=T;i++){

		scanf("%d%d",&A,&B);

		for(j=0;j<A;j++){
			scanf("%lf",&r[j]);
			w[j]=1.0-r[j];
		}


		if(A==1){

			p=B*r[0]+(2*B+1)*w[0];
			f=(B+2)*r[0]+(B+2)*w[0];

			if(p<f)
				printf("Case #%d: %lf\n",i,p);
			else
				printf("Case #%d: %lf\n",i,f);


		}

		else if(A==2){

			pr[0]=r[0]*r[1];
			pr[1]=r[0]*w[1];
			pr[2]=w[0]*r[1];
			pr[3]=w[0]*w[1];

			k=0;
			ca[k++]=pr[0]*(B-1)+(1-pr[0])*(2*B);
			ca[k++]=(pr[0]+pr[1])*(B+1)+(pr[2]+pr[3])*(2*B+2);
			ca[k++]=B+3;
			ca[k++]=B+2;

			sort(ca,ca+4);
			printf("Case #%d: %lf\n",i,ca[0]);

		}

		else{

			pr[0]=r[0]*r[1]*r[2];
			pr[1]=r[0]*r[1]*w[2];
			pr[2]=r[0]*w[1]*r[2];
			pr[3]=r[0]*w[1]*w[2];
			pr[4]=w[0]*r[1]*r[2];
			pr[5]=w[0]*r[1]*w[2];
			pr[6]=w[0]*w[1]*r[2];
			pr[7]=w[0]*w[1]*w[2];

			k=0;
			ca[k++]=pr[0]*(B-2)+(pr[1]+pr[2]+pr[3]+pr[4]+pr[5]+pr[6]+pr[7])*(2*B-1);
			ca[k++]=(pr[0]+pr[1])*(B)+(pr[2]+pr[3]+pr[4]+pr[5]+pr[6]+pr[7])*(2*B+1);
			ca[k++]=(pr[0]+pr[1]+pr[2]+pr[3])*(B+2)+(pr[4]+pr[5]+pr[6]+pr[7])*(2*B+3);
			ca[k++]=B+4;
			ca[k++]=B+2;

			sort(ca,ca+5);
			printf("Case #%d: %lf\n",i,ca[0]);



		}

	}



  return 0;
}