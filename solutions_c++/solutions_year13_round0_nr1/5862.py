#include "stdio.h"
#include "stdlib.h"
#include "string.h"
int judge(char **s);
int main()
{
	FILE *input;
	FILE *output;	
	int result,k,N,M;
	char **s;
	char *str4;
	str4=(char*)malloc(5*sizeof(char));
	
	input=fopen("E:A-large.in","rw");
	output=fopen("E:A-large.out","awr");
	if(input!=NULL)
	{
		fscanf(input,"%d",&N);
		fgets(str4,5,input);
		M=N;
	while(N--)
	{

		s=(char **)malloc(4*sizeof(char *));
		for (k=0;k<4;k++)
		{
			s[k]=(char *)malloc(5*sizeof(char *));
		}
	fscanf(input,"%s",s[0]);
	fscanf(input,"%s",s[1]);
	fscanf(input,"%s",s[2]);
	fscanf(input,"%s",s[3]);
	result=judge(s);
	switch(result)
	{
	case 0:
		fprintf(output,"Case #%d: Draw\n",M-N);
		break;
	case 1:
		fprintf(output,"Case #%d: X won\n",M-N);
		break;
	case 2:
		fprintf(output,"Case #%d: O won\n",M-N);
		break;
	case 3:
		fprintf(output,"Case #%d: Game has not completed\n",M-N);
		break;
	}
	for (k=0;k<4;k++)
		free(s[k]);
	free(s);

	}
	}
	free(str4);
	return 0;
}




int judge(char **s)
{
	int i,j,nx1,no1,nx2,no2,np;
	nx1=nx2=no1=no2=np=0;
	for (i=0;i<4;i++)
	{		
		for(j=0;j<4;j++)
		{	if (s[i][j]=='.')
				np+=1;
			if (s[i][j]=='X'||s[i][j]=='T')
				nx1+=1;
			if (s[i][j]=='O'||s[i][j]=='T')
				no1+=1;
			if (s[j][i]=='X'||s[j][i]=='T')
				nx2+=1;
			if (s[j][i]=='O'||s[j][i]=='T')
				no2+=1;
		}
		if (nx1==4||nx2==4)
		{
		//	printf("X win\n");
			return 1;
		}
		if (no1==4||no2==4)
		{
		//	printf("O win\n");
			return 2;
		}
		nx1=nx2=no1=no2=0;
	}

	for (i=0;i<4;i++)
	{
		if (s[i][i]=='X'||s[i][i]=='T')
			nx1+=1;
		if (s[i][i]=='O'||s[i][i]=='T')
			no1+=1;
		if (s[i][3-i]=='X'||s[i][3-i]=='T')
			nx2+=1;
		if (s[i][3-i]=='O'||s[i][3-i]=='T')
			no2+=1;
		
	}
	if (nx1==4||nx2==4)
	{
	//	printf("X win\n");
		return 1;
	}
	if (no1==4||no2==4)
	{
	//	printf("O win\n");
		return 2;
	}
	if (np!=0&&nx1!=4&&nx2!=4&&no1!=4&&no2!=4)
	{
	//	printf("Game has not completed\n");
		return 3;
	}
	else 
	{//	printf("Draw\n");
		return 0;}


}