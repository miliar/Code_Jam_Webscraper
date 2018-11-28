#include<stdio.h>
#include<iostream>
#include<string.h>
char a[5000][100];
int d,l,n;
FILE *in,*ou;
int split(char test[100][1000])
{
	int value=0,j;
	char key[2],temp[1000];
	for(int i=0;i<d;i++)
	{	
		for(j=0;j<l;j++)
		{
			key[0]=a[i][j];
			key[1]='\0';
			strcpy(temp,test[j]);
	//		printf("value of i %d and key is %s temp is %s\n",i,key,temp);
			if(strstr(temp,key)==NULL)
				break;			
		}
		if(j==l)
			value++;
	}
	return value;
}
int main()
{
	int i=0;
	char inp[1000],input[100][1000],l1[10],d1[10],n1[10];
	in=fopen("in2","r");
	ou=fopen("output","w");
	fscanf(in,"%s%s%s",l1,d1,n1);
	sscanf(l1,"%d",&l);
	sscanf(d1,"%d",&d);
	sscanf(n1,"%d",&n);
	for(int i=0;i<d;i++)
	{
		fscanf(in,"%s",a[i]);
	}
	for(int i=0;i<n;i++)
	{
		fscanf(in,"%s",inp);
		int g=0;
		for(int j=0;j<strlen(inp);)
		{
			if(inp[j]=='(')
			{
				int k=0;
				j++;
				while(inp[j]!=')')
				{
					input[g][k]=inp[j];
					k++;
					j++;
				}
				input[g][k]='\0';
				j++;
				g++;
			}
			else
			{
				input[g][0]=inp[j];
				input[g][1]='\0';
				g++;
				j++;
			}
		}
		int val=split(input);
	//        printf("Case #%d: %d\n",i+1,val);
		fprintf(ou,"Case #%d: %d\n",i+1,val);


	}
	return 1;
}
