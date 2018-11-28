#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int O[501][21];
char input[501];
char stri[] = "welcome to code jam";
int N;
int main()
{
	//FILE *f;
	//f=fopen("c:\\input.txt","r");
	//fscanf(f,"%d",&N);
	scanf("%d",&N);
	for(int m=1;m<=N;m++)
	{
		memset(O,0,501*21);
		//fgets(input,500,f);
		fflush(stdin);
		gets(input);

		for(int i=1;i<=strlen(input);i++) {
			if(input[i-1]==stri[0])
				O[i][1]=O[i-1][1]+1;
			else
				O[i][1]=O[i-1][1];
		}
		for(int i=1;i<=strlen(input);i++) {
			for(int j=2;j<=strlen(stri);j++) {
				O[i][j]=O[i-1][j];
				if(input[i-1] == stri[j-1])
					O[i][j]+=O[i-1][j-1];
				if(O[i][j]>=10000)
					O[i][j]-=10000;
			}
		}
//		for(int i=1;i<=strlen(input);i++) {
//			for(int j=1;j<=strlen(stri);j++) {
//				printf("%d ",O[i][j]);
//			}
//			printf("\n");
//		}
		printf("Case #%d: %04d\n",m,O[strlen(input)][strlen(stri)]);
	}
	//fclose(f);
}