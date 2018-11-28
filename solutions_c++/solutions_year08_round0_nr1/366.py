#pragma warning(disable:4786)
#include<stdio.h>
#include<string>
#include<map>
using namespace std;

char line[200];
map<string,int> M;
int u[1000];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int Q,query,S,i,ks,total,cnt,id;

	gets(line);
	sscanf(line,"%d",&Q);

	for(ks=1;ks<=Q;ks++)
	{
		gets(line);
		sscanf(line,"%d",&S);
		
		M.clear();
		for(i=1;i<=S;i++)
		{
			gets(line);
			M[line]=i;
			u[i]=0;
		}

		total=0;
		cnt=0;
		gets(line);
		sscanf(line,"%d",&query);
		while(query--)
		{
			gets(line);
			id=M[line];

			if(u[id]) continue;
			else
			{
				if(cnt==S-1)
				{
					for(i=1;i<=S;i++)
						u[i]=0;
					u[id]=1;
					total++;
					cnt=1;
				}
				else
				{
					u[id]=1;
					cnt++;
				}
			}
		}

		printf("Case #%d: %d\n",ks,total);
	}

	return 0;
}