#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
int mat[130001][27];
int l,d,n;
char str[100000];
vector<char> layer[15];
int st;
int ans;
void dfs(int k,int x)
{
//	cout<<k<<","<<x<<endl;
	if(k==l)
		ans++;
	for(int i=0;i<layer[k].size();i++)
		if(mat[x][layer[k][i]-'a'])
			dfs(k+1,mat[x][layer[k][i]-'a']);
}
int main(void)
{
	freopen("A-large.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d%d%d",&l,&d,&n);
	st=1;
	memset(mat,0,sizeof(mat));
	int x;
	for(int i=0;i<d;i++)
	{
		scanf("%s",str);
		int len=strlen(str);
		x=0;
		for(int j=0;j<len;j++)
		{
			int temp=str[j]-'a';
			if(!mat[x][temp])
			{
				mat[x][temp]=st;
				x=st++;	
			}
			else
				x=mat[x][temp];
		}
	}
	
	for(int cas=1;cas<=n;cas++)
	{
		scanf("%s",str);
		int len=strlen(str);
		int y=0;
		ans=0;
		for(int i=0;i<len;)
		{
			if(str[i]>='a'&&str[i]<='z')
			{
				layer[y].push_back(str[i]);
				y++;
				i++;
			}
			else
			{
				i++;
				while(str[i]!=')')
				{
					layer[y].push_back(str[i]);
					i++;
				}
				i++;
				y++;
			}
		}
		dfs(0,0);
		for(int i=0;i<y;i++)
		{
		//    printf("%d\n",layer[i].size());
			layer[i].clear();
		
		}
		printf("Case #%d: %d\n",cas,ans);

		
	}
	
	return 0;
}
