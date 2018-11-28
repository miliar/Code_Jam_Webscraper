#include <stdio.h>
#include <string.h>
#define INPUT "date.in"
#define OUTPUT "date.out"
#define SMAX 128
#define LMAX 128

char cuv[SMAX][LMAX], curent[SMAX];

int fol[SMAX];

int T, S, Q;

int cmp(char *A, char *B)
{
	int i;
	for(i = 0; A[i] != '\n' && B[i] != '\n'; ++i)
		if(A[i] != B[i]) return 0;
	
	if(A[i] == '\n' && B[i] == '\n') return 1;
	if(A[i] == '\n' && B[i] != NULL) return 0;
	if(B[i] == '\n' && A[i] != NULL) return 0;
	
	return 1;
}
int poz(char* A)
{
	int i;
	for(i = 1; i <= S; ++i)
		if(cmp(cuv[i], curent)) return i;
	return 0;
}

int main()
{
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	
	scanf("%d\n", &T);
	
	int j;
	for(j = 1; j <= T; ++j)
	{
		scanf("%d\n", &S);
		
		int i;
		for(i = 1; i <= S; ++i)
			fgets(cuv[i], LMAX, stdin);
		
		scanf("%d\n", &Q);
		int sw = 0;
		
		int nr = 0;
		memset(fol, 0, sizeof(fol));
		for(i = 1; i <= Q; ++i)
		{
			fgets(curent, LMAX, stdin);
			
			int len = strlen(curent);
					
			int ind = poz(curent);	
			if(ind && !fol[ind]) fol[ind] = 1, ++nr;
			if(nr == S)
			{
				++sw;
				memset(fol, 0, sizeof(fol));
				nr = 1;
				fol[ind] = 1;
			}
		}
		
		printf("Case #%d: %d\n", j, sw);
	}
	return 0;
}
