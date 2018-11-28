#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define smax 100
#define qmax 1000

char temp[128];

int find(int offset, int qid[qmax], int snumb, int qnumb)
{
	int i, count=0, sloc[smax];
	for(i=0; i<snumb; i++)	sloc[i]=-1;
	while(offset<qnumb)
	{
		if(sloc[qid[offset]]==-1)
		{
			sloc[qid[offset]]=offset;
			count++;
		}
		if(count==snumb)	return offset;
		offset++;
	}
	for(i=0; i<snumb; i++)	if(sloc[i]==-1)	return -1;
}

void search(int trial)
{
	int i, j, snumb, qnumb, qid[qmax], sid=-1, count=0, offset=0;
	char sdata[smax][128], qdata[qmax][128];
	snumb=atoi(gets(temp));
	for(i=0; i<snumb; i++)
	{
		gets(sdata[i]);
	}
	qnumb=atoi(gets(temp));
	for(i=0; i<qnumb; i++)
	{
		gets(qdata[i]);
	}

	for(i=0; i<qnumb; i++)
	{
		int result;
		for(j=0; j<snumb; j++)
		{
			if((result=strcmp(sdata[j], qdata[i]))==0)
			{
				qid[i]=j;
				break;
			}
		}
	}

	while((offset=find(offset, qid, snumb, qnumb))>=0)	count++;
	printf("Case #%d: %d\n", trial+1, count);
}

int main()
{
	int i, n;
	n=atoi(gets(temp));
	for(i=0; i<n; i++)	search(i);
	return 0;
}