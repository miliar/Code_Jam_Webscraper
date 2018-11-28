#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<queue>

using namespace std;

unsigned int T,R,K,N;
queue<unsigned int> q;
queue<unsigned int> qtmp;
unsigned int arr[11];
int MaxLine = 1024,i;
char buf[1024];
char *p;
FILE* fp;
FILE* fout;

void Handle()
{
	int res = 0;
	for(int t=0;t<R;t++)
	{
		unsigned int full = 0;
		while(!q.empty())
		{
			if(full+q.front() <= K)
			{
				full += q.front();
				qtmp.push(q.front());
				q.pop();
			}
			else break;
		}
		while(!qtmp.empty()){ q.push(qtmp.front()); qtmp.pop();}
		res += full;
	}
	fprintf(fout,"Case #%d: %d\n",i/2,res);
	fflush(fout);
}

int main(int argc,char* argv[])
{
	if((fp=fopen(argv[1],"r")) == NULL)
	{
		return -1;
	}
	if((fout=fopen("B.out","w")) == NULL)
	{
		return -1;
	}
	i = 0;
	while(fgets(buf,MaxLine,fp) != NULL)
	{
		if(i == 0)
		{
			sscanf(buf,"%d",&T);
		}
		else if(i%2)
		{
			sscanf(buf,"%d %d %d",&R,&K,&N);
		}
		else
		{
			p = strtok(buf," ");
			while(!q.empty()) q.pop();
			q.push(atoi(p));
			while((p = strtok(NULL," "))) 
			{
				q.push(atoi(p));
			}
			Handle();
		}
		i++;
	}
	fclose(fp);
	fclose(fout);
	return 0;
}