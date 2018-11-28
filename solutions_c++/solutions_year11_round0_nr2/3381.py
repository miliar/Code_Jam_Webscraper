#include<stdio.h>
using namespace std;
char list[100];
int listind=0;

void empty()
{
	listind=0;
}

int insert(char ch)
{
	list[listind++]=ch;
}

char rmove()
{
	listind--;
	return list[listind];
}
int main()
{
	int t,ct;
	int combine,oppose,i,elem,j,cond,k;
	char com[36][3];
	char opp[28][2];
	char seq[100];
	char ch,insrq,other;
	scanf("%d",&t);
	ct=t;
	while(t--)
	{
		scanf("%d",&combine);
		//printf("comb:%d\n",combine);
		for(i=0;i<combine;i++)
		{
			scanf("%s",com[i]);
		}
		scanf("%d",&oppose);
		//printf("opps:%d\n",oppose);
		for(i=0;i<oppose;i++)
		{
			scanf("%s",opp[i]);
		}
		scanf("%d",&elem);
		scanf("%s",seq);
		//for(i=0;i<combine;i++)
		//	printf("%c+%c=%c\n",com[i][0],com[i][1],com[i][2]);
		//for(i=0;i<oppose;i++)
		//	printf("%c-%c=0\n",opp[i][0],opp[i][1]);
		//printf("%s\n",seq);
		//printf("\n");
		cond=0;
		empty();
		for(i=0;i<elem;i++)
		{
			cond=0;
			insrq=seq[i];
			if(listind>0)
			{
				ch=list[listind-1];
				for(j=0;j<combine;j++)	
				{
					if(com[j][0]==insrq && com[j][1]==ch)
					{
						rmove();
						insrq=com[j][2];
						cond=1;
						break;
					}
					else if(com[j][1]==insrq && com[j][0]==ch)
					{
						rmove();
						insrq=com[j][2];
						cond=1;
						break;
					}
				}
			}	
			if(listind>0 && cond!=1)
			{
				other='0';
				for(j=0;j<oppose;j++)
				{
					if(opp[j][0]==insrq)
						other=opp[j][1];
					else if(opp[j][1]==insrq)
						other=opp[j][0];
					if(other!='0')
					{
						for(k=0;k<listind;k++)
						{
							if(list[k]==other)
							{
								empty();
								cond=2;
								break;
							}
						}
					}
				}
			}
			if(cond!=2)		
			insert(insrq);
		}
		printf("Case #%d: [",ct-t);
		for(i=0;i<listind-1;i++)
			printf("%c, ",list[i]);
		if(listind>0)
		printf("%c]",list[listind-1]);
		else
		printf("]");
		printf("\n");
		
	}
}
