#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;
int del(int,char*,int);
char w[5000][16];
int main()
{
	FILE *fp;
	fp=fopen("output.txt","w");
	int l,d,n;
	cin>>l>>d>>n;

	int i,j,k,ch,count;
	char word[5000][16];

	for(i=0;i<d;i++)
	{
		cin>>word[i];
	}
	
	char test[500][520],charset[27];
	int token;

	for(i=0;i<n;i++)
	{
		cin>>test[i];
		for(j=0;j<d;j++)
			strcpy(w[j],word[j]);
		count=d;
		token=0;
		for(k=0;k<strlen(test[i]);k++)
		{
				ch=0;
				if(test[i][k]=='(')
				{
					k++;
					while(test[i][k]!=')')
						charset[ch++]=test[i][k++];
					token++;
				}	
				else
				{
					charset[ch++]=test[i][k];
					token++;
				}
				charset[ch]='\0';
				count=del(token-1,charset,count);
			
		}
		printf("Case #%d: %d\n",i+1,count);
		fprintf(fp,"Case #%d: %d\n",i+1,count);
	}
	fclose(fp);
	return 0;
}

int del(int pos,char *charset,int d)
{
	int i,j,k,flag,z,count;
	count=d;

	for(i=0;i<d;i++)
	{
		flag=0;
		for(j=0;j<strlen(charset);j++)
		{
			if(w[i][pos]==charset[j])
				flag=1;
		}
		if(flag==0)
		{
			for(k=i;k<d;k++)
			{
				strcpy(w[k],w[k+1]);
			}
			d--;
			i--;
		}
	}
	return d;
}
