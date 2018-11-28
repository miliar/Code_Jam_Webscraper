#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<map>
#include<string>

using namespace std;
map <string,char> array;
int N,M,total;

void check(char *sth,int add)
{
	string cur="";
	int len=strlen(sth),i=0,ok=0;
	while(i<len)
	{
		if(sth[i]=='/')
		{
			if(!ok) ok=1;
			else
			{
				if(array[cur]);
				else
				{
					array[cur]=1;
					total+=add;
				}
			}
		}
		cur+=sth[i];
		i++;
	}
	if(array[cur]);
	else
	{
		array[cur]=1;
		total+=add;
	}
}

int main()
{
	int u,T,i;
	char current[1000];
	FILE *input=fopen("file.in","r"),*output=fopen("file.out","w");
	fscanf(input," %d",&T);
	for(u=1;u<=T;u++)
	{
		printf("Case %d\n",u);
		array.clear();
		total=0;
		fscanf(input," %d %d",&N,&M);
		for(i=1;i<=N;i++)
		{
			fscanf(input," %s",current);
			check(current,0);
		}
		for(i=1;i<=M;i++)
		{
			fscanf(input," %s",current);
			check(current,1);
		}
		fprintf(output,"Case #%d: %d\n",u,total);	
	}
	return 0;
}
