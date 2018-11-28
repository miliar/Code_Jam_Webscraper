#include<stdio.h>
#include<iostream.h>
#include<string.h>
#include<stdlib.h>


struct searchInfo
{
	char sname[150];
	int sn;
};

int scount;
int n,s,q;
struct searchInfo sinfo[100];

void set(int sflag = -1)
{
	if(sflag == -1)
	{
		for(int i=0;i<100;i++)
		{
			memset(sinfo[i].sname ,0x00,sizeof(sinfo[i].sname ));
			sinfo[i].sn = 0;
		}
	}
	else
	{
		for(int i=0;i<100;i++)
			sinfo[i].sn = 0;
	}
}
void cswitch(char *qinfo)
{
	int i,j;

	for(i=0;i<s;i++)
	{
		if(strcmp(sinfo[i].sname,qinfo) == 0)
		{
			if(sinfo[i].sn != 0)
			{
				sinfo[i].sn = sinfo[i].sn + 1;				
			}
			else
			{
				bool cflag =false;
				for(j=0;j<s;j++)
				{
					if((j!=i)&& (sinfo[j].sn == 0))
					{
						sinfo[i].sn = sinfo[i].sn + 1;
						break;
					}
				}
				if(j == s)
				{
					set(0);
					sinfo[i].sn = sinfo[i].sn + 1;
					scount++;
				}
			}
			break;
		}
	}
}
int main()
{
	int i,j,k;
	FILE *ptr = NULL;
	char qinfo[100];
	scanf("%d",&n);
	
	if((ptr=fopen("Result.txt","w+"))==NULL)
	{
		cout<<"File opening Error\n";
		return -1;
	}

	for(i=0;i<n;i++)
	{
		scanf("%d",&s);
		set();
		scount = 0;
		for(j=0;j<s;j++)
		{
			cin.getline(sinfo[j].sname ,100,'\n');	
		}
		scanf("%d",&q);
		for(k=0;k<q;k++)
		{
			memset(qinfo,0x00,sizeof(qinfo));
			cin.getline(qinfo,100,'\n');
			cswitch(qinfo);
		}
		cout<<"S count = "<<scount<<endl;
		fprintf(ptr,"Case #%d: %d\n",(i+1),scount);
	}
	fclose(ptr);
}