#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

int main()
{
	char f[28]={'y','h','e','s','o','c','v','x','d','u','i','g','l'
	,'b','k','r','z','t','n','w','j','p','f','m','a','q'};

	int t,i,l,cas=0;
	char s[105];

	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("out.out","w",stdout);

	scanf("%d",&t);
	getchar();
	while(t--)
	{
		gets(s);
		printf("Case #%d: ",++cas);
		l=strlen(s);
		for(i=0;i<l;i++)
			if (s[i]!=' ')
				printf("%c",f[s[i]-'a']);
			else
				printf(" ");
		printf("\n");
	}
	return 0;
}
