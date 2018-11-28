#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX 10000



//Name : GetNextToken
//This function returns next word from the bufer
//Parameters 
//buf : string buffer to scan.
//Returns: Next word from the buffer
char *GetNextToken(char *buf)
{
	char *token=NULL;
	long i=0;

	while(buf[i] != ' ' && buf[i] != '\0')
	{
		i++;
	}
	token = (char*)malloc(i+1);
	memset(token,0,i+1);
	strncpy(token,buf,i);
	return token;
}


long isDivideEachOther(long n,long m)
{
	long r=0;
	if(n%m==0)
		r=1;
	if(m%n==0)
		r=1;
	return r;
}


void ExecuteTestCase(long min,long max,long caseno,long playercount,long freq[MAX])
{
	long i=0,j=0;
	long res=0;
	long flag;
	for(i=min;i<=max;i++)
	{
		flag=0;
		for(j=0;j<playercount;j++)
		{
			if(!isDivideEachOther(i,freq[j]))
			{
				flag=0;
				break;
			}
		}
		if(j==playercount)
			flag=1;
		if(flag)
		{
			res=i;
			break;
		}		
	}
	if(flag)
	{
		printf("Case #%d: %d\n",caseno,i);
	}
	else
	{
		printf("Case #%d: NO\n",caseno);
	}

}



int main(long argc,char *argv[])
{

	long i=0;
	long c=0;
	char testc[BUFSIZ]="";
	char *testcase;
	long testcasecount=0;
	long noofplayers=0;
	long freq[MAX];
	long min,max;
	long j;
	char *temp=NULL;
	FILE *fp=NULL;
	if(argc < 1)
	{
		fprintf(stderr,"Error : input file missing\n");
		exit(-1);
	}
	fp = fopen(argv[1],"r");
	if(NULL == fp)
	{
		fprintf(stderr,"Input file read error ");
		exit(-1);
	}

	fgets(testc,BUFSIZ,fp);
	testcasecount = atoi(testc);

	while(c < testcasecount)
	{
		min=max=0;
		memset(freq,0,sizeof(long)*MAX);
		memset(testc,0,BUFSIZ);
		fgets(testc,BUFSIZ,fp);
		testcase = testc;
		temp=GetNextToken(testcase);		
		noofplayers= atoi(temp);
		testcase = testcase + strlen(temp) + 1;
		free(temp);
		temp=GetNextToken(testcase);		
		min=atoi(temp);
		testcase = testcase + strlen(temp) + 1;
		free(temp);
		temp=GetNextToken(testcase);		
		max=atoi(temp);
		free(temp);
		fgets(testc,BUFSIZ,fp);
		testcase = testc;
		j=0;
		while(j<noofplayers)
		{
		temp=GetNextToken(testcase);		
		freq[j++]  = atoi(temp);		
		
		testcase = testcase + strlen(temp) + 1;
		free(temp);
		}
		ExecuteTestCase(min,max,c+1,noofplayers,freq);
		c++;
	}

	return 0;
}
