#include<stdio.h>



int mat[2000][2000];
int M,N;






int isSquare ( int i , int j , int s ) {
	int state ;
	for ( int k = 0 ; k < s ; k ++ ) {
		state = 1-mat[i+k][j] ;
		if ( mat[i+k][j] == -1 ) { return 0 ; } 
		for ( int l = 0 ; l < s ; l ++ ) {
			if ( mat[i+k][l+j] == -1 ) { return 0 ; } 
			if ( mat[i+k][l+j] == state ) { return 0 ; } 
			state = 1 - state ; 
		}
	}

	state = 1-mat[i][j] ;
	for ( int k = 0 ; k < s ; k ++ ) {
		if ( mat[i+k][j] == -1 ) { return 0 ; } 
		if ( state == mat[i+k][j] ) { return 0 ; } 
		state = 1 - state ; 
	}
	return 1 ;
}

void makeInvalid ( int i , int j , int s ) {
	for ( int k = 0 ; k < s ; k ++ ) {
		for ( int l = 0 ; l < s ; l ++ ) {
			mat[i+k][l+j] = -1 ;
		}
	}
	return ;
}



int main(){
	int tc;
	char str[2000];
	int a , t;
	int diffSize[2000];
	int maxSize;


	scanf("%d",&tc);
	for(int p=1; p<=tc ; p++)
	{ 
		scanf("%d%d",&M,&N);
		for(int i=0 ; i<M ; i++)
		{
			t=0;
			scanf("%s",str);
			int k=0;
			while(str[k] != '\0')
			{
				if(str[k] == 'A')
					a=10;
				else if(str[k] =='B')
					a=11;
				else if(str[k] == 'C')
					a=12;
				else if(str[k]=='D')
					a=13;
				else if(str[k] =='E')
					a=14;
				else if(str[k] =='F')
					a=15;
				else
					a=str[k]-48;
				for(int j = t*4+3; j>=t*4 ; j--)
				{
					mat[i][j]=a%2;
					a=a/2;
				}
				t++;
				k++;
			}
		}  

		
		

		int maxSize = M > N ? N : M ; 

		for (int i = 1 ; i <= maxSize ; i ++ ) {
			diffSize[i] = 0 ;
		}
		
		for ( int s = maxSize ; s > 0 ; s -- ) {
			for (int  i = 0 ; i <= M-s ; i ++ ) {
				for (int  j = 0 ; j <= N-s ; j ++ ) {
					if ( isSquare(i,j,s) == 1 ) {
						diffSize [s] ++ ; 
						makeInvalid(i,j,s) ; 
					}
				}
			}
		}

		int result = 0 ;
		for ( int i = maxSize ; i > 0 ; i -- ) {
			if ( diffSize[i] != 0 ) { result ++ ; } 
		}
		
		printf("Case #%d: %d\n",p, result ) ;
		for (int  i = maxSize ; i > 0 ; i -- ) {
			if ( diffSize[i] != 0 ) {
				printf("%d %d\n",i,diffSize[i] ) ;
			}
		}



	}	






	
	return 0;
}


