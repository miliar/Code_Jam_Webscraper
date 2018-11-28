#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;
char ar[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char c[110];
int main()
{
    freopen("A-small-attempt4.in","r",stdin);
	freopen("A-small-attempt4.out","w",stdout);
	int n,k=0;
	scanf("%d\n",&n);
	while(n--)
	{
		k++;
		gets(c);
		int l=strlen(c);
		printf("Case #%d: ",k);
		for(int i=0;i<l;i++)
		{
			if(c[i]!=' ')
				c[i]=ar[c[i]-'a'];
			printf("%c",c[i]);
		}
		printf("\n");
	}
    return 0;
}