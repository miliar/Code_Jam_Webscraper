#include<iostream>
#include<string>
using namespace std;

int main()
{
	char grid[250][101];
	char str[101];
	int ncase,tcase;
	__int64 ans;
	int ii,jj,i,j,n,m,len;
	int part,maxpart,totalpart;
	scanf("%d",&ncase);
	grid[0][0]='/';
	grid[0][1]='\0';
	for(tcase=1;tcase<=ncase;tcase++)
	{
		ans=0;
		scanf("%d%d",&n,&m);
		n++;
		for(i=1;i<n;i++)
		{
			scanf("%s",grid[i]);
			len=strlen(grid[i]);
			grid[i][len]='/';
			grid[i][len+1]=0;
		}
		for(i=0;i<m;i++)
		{
			scanf("%s",str);
			len=strlen(str);
			str[len]='/';
			str[len+1]=0;

			totalpart=0;
			for(j=0;str[j]!='\0';j++)
			{
				if(str[j]=='/')
				{
					totalpart++;
				}
			}
			maxpart=0;
			for(j=0;j<n;j++)
			{
				ii=0;
				jj=0;
				for(part=0;grid[j][ii]!=0&&str[jj]!=0;ii++,jj++)
				{
					if(grid[j][ii]!=str[jj])
						break;
					if(grid[j][ii]=='/')
						part++;
				}
				if(part>maxpart)
					maxpart=part;
			}
			ans+=totalpart-maxpart;
			strcpy(grid[n++],str);
		}
		printf("Case #%d: %I64d\n",tcase,ans);
	}
	return 0;
}