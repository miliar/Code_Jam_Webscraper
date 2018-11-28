#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>

using namespace std;


int main()
{
	int i,j,n,t;
	char mapping[]="yhesocvxduiglbkrztnwjpfmaq";
	char input[200];

	scanf("%d\n",&t);
	for(j=1;j<=t;j++)
	{
		gets(input);
		for(i=0;i<strlen(input);i++)
			if(input[i]!=' ')
				input[i]=mapping[s[i]-'a'];
		printf("Case #%d: %s\n",j,input);
	}
	return 0;
}
