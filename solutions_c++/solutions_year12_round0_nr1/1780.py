#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <map>
#include <string>
#include <cmath>
#include <math.h>
#include <fstream>

using namespace std;

int t;
char c[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char a[100][200];

int main()
{
	scanf("%d\n",&t);
	for(int tt=1;tt<=t;tt++)
		gets(a[tt]);
	for(int tt=1;tt<=t;tt++)
	{
		printf("Case #%d: ",tt);
		for(int i=0;a[tt][i]!='\0';i++)
			if(a[tt][i]>='a'&&a[tt][i]<='z')
				printf("%c",c[a[tt][i]-'a']);
			else printf("%c",a[tt][i]);
		printf("\n");
	}
	return 0;
}