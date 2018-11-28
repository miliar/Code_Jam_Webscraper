#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
const int MAXL = 200;
char s[MAXL];
int main()
{
	int cases;
	scanf("%d",&cases);
	for (int tcase=1;tcase<=cases;tcase++)
	{
		scanf("%s",s);
		int len=strlen(s);
		int totw=0;
		for (int i=0;i<len;i++)
			if (s[i]=='?') totw++;
		if (totw==0)
		{
			printf("Case #%d: ",tcase);
			puts(s);
			continue;
		}
		for (int st=0;st<(1<<totw);st++)
		{
			long long t=0;
			int temp=st;
			for (int j=0;j<len;j++)
			if (s[j]=='?')
			{
				t=t*2+(temp&1);
				temp/=2;
			} else t=t*2+s[j]-'0';
			long long p=(long long)sqrt(t)+1e-8;
			if (p*p==t)
			{
				printf("Case #%d: ",tcase);
				int temp=st;
				for (int j=0;j<len;j++)
				if (s[j]=='?')
				{
					printf("%d",(temp&1));
					temp/=2;
				} else printf("%c",s[j]);
				printf("\n");
				break;
			}
		}
	}
}
