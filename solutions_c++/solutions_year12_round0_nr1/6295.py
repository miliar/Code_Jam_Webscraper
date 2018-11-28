#include<stdio.h>
#include<string.h>
int map[300]={0};

char Gstr[3][110]={"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"};

char Sstr[3][110]={"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"};

void study()
{
	int i,j;
	for(i=0;i<3;i++)
		for(j=0;Gstr[i][j]!='\0';j++)
		{
			map[Gstr[i][j]]=Sstr[i][j];
		}
	map['y']='a';
	map['q']='z';
	map['e']='o';
	map['z']='q';
}

int main()
{
	FILE* out, *in;
    int k,i,t; char ss[110],res[110];
	in = fopen("A-small-attempt4.in","r");
	out = fopen("output.txt","w");
	fscanf(in,"%d\n",&t);
	study();
	for(k=1;k<=t;k++)
	{
		fgets(ss,1024,in);
		int len=strlen(ss);
		for(i=0;i<len;i++)
		{
			res[i]=map[ss[i]];
		}
		res[len]='\0';
		if(k<t)
	    	fprintf(out,"Case #%d: %s\n",k,res);
		else
			fprintf(out,"Case #%d: %s",k,res);
	}
	return 0;
}
