#include<stdio.h>
FILE *in,*out;
char a[40][100];
int main()
{
	int t,i,j;
	out=fopen("output.out","w");
	scanf("%d",&t);
	for(i=0;i<=t;i++)
	{
		gets(a[i]);
	}
	for(i=0;i<=t;i++)
	{
		j=0;
		while(a[i][j]!=0)
		{
			if(a[i][j]=='a')
			{
				a[i][j]='y';
			}
			else if(a[i][j]=='b')
			{a[i][j]='h';
			}
			else if(a[i][j]=='c')
			{a[i][j]='e';
			}
			else if(a[i][j]=='d')
			{a[i][j]='s';
			}
			else if(a[i][j]=='e')
			{a[i][j]='o';
			}
			else if(a[i][j]=='f')
			{a[i][j]='c';
			}
			else if(a[i][j]=='g')
			{a[i][j]='v';
			}
			else if(a[i][j]=='h')
			{a[i][j]='x';
			}
			else if(a[i][j]=='i')
			{a[i][j]='d';
			}
			else if(a[i][j]=='j')
			{a[i][j]='u';
			}
			else if(a[i][j]=='k')
			{a[i][j]='i';
			}
			else if(a[i][j]=='l')
			{a[i][j]='g';
			}
			else if(a[i][j]=='m')
			{a[i][j]='l';
			}
			else if(a[i][j]=='n')
			{a[i][j]='b';
			}
			else if(a[i][j]=='o')
			{a[i][j]='k';
			}
			else if(a[i][j]=='p')
			{a[i][j]='r';
			}
			else if(a[i][j]=='q')
			{a[i][j]='z';
			}
			else if(a[i][j]=='r')
			{a[i][j]='t';
			}
			else if(a[i][j]=='s')
			{a[i][j]='n';
			}
			else if(a[i][j]=='t')
			{a[i][j]='w';
			}
			else if(a[i][j]=='u')
			{a[i][j]='j';
			}
			else if(a[i][j]=='v')
			{a[i][j]='p';
			}
			else if(a[i][j]=='w')
			{a[i][j]='f';
			}
			else if(a[i][j]=='x')
			{a[i][j]='m';
			}
			else if(a[i][j]=='y')
			{a[i][j]='a';
			}
			else if(a[i][j]=='z')
			{a[i][j]='q';
			}
			j++;
		}
	}
	for(i=1;i<=t;i++)
	{
		j=0;
		fprintf(out,"Case #%d: ",i);
		printf("\nCase #%d: ",i);
		while(a[i][j]!=0)
		{
			fprintf(out,"%c",a[i][j]);
			printf("%c",a[i][j]);
			j++;
		}
		fprintf(out,"\n",0);
		printf("\n");
	}
	return 0;
}