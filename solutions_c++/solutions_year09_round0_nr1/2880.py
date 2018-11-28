#include <iostream>
using namespace std;

char mystr[5000][16];
bool grid[15][26];

void updatagrid(int strindex)
{
	char ch;
	ch=getchar();
	if(ch!='(')
	{
		grid[strindex][ch-'a']=true;
		return;
	}
	ch=getchar();
	while(ch!=')')
	{
		grid[strindex][ch-'a']=true;
		ch=getchar();
	}
}

int main()
{
	int i,j,ncase,ans,flag;
	int l,d,n;
	while(scanf("%d%d%d",&l,&d,&n)!=EOF)
	{
		getchar();
		for(i=0;i<d;i++)
		{
			gets(mystr[i]);
		}
		for(ncase=1;ncase<=n;ncase++)
		{
			for(i=0;i<15;i++)
			{
				for(j=0;j<26;j++)
				{
					grid[i][j]=false;
				}
			}
			for(i=0;i<l;i++)
			{
				updatagrid(i);
			}
			getchar();

			ans=0;
			for(i=0;i<d;i++)
			{
				flag=1;
				for(j=0;j<l;j++)
				{
					if(!grid[j][mystr[i][j]-'a'])
					{
						flag=0;
						break;
					}
				}
				if(flag==1)
					ans++;
			}
			printf("Case #%d: %d\n",ncase,ans);
		}
	}
	return 0;
}
