# include<stdio.h>
# include<stdlib.h>
# include<string.h>

FILE *input,*output;

void print(char a[4][5])
{
	for(int i=0;i<4;i++)
		printf("%s\n",a[i]);
}
int check(int*a)
{
	for(int i=0;i<10;i++)
	{
		if(a[i]==4)
		return 1;
	}
	return 0;
}
int main()
{
	char matrix[4][5];
	int a[10],sum=0,flag,j;
	int b[10];


	int N,C,L,i,t;
	 input  = fopen("F:\Tic.in","r");
	 output = fopen("F:\output.txt","w");
	fscanf(input,"%d",&N);
	
	for(t=1;t<=N;t++)
	{
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		flag = 0;
		sum=0;
		fprintf(output,"Case #%d: ",t);
		for(i=0;i<4;i++)
		{
			fscanf(input,"%s",matrix[i]);
			
		}
		
	
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(matrix[i][j] =='X')
				{
					sum++;
					a[i]++;
					a[4+j]++;
					if(i==j)
						a[8]++;
					if(i==3-j)
						a[9]++;
						
					
				}
				else if(matrix[i][j] =='O')
				{
				
					sum++;
					b[i]++;
					b[j+4]++;
					if(i==j)
						b[8]++;
					if(i==3-j)
						b[9]++;
						
					
				}
				else if(matrix[i][j] =='T')
				{
					sum++;
					a[i]++;
					a[j+4]++;
					if(i==j)
						a[8]++;
					if(i==3-j)
						a[9]++;
					
					b[i]++;
					b[4+j]++;
					if(i==j)
						b[8]++;
					if(i==3-j)
						b[9]++;
					
					
					
				}
				
				  
					
						
			}
			
			
		}
		
	/*	for(int k=0;k<10;k++)
			printf("%d ",a[k]);
			printf("\n");
		for(int k=0;k<10;k++)
			printf("%d ",b[k]);
			printf("\n");*/
		if(check(a))
			{
				char *str = "X won\n";
				fprintf(output,"%s",str);
				flag=1;
				
					
			}
		if(check(b))
			{
				char *str = "O won\n";
				fprintf(output,"%s",str);
				flag=1;
				
			}
		
		if(!flag)
		{
			if(sum == 16)
				
				{
					char *str = "Draw\n";
					fprintf(output,"%s",str);
				}
			else
			
				{
					char *str = "Game has not completed\n";
					fprintf(output,"%s",str);
				}
			
				
		}
		
		
		/*fscanf(input,"%d",&L);
		
		for(i=0;i<L;i++)
		{
			fscanf(input,"%d",&(a[i].value));
			a[i].position = i+1;

			
		}
		
		qsort(a,L,sizeof(key),compare);
		
		findSolution(a,L,C);
		*/
	
	
	}
return 0;	
}
