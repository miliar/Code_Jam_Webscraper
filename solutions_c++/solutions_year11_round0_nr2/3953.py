#include<iostream>
using namespace std;
#include<stdio.h>
#include<ctype.h>
#include<string.h>
int c,d,n;

void getline(char com[][3],char opp[][2],char ip[])
{
	int k=0,i;
	scanf("%d",&c);
	//c=getchar()-'0';
	getchar();
	for(i=0;i<c;i++)
	{
		com[k][0]=getchar();
		com[k][1]=getchar();
		com[k][2]=getchar();
		k++;
		com[k][0]=com[k-1][1];
		com[k][1]=com[k-1][0];
		com[k][2]=com[k-1][2];
		k++;
		getchar();
	}
	scanf("%d",&d);
	//d=getchar()-'0';
	getchar();
	k=0;
	for(i=0;i<d;i++)
	{
		opp[k][0]=getchar();
		opp[k][1]=getchar();
		k++;
		opp[k][0]=opp[k-1][1];
		opp[k][1]=opp[k-1][0];
		k++;
		getchar();	
	}
	scanf("%d",&n);
	//n=getchar()-'0';
	getchar();
	for(i=0;i<n;i++)
		ip[i]=getchar();
	getchar();
	c*=2;
	d*=2;	
}

void print(char str[])
{
	int i=0;
	if(!strlen(str))
		printf("[]\n");
	else
	{
		printf("[%c",str[0]);
		for(i=1;i<strlen(str);i++)
			printf(", %c",str[i]);
		printf("]\n");
	}

}

main()
{
int t,i,j,k,top,cas=1;
char key,com[100][3],opp[100][2],ip[102],op[102];
scanf("%d",&t);
getchar();
while(t--)
{
top=0;
getline(com,opp,ip);
op[top]='\0';
for(i=0;i<n;i++)
{
if(top==0)
{
	op[top]=ip[i];
	op[++top]='\0';
	continue;
}
	key=ip[i];
	for(j=0;j<c;j++)
	{
		if(com[j][0]==key)
		{
			if(op[top-1]==com[j][1])
			{
				op[top-1]=com[j][2];
				goto lab;
			}
		}
	}
	for(j=0;j<d;j++)
	{
		if(opp[j][0]==key)
		{
			for(k=top-1;k>=0;k--)
			{
				if(op[k]==opp[j][1])
				{
					op[0]='\0';
					top=0;
					goto lab;
				}
			}
		}
	}

op[top]=key;
op[++top]='\0';
lab: continue;
}
printf("Case #%d: ",cas++);
print(op);
}
}
