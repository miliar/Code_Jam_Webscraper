#include<iostream>
#include<cstdio>
#include<string.h>
#include<math.h>
#include<vector>
using namespace std;
int cv(char s)
{
	return s-'A';
}
int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	int t,i,j,C,D,N;
	char in[120];
	scanf("%d",&t);
	for(int ca=1;ca<=t;ca++)
	{
		vector<int> com[26];
		vector<int> bec[26];
		vector<int> opp[26];
		scanf("%d",&C);
		for(i=0;i<C;i++)
		{
			scanf("%s",in);
			com[cv(in[0])].push_back(cv(in[1]));
			bec[cv(in[0])].push_back(cv(in[2]));
			com[cv(in[1])].push_back(cv(in[0]));
			bec[cv(in[1])].push_back(cv(in[2]));
		}
		scanf("%d",&D);
		for(i=0;i<D;i++)
		{
			scanf("%s",in);
			opp[cv(in[0])].push_back(cv(in[1]));
			opp[cv(in[1])].push_back(cv(in[0]));
		}
		scanf("%d",&N);
		scanf("%s",in);
		int tail,que[110];
		tail=0;
		for(i=0;i<N;i++)
		{
			bool f=false;
			if(tail>0)
			{
				int p=-1;
				for(j=0;j<com[cv(in[i])].size();j++)
					if(com[cv(in[i])][j]==que[tail-1])
					{
						p=bec[cv(in[i])][j];
						break;
					}
				if(p!=-1)
				{
					que[tail-1]=p;
					f=true;
				}
			}
			if(!f)
			{
				bool clear = false;
				for(int h=0;h<tail && !clear;h++)
					for(j=0;j<opp[cv(in[i])].size() && !clear;j++)
						if(que[h]==opp[cv(in[i])][j])
							clear = true;
				if(clear)
				{
					tail=0;
				}
				else
					que[tail++]=cv(in[i]);
			}
		}
		printf("Case #%d: [",ca);
		for(i=0;i<tail;i++)
		{
			printf("%c",char(que[i]+'A'));
			if(i!=tail-1)
				printf(", ");
		}
		printf("]\n");
	}
	return 0;
}