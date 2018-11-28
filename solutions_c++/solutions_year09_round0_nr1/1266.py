#include<stdio.h>
#include<string.h>

char words[5000][20];
bool pattern[500][26];
char str[500000];

int main()
{
	int l,d,n;
	scanf("%d%d%d",&l,&d,&n);
	getchar();
	for(int i=0;i<d;i++)
		gets(words[i]);
	int kase=1;
	while(n--)
	{
		memset(pattern,0,sizeof(pattern));
		fgets(str,500000,stdin);
		printf("Case #%d: ",kase++);
		int len=strlen(str),cnt=0;
		bool in_bracket=false;
		for(int i=0;i<len;i++)
		{
			if(str[i]=='(')
				in_bracket=true;
			else if(str[i]>='a'&&str[i]<='z')
			{
				pattern[cnt][str[i]-'a']=true;
				if(!in_bracket) cnt++;
			}
			else if(str[i]==')')
			{
				cnt++;
				in_bracket=false;
			}
		}
		cnt=0;
		for(int i=0;i<d;i++)
		{
			bool flag=true;
			for(int j=0;j<l;j++)
				if(!pattern[j][words[i][j]-'a'])
				{
					flag=false;
					break;
				}
			if(flag)
				cnt++;
		}
		printf("%d\n",cnt);
	}
	return 0;
}