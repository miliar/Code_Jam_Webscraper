#include<iostream>
#include<string.h>
using namespace std;
char dict[5100][20];
char str[100000];
char tmp[30];
int main()
{
	int l,n,m;
	scanf("%d%d%d",&l,&n,&m);
	printf("");
	for(int i=0;i<n;++i)
		scanf("%s",dict[i]);
	for(int t=1;t<=m;++t)
	{
		scanf("%s",str);
		int ans=0;
		for(int i=0;i<n;++i)
		{
			int len=0;
			int p=0;
			while(str[len])
			{
//				printf("%d\n",len);
				if(str[len]=='(')
				{
					++len;
					for(int j=0;str[len]!=')';++len,++j)
					{
						tmp[j]=str[len];
						tmp[j+1]=0;
					}
					++len;
				}
				else
				{
					tmp[0]=str[len++];
					tmp[1]=0;
				}
//				printf("%c %s\n",dict[i][p],tmp);
				int tag=0;
				for(int j=0;tmp[j];++j)
				{
					if(tmp[j]==dict[i][p])
					{
						tag=1;
						break;
					}
				}
				if(!tag)
					break;
				++p;
			}
			if(str[len]==0&&dict[i][p]==0)
				++ans;
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
