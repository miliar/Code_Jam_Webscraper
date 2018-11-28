#include<stdio.h>
#include<cstring>

FILE*f=fopen("dancing.in","r");
FILE*g=fopen("dancing.out","w");

int n,s,p,score[105];
int surpriza[2][35][35],surp[2][35],D[105][105];

inline int max ( const int &a , const int &b ){
	return a >= b ? a : b;
}

int main () {
	//surpriza[2][i][j] = face surpriza sau nesurpriza cu suma i incat best score >= j
	
	for ( int sum = 0 ; sum <= 30 ; ++sum ){
		
		for ( int a = 0 ; a <= sum ; ++a ){
			for ( int b = a ; a + b <= sum && b - a < 3 ; ++b ){
				int c = sum - a - b;
				if ( c < b )	continue ;
				if ( c - a >= 3 )	continue ;
				int now = c - a; if ( now > 0 )	--now;
				
				surp[now][sum] = 1;
				for ( int index = c ; index >= 0 ; --index ){
					surpriza[now][sum][index] = 1;
				}
			}
		}
		
	}
	
	int t;
	fscanf(f,"%d",&t);
	
	for ( int ii = 1 ; ii <= t ; ++ii ){
		fscanf(f,"%d %d %d",&n,&s,&p);
		for ( int i = 1 ; i <= n ; ++i ){
			fscanf(f,"%d",&score[i]);
		}
		
		for ( int i = 0 ; i <= n ; ++i ){
			for ( int j = 0 ; j <= s ; ++j ){
				D[i][j] = -(1<<29);
			}
		}
		D[0][0] = 0;
		
		for ( int i = 1 ; i <= n ; ++i ){
			if ( surpriza[0][score[i]][p] ){
				if ( D[i-1][0] >= 0 )
					D[i][0] = D[i-1][0] + 1;
			}
			else{
				if ( surp[0][score[i]] ){
					D[i][0] = D[i-1][0];
				}
			}
			for ( int j = 1 ; j <= s ; ++j ){
				//D[i][j] = numarul maxim dintre primii i cu scor >= p a.i sunt exact j surprize
				if ( surpriza[0][score[i]][p] ){
					D[i][j] = D[i-1][j]+1;
				}
				else{
					if ( surp[0][score[i]] ){
						D[i][j] = D[i-1][j];
					}
				}
				if ( surpriza[1][score[i]][p] ){
					D[i][j] = max(D[i][j],D[i-1][j-1]+1);
				}
				else{
					if ( surp[1][score[i]] ){
						D[i][j] = max(D[i][j],D[i-1][j-1]);
					}
				}
			}
		}
		
		fprintf(g,"Case #%d: %d\n",ii,D[n][s]);
	}
	
	fclose(f);
	fclose(g);
	
	return 0;
}
