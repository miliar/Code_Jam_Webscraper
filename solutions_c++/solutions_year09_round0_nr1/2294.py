#include <stdio.h>
#include <iostream.h>

struct words
{
	char word[26];


} w[50000];

int main()
{
	FILE *in,*out;
	int l,d,n,k,i=0,t=0,num,j,counter=0,flag;
	char t1[26],t2[26],t3[26],temp[150][26];
	in=fopen("in2.txt","r");
	out=fopen("out.txt","w");
	fscanf(in,"%s%s%s",t1,t2,t3);
	sscanf(t1,"%d",&l);
	sscanf(t2,"%d",&d);
	sscanf(t3,"%d",&n);
	printf("%d\t%d\t%d",l,d,n);
	for(;i<d;i++)
	fscanf(in,"%s",w[i].word);
	for(num=0;num<n;num++)
	{
	char ch;
	fscanf(in,"%c",&ch);
	counter=0;		
	for(t=0;t<l;t++)
	{	
		char t1;
		fscanf(in,"%c",&t1);
		if(t1=='(')
		{
			fscanf(in,"%[^)]",temp[t]);
			fscanf(in,"%c",&t1);
		}
		else{	
			temp[t][0]=t1;
			temp[t][1]='\0';
			}
		printf("%s\n",temp[t]);
	}
/*	for(i=0;i<t;i++)
	{	
		if(strlen(temp[i])==1)
			continue;
		else
		{	
			for(j=0;j<strlen(temp[i])-1;j++)
				temp[i][j]=temp[i][j+1];
			temp[i][strlen(temp[i])-2]='\0';

		}
		printf("%s\n",temp[i]);

	}*/
	for(i=0;i<d;i++)
	{
		for(j=0;j<l;j++)
		{	flag=0;
			for(k=0;k<strlen(temp[j]);k++)
				if(w[i].word[j]==temp[j][k])
					flag=1;
			if(flag==0)
				break;

		}
		if(j==l)
			counter++;
	}
	fprintf(out,"Case #%d: %d\n",num+1,counter);

}
fcloseall();
}


