#include<stdio.h>
#include<string.h>
#define L 20
#define D 5000+10
#define N 500+10
char word[D][L];
char patten[N][600];
bool match[L][27];                //第i个位置是否能放字母j
int main()
{
	int i,j,k,l,d,n;
//	freopen("A-large.in","r",stdin);
//	freopen("out.txt","w",stdout);
	while(scanf("%d%d%d",&l,&d,&n)!=EOF)
	{
		for(i=0;i<d;++i)
			scanf("%s",word[i]);
		for(i=0;i<n;++i)
			scanf("%s",patten[i]);
		for(i=0;i<n;++i)
		{
			memset(match,false,sizeof(match));
			bool flag=false;
			int p=0;
			int len=strlen(patten[i]);
			for(j=0;j<len;++j)
			{
				if(patten[i][j]=='(')
					flag=true;
				else if(patten[i][j]==')')
					flag=false,++p;
				else
				{
					match[p][patten[i][j]-'a']=true;
					if(!flag)
						++p;
				}
			}
			int ans=0;
			for(j=0;j<d;++j)
			{
				for(k=0;k<l;++k)
					if(!match[k][word[j][k]-'a'])
						break;
					if(k==l)
						++ans;
			}
			printf("Case #%d: %d\n",i+1,ans);
		}
	}
	return 0;
}