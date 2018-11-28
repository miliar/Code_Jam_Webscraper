#include <cstdio>
#include <cstring>

bool oppo[1000][1000];
char change[1000][1000];
char str[1000];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int Case=1;Case<=T;Case++)
	{
		int C,D;
		scanf("%d",&C);
		memset(change,0,sizeof(change));
		memset(oppo,false,sizeof(oppo));
		for(int i=0;i<C;i++)
		{
			char str[5];
			scanf(" %s",str);
			change[str[0]][str[1]]=str[2];
			change[str[1]][str[0]]=str[2];
		}
		scanf("%d",&D);
		for(int i=0;i<D;i++)
		{
			char str[5];
			scanf(" %s",str);
			oppo[str[0]][str[1]]=true;
			oppo[str[1]][str[0]]=true;
		}
		int N;
		scanf("%d",&N);
		scanf(" %s",str);
		char re[200],*p=re;
		memset(re,0,sizeof(re));
		for(int i=0;i<N;i++)
		{
			*p=str[i];
			p++;
			while((p-re)>=2 && change[*(p-2)][*(p-1)])
			{
				*(p-2)=change[*(p-2)][*(p-1)];
				p--;
			}
			for(char *j=re;j<p;j++)
				if (oppo[*j][*(p-1)])
				{
					p=re;
					break;
				}
		}
		*p=0;
		printf("Case #%d: [",Case);
		if (p!=re)
			printf("%c",*re);
		for(char *j=re+1;j<p;j++)
			printf(", %c",*j);
		printf("]\n");
	}
	return 0;
}
