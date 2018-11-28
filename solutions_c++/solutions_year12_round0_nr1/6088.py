#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
using namespace std;

char str[1000000],temp[28]={"yhesocvxduiglbkrztnwjpfmaq"};
int main()
{
	int t,cas=0,len,i,dummy;
	freopen("A-small-attempt1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d%c",&t,&dummy);
	while(t--)
	{
		gets(str);
		len=strlen(str);
		for(i=0;i<len;i++)
		{
			if(str[i]>='a'&&str[i]<='z'){str[i]=temp[str[i]-'a'];}
		}
		printf("Case #%d: %s\n",++cas,str);
	}
	return 0;
}