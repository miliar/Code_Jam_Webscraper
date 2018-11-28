#include<stdio.h>

int main()
{
	int L,D,N,K,X=1;
	int i,j,k;
	char buf,d;
	char dic[5001][16];
	char aln[27][16];

	scanf("%d%d%d", &L,&D,&N);
	scanf("%c", &buf);


	for(i=0;i<D;i++){
		for(j=0;j<L;j++){
			scanf("%c",&dic[i][j]);
		}
		scanf("%c", &buf);
	}
/*
	for(i=0;i<D;i++){
		for(j=0;j<L;j++){
			printf("%c",dic[i][j]);
		}
		printf("\n");	
	}
*/		

	while(N--){
	for(i=0;i<L;i++){
		scanf("%c",&d);
	//	printf("%c yes~!\n", d);

		if( d=='(' ){
	//		printf("come\n");
			for(j=0;;j++){
				scanf("%c",&d);
				if( d==')' ) {
					aln[j][i]='\0';	
					break;
				}
				else {
					aln[j][i]=d;
				}
			}
		}
		else {
			aln[0][i]=d;
			aln[1][i]='\0';
		}
	}
	scanf("%c", &buf);

/*
	for(i=0;i<L;i++){
		for(j=0; aln[j][i]!='\0' ;j++){
			printf("%c",aln[j][i]);
		}
		printf("\n");
	}
*/

	K=0;
	for(i=0;i<D;i++){
		for(j=0;j<L;j++){
			for(k=0; aln[k][j]!='\0' ;k++){
				if( dic[i][j]==aln[k][j] ) break;
			}
			if(aln[k][j]=='\0') break;
		}
		if(j==L) K++;
	}
	printf("Case #%d: %d\n", X++, K);


	for(i=0;i<27;i++){
		for(j=0;j<16;j++){
			aln[i][j]=0;
		}
	}
	

	}


	return 0;
}