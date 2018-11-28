#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <string>
#include <math.h>
#include <algorithm>

using namespace std;

char code[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;
	cin >> t;
	char ch;
	scanf("%c",&ch);
	for (int cnt=1;cnt<=t;cnt++)
	{
		printf("Case #%d: ",cnt);
		while ((ch=getchar())!=EOF && ch!='\n')
		{
			if (ch==' ') printf(" ");
			else printf("%c",code[ch-'a']);
		}
		printf("\n");
	}
	return 0;
}