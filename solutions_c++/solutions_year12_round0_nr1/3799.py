#include<cstdio>

using namespace std;

char map[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
	int T;
	char gstring[103];
	scanf("%d\n",&T);
	for (int t=1;t<=T;t++)
	{
		gets(gstring);
		for (int i=0;gstring[i]!='\0';i++)
		{
			if (gstring[i]!=' ')
			{
				gstring[i]=map[(gstring[i]-'a')];
			}

		}
		printf("Case #%d: %s\n",t,gstring);
	}
	return 0;
}
