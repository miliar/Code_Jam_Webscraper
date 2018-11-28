#include<stdio.h>
#include<string.h>

int main()
{
	int i,j,k,sol[4],d;
	int N, Li=19 ,Lj;
	int c[21][502];
	char X[21]=" welcome to code jam";
	char Y[502], buf;


	scanf("%d%c", &N,&buf);

	for(k=0;k<N;){
		gets(Y+1);
//		Y[0]='9';
		Lj = strlen(Y)-1;
//		printf("%s %d\n", Y, Lj);
//		printf("%s\n", X);

		for(i=0;i<21;i++){
			for(j=0;j<502;j++){
				c[i][j]=0;
			}
		}
		for(j=1;j<=Lj;j++){
			if( Y[j]=='w' )
				c[1][j]=c[1][j-1]+1;
			else 
				c[1][j]=c[1][j-1];
		}

		for(i=2;i<=Li;i++){
			for(j=2;j<=Lj;j++){
				if( X[i]==Y[j] )
					c[i][j]=c[i][j-1]+c[i-1][j-1];
				else
					c[i][j]=c[i][j-1];
				if( c[i][j]>=10000 )
					c[i][j]=c[i][j]%10000;
			}
		}
/*
		for(i=0;i<=Li;i++){
			for(j=0;j<=Lj;j++){
				printf("%d ", c[i][j]);
			}
			printf("\n");
		}
//		printf("%d\n", c[Li][Lj]);
		k++;
*/
		d=c[Li][Lj];
		sol[0]=d/1000;
		d=d%1000;
		sol[1]=d/100;
		d=d%100;
		sol[2]=d/10;
		sol[3]=d%10;

		printf("Case #%d: %d%d%d%d\n", ++k,sol[0],sol[1],sol[2],sol[3]);

	}

	return 0;
}