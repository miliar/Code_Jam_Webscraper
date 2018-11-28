#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>



void main()
{
int cases,index_cases,i,index,uc,spc,len;
char InpStr[401],OutStr[101];
char trans[26];
trans[0]='y';
trans[1]='h';
trans[2]='e';
trans[3]='s';
trans[4]='o';
trans[5]='c';
trans[6]='v';
trans[7]='x';
trans[8]='d';
trans[9]='u';
trans[10]='i';
trans[11]='g';
trans[12]='l';
trans[13]='b';
trans[14]='k';
trans[15]='r';
trans[16]='z';
trans[17]='t';
trans[18]='n';
trans[19]='w';
trans[20]='j';
trans[21]='p';
trans[22]='f';
trans[23]='m';
trans[24]='a';
trans[25]='q';

freopen("A-small-attempt0.in" , "rt" , stdin ) ;
freopen("A-small-attempt0.out" , "wt" , stdout ) ;

cases = 0;
//read the number of test cases 
scanf("%d",&cases);
//printf("Cases = %d\n",cases);
scanf("%c",&InpStr[0]);


//Loop through all the cases
for (index_cases=0 ; index_cases<cases; index_cases++)
{
//	scanf("%s",InpStr);
//	len =strlen(InpStr);

	for(i=0;i<401;i++)
	{
		scanf("%c",&InpStr[i]);
		if //(InpStr[i]== ' ') word++; else if 
		(InpStr[i]== '\n') break;
	}
	len = i;
//	printf("len = %d: ",len);
//	for(i=0;i<len;i++)
//	{
//		printf("%d\n",InpStr[i]);
//	}


	memset(OutStr,0,sizeof(OutStr));
	for (i=0;i<len;i++)
	{
		if ((InpStr[i]>='a')&&(InpStr[i]<='z'))
		{
	
			uc= 0;
			index = InpStr[i]-'a';
			spc = 0;
		}

		else if ((InpStr[i]>='A')&&(InpStr[i]<='Z'))
		{
	
			uc= 1;
			index = InpStr[i]-'A';
			spc = 0;
		}
		else
		{
			uc=0;
			spc = 1;
			OutStr[i] = InpStr[i];
		}
		if (spc==0)
		{
			OutStr[i] = trans[index] + (uc * ('A'-'a')); 
		}
	}
	OutStr[i] ='\n';

	printf("Case #%d: ",index_cases+1);
	for(i=0;i<len+1;i++)
	{
		printf("%c",OutStr[i]);
	}

}
fclose(stdin) ;
fclose(stdout) ;
}