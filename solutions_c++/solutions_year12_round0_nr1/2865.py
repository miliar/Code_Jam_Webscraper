#include <algorithm>
#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;

#define zero(a) memset(a,0,sizeof(a))
#define one(a) memset(a,1,sizeof(a))
#define fone(a) memset(a,-1,sizeof(a))

char s[200];
char tochar[30]="yhesocvxduiglbkrztnwjpfmaq";
int main()
{
	int T;
	//freopen("1.in","r",stdin);
	//freopen("output.o","w",stdout);
	scanf("%d",&T);
	int TT=1;
	getchar();
	while(T--)
	{
		gets(s);
		printf("Case #%d: ",TT++);
		for(int i=0;s[i];i++)
		{
			if(s[i]==' ')
			{
				printf(" ");
				continue;
			}
			printf("%c",tochar[s[i]-'a']);
		}
		printf("\n");
	}
	return 0;
}