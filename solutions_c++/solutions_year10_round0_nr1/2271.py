#include<iostream>
#include<cstring>
#include<stdio.h>
using namespace std;
int main()
{
	int t,text,n,k,i;
	freopen("A-large.in","r",stdin);
	freopen("A-small-attempt.out","w",stdout);
	scanf("%d",&text);
	for(t=1;t<=text;t++)
	{
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",t);
		if (((k+1)%(1<<n))==0)
			printf("ON\n");
		else printf("OFF\n");
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
