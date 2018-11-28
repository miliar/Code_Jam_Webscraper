#include <iostream>
#include <cstring>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
struct point{
char a,b;
}p[1001];
int main()
{
	char pp[27]={'y','h','e','s','o','c','v','x','d','u','i','g','l',
	'b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int nCase;
	char s[101];
	int i,j;
	freopen("A-small-attempt4.in","r",stdin);
	freopen("b.txt","w",stdout);
	scanf("%d",&nCase);
	getchar();
	for(i=1;i<=nCase;i++)
	{	
		gets(s);
		j=0;
		printf("Case #%d: ",i);	
		while(s[j]!='\0')
		{
			if(s[j]==' ')cout<<' ';
			else cout<<pp[s[j]-'a'];
			j++;
		}
		cout<<endl;
	}	
	return 0;
}
