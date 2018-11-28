/*Speaking in Tongues*/

#include<cstdio>

using namespace std;

char mapping[]="yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	char str[128];
	int i,j,T;
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A.out","wt",stdout);
	scanf("%d",&T);
	gets(str);
	for(i=1;i<=T;i++)
	{
		gets(str);
		for(j=0;str[j]!='\0';j++)
			if(str[j]!=' ')
				str[j]=mapping[str[j]-'a'];
		printf("Case #%d: %s\n",i,str);
	}
	return 0;
}