#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <cmath>
#include <vector>
using namespace std;

char a[30]={'y','h','e','s','o','c','v',
            'x','d','u','i','g','l','b',
			'k','r','z','t','n','w','j',
			'p','f','m','a','q' 
           };
int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.out","w",stdout);
	
    int ca;
	int tca=1;
	scanf("%d",&ca);
    char strbuf[110];
	getchar();
	while(ca--)
	{
	    cin.getline(strbuf,110,'\n');
		printf("Case #%d: ",tca++);
		for(int i=0;i<strlen(strbuf);i++)
		{
            if(strbuf[i]!=' ')
               printf("%c",a[strbuf[i]-'a']);
			else
			   printf(" ");
			
		}
		printf("\n");
	}

	return 0;
}