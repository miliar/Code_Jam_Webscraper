#include <iostream>
#include <cstdio>
using namespace std;

int main(void)
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t,T;
	scanf(" %d ",&T);
	for(int t = 1; t <= T; ++t)
	{
		printf("Case #%d: ",t);
		//char arr[] = "ynficwlbkuomxsevzpdrjgthaq";
		char str[200];
		char arr[] = "yhesocvxduiglbkrztnwjpfmaq";
		gets(str);
		for(int i=0; str[i]; i++)
			if(str[i]>=97 && str[i]<=122)
				putc(arr[str[i]-97],stdout);
			else
				putc(str[i],stdout);
		putc('\n',stdout);
	}
	return 0;
}
