#include<stdio.h>
#include<string.h>
#define N 110
#define H 10010

int n;
int l, c;
int mat[N][N];
int visita[N][N];
char letras[N][N];
char letra = 'a';

char dfs ( int lin, int col)
{
	//printf("<%d %d>",lin,col);
	visita[lin][col] = 1;

	int norte = mat[lin-1][col], oeste = mat[lin][col-1];
	int leste = mat[lin][col+1], sul = mat[lin+1][col];
	
	//printf("<lin,col> = <%d,%d>\nnorte = %d, oeste =%d, leste = %d, sul = %d\n",lin,col,norte,oeste,leste,sul); 
	
	int bool_n = norte <= oeste && norte <= leste && norte <= sul && norte < mat[lin][col];
	int bool_o = oeste < norte && oeste <= leste && oeste <= sul && oeste < mat[lin][col] ;
	int bool_l = leste < norte && leste < oeste && leste <= sul && leste < mat[lin][col] ;
	int bool_s = sul < norte && sul < oeste && sul < leste && sul < mat[lin][col];
	

	if ( bool_n )
	{

		if ( visita[lin-1][col]	== 1 ) 	letras[lin][col] = letras[lin-1][col];
		else {  letras[lin][col] = dfs (lin-1, col);  }
		return letras[lin][col];
	}
				
	
	if ( bool_o  )
	{

		if ( visita[lin][col-1]	== 1 ) 	letras[lin][col] = letras[lin][col-1];
		else {  letras[lin][col] = dfs (lin, col-1); }
		return letras[lin][col];
	}
		
	if ( bool_l  )
	{

		if ( visita[lin][col+1]	== 1 ) 	letras[lin][col] = letras[lin][col+1];
		else {  letras[lin][col] = dfs (lin, col+1);  }
		return letras[lin][col];
	}
	
	if ( bool_s ) 
	{

		if ( visita[lin+1][col]	== 1 ) 	letras[lin][col] = letras[lin+1][col];
		else {  letras[lin][col] = dfs ( lin+1,col);  }
		return letras[lin][col];
		
	}

	/*if ( ! (bool_n || bool_o || bool_l || bool_s ) )
		{ 
			letras[lin][col] = letra;
			printf("<%d,%d> eh sink = '%c'\n",lin,col,letra); 
			//letra++;
			
		}*/
	

	
	letras[lin][col] = letra;
	//printf("<%d,%d> eh sink = '%c'\n",lin,col,letra);
	letra+=1;	
	return letras[lin][col];

}

int main (void)
{
	scanf("%d",&n);
	int lin, col;
	//int contador = 0;
	
	for ( int caso = 1; caso <= n; caso++) {
		scanf("%d %d",&l, &c);
		//printf("matriz %d x %d\n",l,c);
		letra = 'a';
		
		printf("Case #%d:\n",caso);

		for ( lin= 0; lin < N; lin++ )
			for ( col = 0; col < N; col++ )
				mat[lin][col] = H;

		for ( lin= 0; lin < N; lin++ )
			for ( col = 0; col < N; col++ )
				visita[lin][col] = 0;

		for ( lin= 1; lin <= l; lin++ )
			for ( col = 1; col <= c; col++ ) {
				scanf("%d",&mat[lin][col]);
				letras[lin][col] = 'D';
			}

		/*for ( int correL = 1; correL <= l; correL++ )
			for ( int correC = 1; correC <= c; correC++ ) {
				vizinhos[correL+1][correC]) = 1;
				vizinhos[correL-1][correC]) = 1;
				vizinhos[correL1][correC+1]) = 1;
				vizinhos[correL1][correC-1]) = 1;
				vizinhos[correL1][correC]) = 0;
			}*/	

		/*for ( int correL = 1; correL <= l; correL++ )
			for ( int correC = 1; correC <= c; correC++ ) {
				if (correC == 1) printf("\n");
				printf("%d ",mat[correL][correC]);
			}*/

		for ( lin = 1; lin <= l; lin++ )
			for ( col = 1; col <= c; col++ ) {

				if (visita[lin][col] == 0) {
					char teste = dfs(lin,col);

				}
			}	
		
		for ( lin = 1; lin <= l; lin++ ) {
			printf("%c",letras[lin][1]);
			for ( col = 2; col <= c; col++ ) {
				//printf("%d",contador++);
				
				printf(" %c",letras[lin][col]);
			}
			printf("\n");
		}
		

	}

	return 0;
}
