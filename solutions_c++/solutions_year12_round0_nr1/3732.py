#include <stdio.h>
#define NMAX 205
#define LMAX 27
char A[NMAX],B[NMAX],code[LMAX];
int n,m,marc[LMAX];
inline int lit(char x)
{
	return x>='a' && x<='z';
}
int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d\n",&n);
	int i,j;
	code[1]=25; code[15]=5; code[26]=17;
	for (i=1; i<=n; i++)
	{
		fgets(A+1,NMAX,stdin);
		m=0;
		while (lit(A[m+1]))
		{
			while (lit(A[m+1])) m++;
			m++;
		}
		m--;
		fgets(B+1,NMAX,stdin);
		for (j=1; j<=m; j++)
			if (A[j]!=' ')
				code[A[j]-'a'+1]=B[j]-'a'+1,marc[B[j]-'a'+1]=1;
	}
	//17 is the winner of googliada
	for (i=1; i<=26; i++)
		if (!marc[i])
			code[17]=i;
	scanf("%d\n",&n);
	for (i=1; i<=n; i++)
	{
		fgets(A+1,NMAX,stdin);
		m=0;
		while (lit(A[m+1]))
		{
			while (lit(A[m+1])) m++;
			m++;
		}
		m--;
		printf("Case #%d: ",i);
		for (j=1; j<=m; j++)
			if (A[j]==' ')
				printf("%c",A[j]);
			else
				printf("%c",'a'+code[A[j]-'a'+1]-1);
		printf("\n");
	}
	return 0;
}
