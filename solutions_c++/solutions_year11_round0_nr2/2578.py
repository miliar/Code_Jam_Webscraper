#include<cstdio>
using namespace std;
char comb1[75],comb2[75],rep[75],opp1[75],opp2[75];
int c,d,n,current;
char ele[120];
void function(char ch)
{
	char tester;
	int i,j,exit,notoccur;
	notoccur=exit=0;
	if(current==0)
	{
		current++;
		ele[current]=ch;
		//printf("1.%c \n",ele[current]);
	}
	else
	{
		tester=ele[current];
		for(i=1;i<=2*c;i++)
		{
			if(comb1[i]==ch && comb2[i]==tester)
			{
			ele[current]=rep[i];
			notoccur=1;
			//printf("2.%c \n",ele[current]);
			break;
			}
		}
		if(notoccur==0)
		{
		for(i=1;i<=current;i++)
		{
			for(j=1;j<=2*d;j++)
			{
				if(opp1[j]==ele[i]&&opp2[j]==ch)
				{
					current=0;
					exit=1;
					break;
				}
			}
		if(exit==1)
			break;
		}
		if(exit==0)
		{
			current++;
			ele[current]=ch;
			//printf("3.%c \n",ele[current]);
		}
		}

	}
	
}
int main()
{
	int num_cases,temp,i,j,k,l;
	char ch,n1,n2,n3;
	scanf("%d",&num_cases);
	for(i=1;i<=num_cases;i++)
	{
		current=0;
		scanf("\n%d",&c);
		temp=1;
		for(j=1;j<=c;j++)
		{
			scanf(" %c%c%c",&n1,&n2,&n3);
			comb1[temp]=comb2[temp+1]=n1;
			comb2[temp]=comb1[temp+1]=n2;
			rep[temp]=rep[temp+1]=n3;
			temp=temp+2;
				
		}
		scanf(" %d",&d);
		temp=1;
		for(k=1;k<=d;k++)
		{
			scanf(" %c%c",&n1,&n2);
			opp1[temp]=opp2[temp+1]=n1;
			opp2[temp]=opp1[temp+1]=n2;
			temp=temp+2;		
		}
		scanf(" %d ",&n);
		
		for(l=1;l<=n;l++)
		{
		//	printf("jj");
			scanf("%c",&ch);
			function(ch);
		}
		printf("\nCase #%d: [",i);
		for(l=1;l<=current;l++)
			{
			if(l==current)
			printf("%c]",ele[l]);			
			else
			printf("%c, ",ele[l]);
			}
		if(current==0)
			printf("]");
	}
	return 0;
}
