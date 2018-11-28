#include<stdio.h> 
int P[1005];
void prime()
{
	int i ,j;
	P[1] = 0;
	P[2] = 0;
	for(i = 2;i <= 1000; i ++)
	{
		if(!P[i])
		{
			for(j = i *i ; j < 1000 ;j +=i)
				P[j] = 1;
		}
	}
	return ;
}
int main()
{
	int c,k,i,j;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);

	scanf("%d",&c);
	prime();
	for(k = 1; k<= c; k ++)
	{
		__int64 a,b,p;
		scanf("%I64d%I64d%I64d",&a,&b,&p);
		int visit[10000] = {0};
		int len = 2,form;
		for(j = p ;j <= b;j ++)
		{
			if(!P[j])
			{
				int sign = 0,g = 0;
				for(i = a; i <= b; i++)
				{
					if(i%j == 0)
					{
						sign ++;
						if(sign == 1)
						{
							form = i;
							if(visit[i])
								g = 1;
						}
						if(sign >= 2)
						{
							if(visit[i])
								g = 1;
							visit[i] = len;
							visit[form] = len;
						}
					}
				}
				if(sign >1 && !g)
				len ++;
			}
			
		}
			__int64 count = 0;
		for(i = a;i <= b; i ++)
			if(visit[i]== 0 || visit[i] == 1 )
				count ++;
		count += (len - 2);
		printf("Case #%d: %I64d\n",k,count);

			
	}
	return 0;
}