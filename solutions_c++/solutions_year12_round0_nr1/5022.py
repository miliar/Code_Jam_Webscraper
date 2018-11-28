#include<stdio.h>
#include<string.h>
int main()
{
	int t,l;
	int a[26]={
		24,6,2,15,10,-3,15,16,-5,11,-2,-5,-1,-12,-4,2,9,2,-5,3,-11,-6,-17,-11,-24,-9
	};
	char str[100000],c,cases=0;
	scanf("%d",&t);
	while(t--)
	{
		cases++;
		scanf("%c",&c);
		scanf("%[^\n]",&str);
		l=strlen(str);
		for(int i=0;i<l;i++)
		{
			if(str[i]>='a'&&str[i]<='z')
			{
				str[i]=(char)(str[i]+a[int(str[i]-'a')]);
			}
		}
		printf("Case #%d: %s\n",cases,str);
	}
}