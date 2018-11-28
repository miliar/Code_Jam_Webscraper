#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{
	char g[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	FILE *f=fopen("A-small-attempt2.in","rb");
	if(!f)
	{
		printf("fail to open\r\n");
		return 0;
	}

	int num;
	fscanf(f,"%d\n",&num);
	char **str=new char*[num];
	
	for(int i=0;i<num;i++)
	{
		str[i]=new char[200];
		fgets(str[i],200,f);
	}
	fclose(f);

	f=fopen("out.txt","wb");
	for(int i=0;i<num;i++)
	{
		fprintf(f,"Case #%d: ",i+1);
		for(char* pc=str[i];*pc!=0;pc++)
		{
			if(*pc<'a'||*pc>'z')
				putc(*pc,f);
			else
				putc(g[*pc-'a'],f);
		}
		fprintf(f,"\n");
		delete[] str[i];
	}
	fclose(f);

	delete[] str;
	return 0;
}