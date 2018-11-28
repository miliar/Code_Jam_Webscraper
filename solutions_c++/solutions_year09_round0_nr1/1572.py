// Alien Language.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "string.h"
#include <iostream>
using namespace std;
int L,D,N;
char temp[1005];
char temp2[20];
const int MOD=4777;
int ELFhash(char *key)              
{ 
	unsigned long h=0; 
	while(*key) 
	{ 
		h=(h<<4)+*key++; 
		unsigned long g=h&0Xf0000000L; 
		if(g) h^=g>>24; 
		h&=~g; 
	} 
	return h%MOD; 
} 
struct Node
{
	char test[20];
	int next;
}my_hash[5000];
int p[MOD+5];
int index;
void Insert(char str[])
{
	int m=ELFhash(str);
	int t=p[m];
	while(t!=-1)
	{
		if(strcmp(my_hash[t].test,str)==0) return;
		t=my_hash[t].next;
	}
	strcpy(my_hash[index].test,str);
	my_hash[index].next=p[m];
	p[m]=index++;
}
bool Find(char str[])
{
	int m=ELFhash(str);
	int t=p[m];
	while(t!=-1)
	{
		if(strcmp(my_hash[t].test,str)==0) return true;
		t=my_hash[t].next;
	}
	return false;
}
int ans;
void DFS(int i,int index)
{
	temp2[i]='\0';
	if(!Find(temp2)) return;
	if(i==L)
	{
		ans++;
		return;
	}
	if(temp[index]>='a'&&temp[index]<='z')
	{
		temp2[i]=temp[index];
		DFS(i+1,index+1);
	}
	else if(temp[index]=='(')
	{
		int end=index+1;
		while(temp[end]!=')') end++;
		for(int j=index+1;j<end;j++)
		{
			temp2[i]=temp[j];
			DFS(i+1,end+1);
		}
	}
}
int main()
{
	//freopen("d:\\1.txt","r",stdin);
	freopen("d:\\A-small-attempt1.in","r",stdin);
	freopen("d:\\A-small-attempt1.out","w",stdout);
	scanf("%d%d%d\n",&L,&D,&N);
	memset(p,-1,sizeof(p));
	index=0;
	for(int i=0;i<D;i++)
	{
		cin.getline(temp2,20);
		for(int j=L;j>0;j--)
		{
			temp2[j]='\0';
			Insert(temp2);
		}
	}
	temp2[0]='\0';
	Insert(temp2);
	for(int i=1;i<=N;i++)
	{
		cin.getline(temp,1000);
		ans=0;
		DFS(0,0);
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}

