#include <stdio.h>
#include <conio.h>
#include <math.h>
#include <string.h>
int in(char totest,char* stri)
{
	int i=0;
	int res=0;
	for (i=0;i<strlen(stri);i++) if(totest==stri[i])res=1;
	return res;
}


int main()
{
	int res1=0;
	int left=0;int right=0;
	int ii=0;
	int testres=0;
	int len=0;
	int linenum=0;
	int testcases=0;
	int alienlen=0;
	int current=0;
	int counter=0;
	long long res=0;
	char userdict[5008][200];
	char knownwords[5002][17];
	char alien[50002]="";
	int i=0;int j=0;int k=0;
	scanf("%d",&len);
	scanf("%d",&linenum);
	scanf("%d",&testcases);
	gets(userdict[5007]);
	for (i=0;i<linenum;i++) gets(knownwords[i]);

	//for each test case below:
	for (i=0;i<testcases;i++)
	{
		gets(alien);
		alienlen=strlen(alien);
		
		//clean user dicts
		for (j=0;j<5002;j++)
		{
			for(k=0;k<200;k++)userdict[j][k]='\0';
		}
		j=0;k=0;current=0;
		left=0;right=0;
		//generate user dict for each alien word
		for(j=0;j<alienlen;j++)
		{
			if ((alien[j]!='(')&&(alien[j]!=')')&&(!left))
				{
					userdict[k][current]=alien[j];
					current=0;
					k++;
				}
			else 
				{
				if (alien[j]=='(')left=1;
				if (alien[j]==')')right=1;
				if (left&&right)
					{
					k++;
					current=0;
					left=0;right=0;						
					}
				else
					{
						if (alien[j]!='(')
						{
							userdict[k][current]=alien[j];
							current++;
						}
					}
				}
		}
		
		
		
		res=0;testres=1;;
		for (j=0;j<linenum;j++)
		{
			res1=1;
			for(k=0;k<len;k++)
			{
				res1=res1&&(in(knownwords[j][k],userdict[k]));
			}
			res+=res1;
			//printf("%d",in(knownwords[j][k],userdict[k]));
			//printf("|");
			//res1=(testres&&(in(knownwords[j][k],userdict[k])));
			//res+=res1;
		}
		printf("Case #%d",i+1);
		printf(": %d",res);
		printf("\n");
		//for (ii=0;ii<linenum;ii++) printf("%s\n",userdict[ii]);
	}	
		

		//for (ii=0;ii<linenum;ii++) printf("%s\n",knownwords[ii]);

}
/*
DATA FOR THIS PROBLEM

INPUT 
   
Output 
   
3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc

OUTPUT:

Case #1: 2
Case #2: 1
Case #3: 3
Case #4: 0
 

*/



/*
one of the possible test cases for problem 3
wewellccoommee to code qps jam
*/
