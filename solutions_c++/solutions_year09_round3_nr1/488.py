#include<stdio.h>
#include<string.h>
#include<stdlib.h>
char word[100];
int map[1000];
int num[1000];
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("f.txt","w",stdout);
	int i,j;
	int T;
	scanf("%d",&T);
	getchar();
	int case_cnt=1;
	while(T--)
	{
		long long res;
		memset(num,0,sizeof(num));
		memset(map,-1,sizeof(map));
		int cnt=0;
		gets(word);
		int len=strlen(word);
		//if(len>1)
		//{
			map[word[0]+256]=1;
			int type_cnt=1;
			num[0]=1;
			for(i=1;i<len;i++)
			{
				if(map[word[i]+256]==-1)
				{
					num[i]=cnt;
					map[word[i]+256]=cnt++;
					if(cnt==1)
						cnt++;
					type_cnt++;
				}
				else
					num[i]=map[word[i]+256];
			}
			res=0;
			if(type_cnt==1)
				type_cnt++;
			for(i=0;i<len;i++)
				res=res*type_cnt+num[i];
		//}
		//else
		//	res=0;
		printf("Case #%d: %lld\n",case_cnt++,res);
	}
}