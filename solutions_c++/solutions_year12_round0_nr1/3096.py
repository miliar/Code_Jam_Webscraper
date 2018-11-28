#include<iostream>
#include<cstdio>
using namespace std;

FILE *fp,*fp2;

void Init()
{
	fp = fopen("A-small-attempt0.in","r");
	fp2 = fopen("A-small.out","w");
}

void Close()
{
	fclose(fp);
	fclose(fp2);
}

char ch[27] = {'y','h','e','s','o','c','v',   'x','d','u','i','g','l','b',  'k','r','z','t','n','w',  'j','p','f','m','a','q'};

int main(void)
{
	Init();

	int i,T,cases;
	char str[1029];

	fscanf(fp,"%d",&cases);
	fgets(str,1024,fp);
	for(T=1;T<=cases;T++)
	{
		fgets(str,1024,fp);
		for(i=0;str[i]!='\0';i++)
		{
			if(str[i]!=' ')
				str[i] = ch[str[i]-'a'];
		}
		str[i-1] = '\0';
		fprintf(fp2,"Case #%d: %s\n",T,str);
	}
	Close();

	return 0;
}