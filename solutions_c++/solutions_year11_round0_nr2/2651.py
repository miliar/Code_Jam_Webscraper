#include<stdio.h>
char c[40][4],e[30][3],str[105],ans[105];
int C,D,l;
int find(char c1,char c2)
{
	int j;
	for(j=0;j<C;j++)
		if((c[j][0]==c1&&c[j][1]==c2)||(c[j][0]==c2&&c[j][1]==c1))
			return j;
	return -1;
}
void eli(char ch)
{
	int i,j,k;
	for(i=0;i+1<l;i++)
		for(k=0;k<D;k++)
			if((ans[i]==e[k][0]&&ch==e[k][1])||(ans[i]==e[k][1]&&ch==e[k][0]))
			{
				l=0;
				return;
			}
}
int main()
{
	int cas,i,n,index;
	//freopen("b.in","r",stdin);
	//freopen("2.txt","w",stdout);
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;ii++)
	{
		scanf("%d",&C);
		for(i=0;i<C;i++)
			scanf("%s",c[i]);
		scanf("%d",&D);
		for(i=0;i<D;i++)
			scanf("%s",e[i]);
		scanf("%d%s",&n,str);
		l=0;
		for(i=0;i<n;i++)
		{
			if(l==0)
				ans[l++]=str[i];
			else
			{
				index=find(str[i],ans[l-1]);
				if(index>=0)
					ans[l-1]=c[index][2];
				else
				{
					ans[l++]=str[i];
					eli(ans[l-1]);
				}
			}
		}
		printf("Case #%d: [",ii);
		for(i=0;i<l;i++)
		{
			if(i)
				printf(", ");
			printf("%c",ans[i]);
		}
		printf("]\n");
	}
	return 0;
}