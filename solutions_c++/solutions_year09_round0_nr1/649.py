#include<cstdio>
#include<iostream>

#define MAX_L 15+1
#define MAX_D 5000+1
#define MAX_N 500+1

using namespace std;

char Word[MAX_D][MAX_L];

bool Hash[MAX_L][26];

int main()
{
	//freopen("E:\\我的文档\\Visual Studio 2005\\Text_Data\\in","r",stdin);
	//freopen("E:\\我的文档\\Visual Studio 2005\\Text_Data\\out","w",stdout);
	int L,D,N;
	scanf("%d %d %d",&L,&D,&N);
	for(int i=0;i<D;i++) scanf(" %s",Word[i]);
	for(int Case=1;Case<=N;Case++)
	{
		memset(Hash,false,sizeof(Hash));
		for(int i=0;i<L;i++)
		{
			char c;
			scanf(" %c",&c);
			if(c=='(')
			{
				while(true)
				{
					scanf(" %c",&c);
					if(c==')') break;
					Hash[i][c-'a']=true;
				}
			}
			else Hash[i][c-'a']=true;
		}
		int Ans=0;
		for(int i=0;i<D;i++)
		{
			bool Same=true;
			for(int j=0;j<L;j++) if(!Hash[j][Word[i][j]-'a'])
			{
				Same=false;
				break;
			}
			if(Same) Ans++;
		}
		printf("Case #%d: %d\n",Case,Ans);
	}
	return 0;
}