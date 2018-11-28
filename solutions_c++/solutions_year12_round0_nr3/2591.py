#include<stdio.h>
#include<math.h>
#include<conio.h>
int main()
{
    long int a,b ;
	int Ar[9],i,t,x,c,y,j,temp[9],k,l,m,count=0,cases=0;
	scanf("%d",&t);
	while(t--)
	{
		count=0;
		scanf("%d%d",&a,&b);
		c=1;
		x=a;
		cases++;
		while(x/10!=0)
		{x=x/10;
			c++;

		}
		l=pow(10,c-1);
		for(i=a;i<=b;i++)
		{
				x=i;
				for(j=c-1;j>=0;j--)
				{
					Ar[j]=x%10;
					x/=10;

				}
				for(k=0;k<c-1;k++)
				{
					m=l;
					temp[k]=0;
					for(j=k+1;j<c;j++)
					{
						temp[k]+=(Ar[j]*m);
						m=m/10;
					}

					for(j=0;j<k+1;j++)
					{
						temp[k]+=(Ar[j]*m);
						m=m/10;
					}


				}
				for(k=0;k<c-1;k++)
				{
					for(j=k+1;j<c-1;j++)
					{
						if(temp[j]==temp[k])
						temp[j]=0;
					}
					if(temp[k]>i&&temp[k]<=b)
					count++;
				}

		}
		printf("\nCase #%d: %d",cases,count);
	}
	getch();
	return(0);
}
