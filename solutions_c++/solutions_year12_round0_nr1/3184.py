#include <iostream>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
using namespace std;
char s[]="yhesocvxduiglbkrztnwjpfmaq";
int main()
{
	int t,i,j,k,n,zz;
	//freopen("example.txt","r",stdin);
	char tmp[1000];
	scanf("%d",&t);
	getchar();
	zz=1;
	while(t--)
	{
		gets(tmp);
		printf("Case #%d: ",zz);
		for(i=0;tmp[i]!='\0';i++)
		{
			if(tmp[i]==' ')
				printf(" ");
			else
				printf("%c",s[tmp[i]-'a']);
		}
		printf("\n");
		zz++;
	}
	return 0;
}