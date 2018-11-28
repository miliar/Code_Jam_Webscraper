#include <stdio.h>
#include <string.h>
void input();
void process();
void output(int T);

char code[27]={0,'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char googcode[200],normcode[200];

int main()
{
	int i,T;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d\n",&T);
	for(i=1; i<=T; i++)
	{
		input();
		process();
		output(i);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}

void input()
{
	int i;
	for(i=1; i<=150; i++)
	{
		googcode[i]=0;
		normcode[i]=0;
	}
	gets(googcode+1);
}

void process()
{
	int i,len;
	len = strlen(googcode+1);
	for(i=1; i<=len; i++)
	{
		if(googcode[i]==' ')normcode[i]=' ';
		else normcode[i]=code[googcode[i]-'a'+1];
	}

}

void output(int T)
{
	printf("Case #%d: %s\n",T,normcode+1);
}