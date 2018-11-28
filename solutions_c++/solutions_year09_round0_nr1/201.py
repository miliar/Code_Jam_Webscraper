#include<stdio.h>
#include<string.h>
#define MAX 501
char c[MAX*10][20],temp[1000];
bool is[20][26];
int main()
{
	int l,i,j,k,d,n,cnt;
	freopen("out.txt","w",stdout);
	scanf("%d%d%d",&l,&d,&n);
	for(i=0;i<d;i++)
		scanf("%s",c[i]);
	for(i=0;i<n;i++)
	{
		scanf("%s",temp);
		memset(is,0,sizeof(is));
		for(k=j=0;j<l;j++)
		{
			if(temp[k]=='(')
			{
				k++;
				while(temp[k]!=')')
				{
					is[j][temp[k]-'a']=true;
					k++;
				}
				k++;
			}
			else
			{
				is[j][temp[k]-'a']=true;
				k++;
			}
		}
		for(cnt=j=0;j<d;j++)
		{
			for(k=0;k<l;k++)
				if(!is[k][c[j][k]-'a'])
					break;
			if(k==l)
				cnt++;
		}
		printf("Case #%d: %d\n",i+1,cnt);
	}
	return 0;
}