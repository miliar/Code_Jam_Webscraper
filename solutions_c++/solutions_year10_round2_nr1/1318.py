// cjr21.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<malloc.h>
#include<string.h>

struct abc
{
	char dirs[100][100];
	struct abc *next[100];
	int count;
};

typedef struct abc node;

int check(node *t,char a[100])
{
	for(int i=0;i<t->count;i++)
	{
		if(!strcmp(t->dirs[i],a))
			return i;
	}
	return -1;
}

void create(node *t,node *t2,char a[100])
{
	strcpy(t->dirs[t->count],a);
	t->next[t->count]=t2;
	t->count=t->count+1;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int c,n,total,mkdirs=0,k;
	char ch;
	int p,q;
	char words[100][100];
	FILE *fp=fopen("a.in","r");
	FILE *fout=fopen("out","w");
	fscanf(fp,"%d",&total);
	for(int i=0;i<total;i++)
	{
		mkdirs=0;
		node *head=(node *)(malloc(sizeof(node)));
		head->count=0;
		fscanf(fp,"%d %d",&c,&n);
		fscanf(fp,"%c",&ch);
		for(int j=0;j<c+n;j++)
		{
			fscanf(fp,"%c",&ch);
			node *t=head;
			p=0;q=0;
			while(1)
			{
				fscanf(fp,"%c",&ch);
//				printf("a%c",ch);
				if(ch=='/')
				{
//					printf("Found \\");
					words[p][q]='\0';
					p++;
					q=0;
					continue;
				}
				else if(ch=='\n')
					break;
				else if(feof(fp))
					break;
				words[p][q++]=ch;
			}
			words[p][q]='\0';
//			printf("a");
//			for(int k=0;k<=p;k++)
//				printf("%s\n",words[k]);
			k=0;
			while(k<=p)
			{
				int num=check(t,words[k]);
//				printf("check returned %d",num);
				if(num!=-1)
				{
//					printf("here");
					t=t->next[num];
					k++;
					continue;
				}
				else
				{
					node *t2=(node *)(malloc(sizeof(node)));
					t2->count=0;
					create(t,t2,words[k]);
//					printf("created");
					if(j>=c)
						mkdirs++;
					t=t2;
					k++;
				}
			}
		}
		printf("Case #%d: %d\n",i+1,mkdirs);
		fprintf(fout,"Case #%d: %d\n",i+1,mkdirs);
	}
	return 0;
}