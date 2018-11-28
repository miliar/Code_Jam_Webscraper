#include <stdio.h>
int Abs(int a)
{
	return a>0?a:-a;
}
int main()
{
	int i,repeat,n,o,b,to,tb,pos,ri=1,ct;
	char color;
	freopen("1.out","w",stdout);
	
	scanf("%d",&repeat);
	while(repeat--)
	{
		scanf("%d",&n);
		o=b=1;
		to=tb=ct=0;
		for(i=0;i<n;i++)
		{
			scanf("%1s%d",&color,&pos);
			if( color=='O' )
			{
				if( to>=Abs(pos-o) )
				{
					tb++;
					to=0;
					o=pos;
					ct++;
				}
				else
				{
					ct+=Abs(pos-o)-to+1;
					tb+=Abs(pos-o)-to+1;
					to=0;
					o=pos;
				}
			}
			else
			{
				if( tb>=Abs(pos-b) )
				{
					to++;
					tb=0;
					b=pos;
					ct++;
				}
				else
				{
					ct+=Abs(pos-b)-tb+1;
					to+=Abs(pos-b)-tb+1;
					tb=0;
					b=pos;
				}
			}
		}
		printf("Case #%d: %d\n",ri++,ct);
	}
	return 0;
}