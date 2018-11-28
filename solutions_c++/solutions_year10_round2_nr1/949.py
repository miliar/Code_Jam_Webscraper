#include<stdio.h>
#include<iostream>
#include<cstring>
#include<string.h>

#define MAX 10000

char Dizin[MAX][102];
int S;

int Search(char *temp)
	{
	for(int i=0; i<S; i++)
		if(!strcmp(Dizin[i],temp))
			return 0;
	
	strcpy(Dizin[S],temp);
	S++;
	return 1;
	}

int Add(char *dizin)
	{
	char *temp,temp2[102]="/";
	int ans=0;
	
	temp = strtok(dizin,"/");
	while(temp)
		{
		strcat(temp2,temp);
		strcat(temp2,"/");
		ans += Search(temp2);
		temp = strtok(NULL,"/");
		}
	return ans;
	}

int main()
	{
	int T,N,M;
	int ans;
	char temp[102];
	scanf("%d ",&T);
	
	for(int i=1; i<=T; i++)
		{
		scanf("%d %d ",&N,&M);
		
		S=0;
		ans=0;
		for(int j=0; j<N; j++)
			{
			scanf("%s ",temp);
			Add(temp);
			}
		
		for(int j=0; j<M; j++)
			{
			scanf("%s ",temp);
			ans+= Add(temp);
			}
		printf("Case #%d: %d\n",i,ans);
		}
	return 0;
	}
