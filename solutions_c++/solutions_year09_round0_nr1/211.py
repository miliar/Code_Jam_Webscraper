#include "stdio.h"
#include "string.h"
char dic[5005][30];
int x[5005],y[5005],numx,numy;
int main()
{
	char ch;
	int kk,l,kase,d,i,j,k;
	scanf("%d%d%d",&l,&d,&kase);
	for(i=0;i<d;i++)
		scanf("%s",dic[i]);
	for(kk=1;kk<=kase;kk++)
	{
		ch=getchar();
		numx=d;
		for(i=0;i<numx;i++)
			x[i]=i;
		for(i=0;i<l;i++)
		{
			ch=getchar();
			if(ch=='(')
			{
				numy=0;
				while(1)
				{
					ch=getchar();
					if(ch==')')
						break;
					for(k=0;k<numx;k++)
					{
						if(dic[x[k]][i]==ch)
							y[numy++]=x[k];
					}
				}
			}
			else
			{
				numy=0;
				for(k=0;k<numx;k++)
				{
					if(dic[x[k]][i]==ch)
						y[numy++]=x[k];
				}
			}
			for(k=0;k<numy;k++)
				x[k]=y[k];
			numx=numy;
		}
		printf("Case #%d: %d\n",kk,numx);
	}
	return 0;
}