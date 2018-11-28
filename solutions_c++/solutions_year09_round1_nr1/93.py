#include <stdio.h>
#include <math.h>
bool isgood[2000][12];
bool occ[2000];
int bases[1000];
bool findit(int i,int B)
{
	if(i<=1500)
	{
		if(occ[i])
			return 0;
		occ[i]=1;
	}
	int tmp=i;
	int sqs=0;
	while(tmp)
	{
		sqs+=(tmp%B)*(tmp%B);
		tmp/=B;
	}
	if(sqs==1)
		return 1;
	else
		return findit(sqs,B);
	
}

int main()
{
	
	for(int B=2;B<=10;B++)
	{
		isgood[1][B]=1;
		for(int i=2;i<=1500;i++)
		{
			for(int j=0;j<=1500;j++)
			{
				occ[j]=0;
			}
			
			isgood[i][B]=findit(i,B);
		}
	}
	
	
	
	
	//printf("%d %d\n",isgood[3][2],isgood[3][3]);
	
	
	
	int tc;
	scanf("%d",&tc);
	char line[100000];
	gets(line);

	for(int t=1;t<=tc;t++)
	{
		gets(line);
		int i=0;
		int ct=0;
		int number=0;
		while(line[i]!='\0')
		{
			if(line[i]==' ')
			{
				bases[ct++]=number;
				number=0;
			}
			else
				number=number*10+line[i]-'0';
			i++;
		}
		bases[ct++]=number;
		
		
		
		int j=2;
		while(1)
		{
			bool good=1;
			for(int i=0;i<ct;i++)
			{
				int sq=0;
				int tmp=j;
				while(tmp)
				{
					sq+=(tmp%bases[i])*(tmp%bases[i]);
					tmp/=bases[i];
				}
				//printf("%d %d %d\n",j,bases[i],sq);
				if(!isgood[sq][bases[i]])
				{
					good=0;
					break;
				}
			}
			if(good)
			{
				printf("Case #%d: %d\n",t,j);
				break;
			}
			j++;

		}
		
		

	}
	
	
	
}

