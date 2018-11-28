#include<stdio.h>
int main()
{
	int t,i,j,k,w;
	char a[5][5],junk;
	freopen("test1.in","r",stdin);
	freopen("test_out.txt","w",stdout);
	
	scanf("%d",&t);
		scanf("%c",&junk);

	//scanf("%d",&a);
	//printf("%d",a);
	for(i=0;i<t;i++)
	{
		w=0;
		for(j=1;j<5;j++)
		{
			for(k=1;k<5;k++)
				{
					scanf("%c",&a[j][k]);
				}
			
			scanf("%c",&junk);		
		}
		
		
		scanf("%c",&junk);
		/*for(j=1;j<5;j++)
		{
			for(k=1;k<5;k++)
					printf("%c",a[j][k]);
			printf("\n");		
		}
		printf("\n");*/
		
		k=1;
		for(j=1;j<5;j++)
		{
			if(a[j][k]=='X'&&a[j][k+1]	=='X'&&a[j][k+2]=='X'&&a[j][k+3]=='X')
			{
				w=1;
				break;
			}
			else if(a[j][k]=='O'&&a[j][k+1]=='O'&&a[j][k+2]=='O'&&a[j][k+3]=='O')
			{
				w=2;
				break;
			}
			else if(a[j][k]=='T'&&a[j][k+1]=='X'&&a[j][k+2]=='X'&&a[j][k+3]=='X')
			{
				w=1;
				break;
			}
			else if(a[j][k]=='X'&&a[j][k+1]=='T'&&a[j][k+2]=='X'&&a[j][k+3]=='X')
			{
				w=1;
				break;
			}
			else if(a[j][k]=='X'&&a[j][k+1]=='X'&&a[j][k+2]=='T'&&a[j][k+3]=='X')
			{
				w=1;
				break;
			}
			else if(a[j][k]=='X'&&a[j][k+1]=='X'&&a[j][k+2]=='X'&&a[j][k+3]=='T')
			{//printf("5");
				w=1;
				break;
			}
			
			
			else if(a[j][k]=='T'&&a[j][k+1]=='O'&&a[j][k+2]=='O'&&a[j][k+3]=='O')
			{
				w=2;
				break;
			}
			else if(a[j][k]=='O'&&a[j][k+1]=='T'&&a[j][k+2]=='O'&&a[j][k+3]=='O')
			{
				w=2;
				break;
			}
			else if(a[j][k]=='O'&&a[j][k+1]=='O'&&a[j][k+2]=='T'&&a[j][k+3]=='O')
			{
				w=2;
				break;
			}
			else if(a[j][k]=='O'&&a[j][k+1]=='O'&&a[j][k+2]=='O'&&a[j][k+3]=='T')
			{
				w=2;
				break;
			}
				
			//scanf("%c",&junk);		
		}
		
		if(w==0)
		{
			j=1;
		for(k=1;k<5;k++)
		{
			if(a[j][k]=='X'&&a[j+1][k]	=='X'&&a[j+2][k]=='X'&&a[j+3][k]=='X')
			{
				w=1;
				break;
			}
			else if(a[j][k]=='O'&&a[j+1][k]=='O'&&a[j+2][k]=='O'&&a[j+3][k]=='O')
			{
				w=2;
				break;
			}
			else if(a[j][k]=='T'&&a[j+1][k]=='X'&&a[j+2][k]=='X'&&a[j+3][k]=='X')
			{
				w=1;
				break;
			}
			else if(a[j][k]=='X'&&a[j+1][k]=='T'&&a[j+2][k]=='X'&&a[j+3][k]=='X')
			{
				w=1;
				break;
			}
			else if(a[j][k]=='X'&&a[j+1][k]=='X'&&a[j+2][k]=='T'&&a[j+3][k]=='X')
			{
				w=1;
				break;
			}
			else if(a[j][k]=='X'&&a[j+1][k]=='X'&&a[j+2][k]=='X'&&a[j+3][k]=='T')
			{//printf("5");
				w=1;
				break;
			}
			
			
			else if(a[j][k]=='T'&&a[j+1][k]=='O'&&a[j+2][k]=='O'&&a[j+3][k]=='O')
			{
				w=2;
				break;
			}
			else if(a[j][k]=='O'&&a[j+1][k]=='T'&&a[j+2][k]=='O'&&a[j+3][k]=='O')
			{
				w=2;
				break;
			}
			else if(a[j][k]=='O'&&a[j+1][k]=='O'&&a[j+2][k]=='T'&&a[j+3][k]=='O')
			{
				w=2;
				break;
			}
			else if(a[j][k]=='O'&&a[j+1][k]=='O'&&a[j+2][k]=='O'&&a[j+3][k]=='T')
			{
				w=2;
				break;
			}
				
			//scanf("%c",&junk);		
		}
		}
		j=1;
		k=1;
		if(w==0)
		{
			if(a[j][k]=='X'&&a[j+1][k+1]=='X'&&a[j+2][k+2]=='X'&&a[j+3][k+3]=='X')
			{
				w=1;
				//break;
			}
			else if(a[j][k]=='O'&&a[j+1][k+1]=='O'&&a[j+2][k+2]=='O'&&a[j+3][k+3]=='O')
			{
			//	printf("6");
				w=2;
				//break;
			}
			else if(a[j][k]=='T'&&a[j+1][k+1]=='X'&&a[j+2][k+2]=='X'&&a[j+3][k+3]=='X')
			{
				w=1;
				//break;
			}
			else if(a[j][k]=='X'&&a[j+1][k+1]=='T'&&a[j+2][k+2]=='X'&&a[j+3][k+3]=='X')
			{
				w=1;
				//break;
			}
			else if(a[j][k]=='X'&&a[j+1][k+1]=='X'&&a[j+2][k+2]=='T'&&a[j+3][k+3]=='X')
			{
				w=1;
				//break;
			}
			else if(a[j][k]=='X'&&a[j+1][k+1]=='X'&&a[j+2][k+2]=='X'&&a[j+3][k+3]=='T')
			{//printf("5");
				w=1;
				//break;
			}
			
			
			else if(a[j][k]=='T'&&a[j+1][k+1]=='O'&&a[j+2][k+2]=='O'&&a[j+3][k+3]=='O')
			{
				w=2;
				//break;
			}
			else if(a[j][k]=='O'&&a[j+1][k+1]=='T'&&a[j+2][k+2]=='O'&&a[j+3][k+3]=='O')
			{
				w=2;
				//break;
			}
			else if(a[j][k]=='O'&&a[j+1][k+1]=='O'&&a[j+2][k+2]=='T'&&a[j+3][k+3]=='O')
			{
				w=2;
				//break;
			}
			else if(a[j][k]=='O'&&a[j+1][k+1]=='O'&&a[j+2][k+2]=='O'&&a[j+3][k+3]=='T')
			{
				w=2;
				//break;
			}
			}
			j=1;
			k=4;
			if(w==0)
			{
			 if(a[j][k]=='X'&&a[j+1][k-1]=='X'&&a[j+2][k-2]=='X'&&a[j+3][k-3]=='X')
				{
					w=1;
					//break;
				}
				else if(a[j][k]=='O'&&a[j+1][k-1]=='O'&&a[j+2][k-2]=='O'&&a[j+3][k-3]=='O')
				{
			//		printf("6");
					w=2;
					//break;
				}
				else if(a[j][k]=='T'&&a[j+1][k-1]=='X'&&a[j+2][k-2]=='X'&&a[j+3][k-3]=='X')
				{
					w=1;
					//break;
				}
				else if(a[j][k]=='X'&&a[j+1][k-1]=='T'&&a[j+2][k-2]=='X'&&a[j+3][k-3]=='X')
				{
					w=1;
					//break;
				}
				else if(a[j][k]=='X'&&a[j+1][k-1]=='X'&&a[j+2][k-2]=='T'&&a[j+3][k-3]=='X')
				{
					w=1;
					//break;
				}
				else if(a[j][k]=='X'&&a[j+1][k-1]=='X'&&a[j+2][k-2]=='X'&&a[j+3][k-3]=='T')
				{//printf("5");
					w=1;
					//break;
				}
				
				
				else if(a[j][k]=='T'&&a[j+1][k-1]=='O'&&a[j+2][k-2]=='O'&&a[j+3][k-3]=='O')
				{
					w=2;
					//break;
				}
				else if(a[j][k]=='O'&&a[j+1][k-1]=='T'&&a[j+2][k-2]=='O'&&a[j+3][k-3]=='O')
				{
					w=2;
					//break;
				}
				else if(a[j][k]=='O'&&a[j+1][k-1]=='O'&&a[j+2][k-2]=='T'&&a[j+3][k-3]=='O')
				{
					w=2;
					//break;
				}
				else if(a[j][k]=='O'&&a[j+1][k-1]=='O'&&a[j+2][k-2]=='O'&&a[j+3][k-3]=='T')
				{
					w=2;
					//break;
				}
				
				
			}
		if(w==0)
		{
			for(j=1;j<5;j++)
			{
				for(k=1;k<5;k++)
				{
					if(a[j][k]=='.')
						w=4;		
				}
			}
		}
		printf("Case #%d: ",i+1);
		if(w==0)
				printf("Draw\n");
		else if(w==1)
				printf("X won\n");
		
		else if(w==2)
				printf("O won\n");
		
		else if(w==4)
				printf("Game has not completed\n");						
		//printf("%d\n",w);
	}
	
	return 0;
}
