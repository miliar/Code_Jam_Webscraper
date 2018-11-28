#include<hash_map>
#include<stdio.h>
#include<algorithm>
#include<string.h>
stdext::hash_map<char,char> hash;
stdext::hash_map<char,char> hash_1;


void main()
{
	char *src="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char*dest="our language is impossible to understand there are twenty six factorial possibilities so it is okey if you want to just give up";
	char * p,*q;
	p=dest;q=src;
	while(*p!='\0')
	{
		hash_1[*p]=*q;
		p++;q++;
	}
	hash_1['q']='z';
	hash_1['z']='q';
	stdext::hash_map<char,char>::const_iterator itr;
	for(itr=hash_1.begin();itr!=hash_1.end();itr++)
	{
		hash[(*itr).second]=(*itr).first;
	}
	FILE* file,*output;
	file=fopen("data\\A-small-attempt3.in","rb");
	output=fopen("data\\A-small-attempt3.output","wt+");
	int n_count;
	fscanf(file,"%d",&n_count);
	fscanf(file,"\n");
	for(int i=0;i<n_count;i++)
	{	
		char string[255];
		fgets(string,255,file);
		char* p=string;		
		
		fprintf(output,"Case #%d: ",i+1);
		while(*(p+1)!='\0')
		{
			fprintf(output,"%c",hash[*p]);
			p++;
		}
		fprintf(output,"\n");
	}
	fclose(file);
	fclose(output);
}
