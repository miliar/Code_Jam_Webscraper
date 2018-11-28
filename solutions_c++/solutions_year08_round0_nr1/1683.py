#include<stdio.h>
#include<string.h>
int casos,S,Q,i,j,t,k,dp[2000][2000],id,res;
char cadena[2000],buscadores[2000][2000],solicitud[2000];

int min( int u, int v, int aum){
	if( u == -1 && v== -1)
		return -1;
	if( u == -1)
		return v;
	if( v == -1)
		return u + aum;
	return (u+aum) < v? (u+aum):v; 
}
	
main(){
	scanf("%d",&casos);
	//printf("%d\n",casos);
	gets(cadena);
	for(k=1; k<=casos; k++){
		
		scanf("%d",&S);
	//	printf("%d\n",S);
		gets(cadena);
		for(i=1; i<=S; i++){
			gets(buscadores[i]);
	//		printf("%s\n",buscadores[i]);
		}
		memset(dp,-1,sizeof(dp));
		scanf("%d",&Q);
	//	printf("%d\n",Q);
		gets(cadena);
		
		for(i=0; i<= S; i++)
			dp[0][i]= 0;
		for(i=1; i<=Q ; i++){
			gets(solicitud);
	//		printf("%s\n",solicitud);
			for( j=1; j<=S; j++)
				if( strcmp( solicitud, buscadores[j] ) ==0){	
					id= j;
					break;
				}
	//		printf("%d\n",id);
			for(j=1; j<=S ; j++)
				if( j!= id){
					for(t=1; t<=S ; t++)
						if( j== t)
							dp[i][j]=min( dp[i-1][t],dp[i][j], 0);
						else
							dp[i][j]= min( dp[i-1][t] ,dp[i][j],1);
				}else{
					dp[i][j]= -1;
				}
	//		for(j=1; j<=S; j++)
	//			printf("%d ",dp[i][j]);
	//		printf("\n");
		}

		res= 1<<30;
		for(i=1; i<=S; i++)
			if( res > dp[Q][i] && dp[Q][i]!= -1)
				res= dp[Q][i];
		printf("Case #%d: %d\n",k,res);
	}
	return 0;
}

			
