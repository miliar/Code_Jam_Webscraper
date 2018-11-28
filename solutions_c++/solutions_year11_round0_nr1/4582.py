#include<stdio.h>

int absoluto (int a)
{
	if(a<0)
		return (a*-1);
	return a;
}

int main()
{
	int i,j,n,n1,nc,O,B,seg,ant,k,aux;
	char color,antcol;
	
	scanf("%d",&n);	
	for(k=1;k<=n;k++)
	{
		scanf("%d ",&n1);
		O=B=1;	
		j=seg=0;
		ant=0;


		for(j=1;j<=n1;j++)
		{
			scanf("%c %d ",&color,&nc);
			if(j==1)
			antcol=color;
	
			if(color=='O')
			{
				i=absoluto(nc-O)+1;	
				O=nc;

				if(color!=antcol)
				{
					if(ant<i)
					{
						seg += i-ant;
						aux=i-ant;
						ant=aux;
					}
					else
					{	
						seg++;
						ant=1;
					}
				}
				else
				{
					ant += i;
					seg += i;	
				}
				
			}
			if(color=='B')
			{
				i=absoluto(nc-B)+1;
				//printf("%d %d %d %d  	",nc,B,O,ant);				
				B=nc;
				
				if(color!=antcol)
				{
					if(ant<i)
					{
						seg += i-ant;
						aux=i-ant;
						ant=aux;
					}
					else
					{	
						seg++;
						ant=1;
					}
				}
				else
				{
					ant += i;
					seg += i;	
				}
				
			}
			antcol=color;
			
		}
		printf("Case #%d: %d\n",k,seg);
	}
	return 0;
}
