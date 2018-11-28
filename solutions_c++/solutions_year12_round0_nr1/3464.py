#include<stdio.h>
#include<string>
#include<iostream>
using namespace std;
char hai[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char hen(char a)
{
	return hai[a-'a'];
}
int main()
{
	FILE *fp;
	fp=fopen("A-small-attempt6.in","r");
	int data;
	fscanf(fp,"%d",&data);
	char gomi;
	fscanf(fp,"%c",&gomi);
	FILE *fp2;
	fp2=fopen("out.txt","w");
	for(int i=1;i<=data;i++)
	{
		fprintf(fp2,"Case #%d: ",i);
		for(;;)
		{
			char ch;
			fscanf(fp,"%c",&ch);
			if(ch=='\n')
			{
				break;
			}
			if(ch!=' ')
			{
				ch=hen(ch);
			}
			fprintf(fp2,"%c",ch);
		}
		fprintf(fp2,"\n");
	}
}