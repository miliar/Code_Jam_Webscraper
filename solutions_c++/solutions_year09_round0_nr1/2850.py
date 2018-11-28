#include<stdio.h>
char a[5005][20];
void main()
{
	int L,D,N;
	int i,j;
	
	freopen("A-large.in","r",stdin);

	freopen("A-large.out","w",stdout);

	scanf("%d%d%d",&L,&D,&N);
	getchar();
	//printf("L=%d D=%d N=%d \n",L,D,N);
	for(i=0; i<D; i++)
	{
		for(j=0; j<L; j++)
			scanf("%c",&a[i][j]);
		getchar();
	}
	
	int count;
	for(count=1; count<=N; count++)
	{
		char input[10000];
		char b[20][10000];
		
		int m=0,n=0;
		scanf("%s",input);
		
	
		
		for(j=0; j<10000 && input[j] != '\0'; j++)
		{
			if( input[j] == '(' )
			{
				j++;
				for(; j<10000 && input[j] != '\0'; j++)
				{
					
					if(input[j] == ')')
					{	b[m][n] = '\0';
					m++;
					n=0;
					break;
					}
					b[m][n++] = input[j];
					
				}
			}
			else
			{
				b[m][n] = input[j];
				b[m][++n] = '\0';
				m++;
				n=0;
				
			}	
		}
		
		
		int allnum = 0;
		for(i=0; i<D; i++)
		{
			int num = 0;
			for(j=0; j<L; j++)
			{
				for(int q=0; q<10000 && b[j][q] != '\0'; q++)
					if(a[i][j] == b[j][q])
					{
						num++;
						break;
					}

			}
			if(num == L)
			{
				allnum++;
			}
		}
		printf("Case #%d: %d\n",count,allnum);
		
		
	}
	
	
}


/*		for(int k=0; k<m; k++)
		{
				printf("%s",b[k]);	
		//	for(int q=0; q<10000 && b[k][q] != '\0'; q++)
		//		printf("%c",b[k][q]);
			printf("\n");
		}
		
*/	

/*	
	for(i=0; i<D; i++)
	{
		for(j=0; j<L; j++)
			printf("%c",a[i][j]);
		printf("\n");
		//getchar();
	}
*/