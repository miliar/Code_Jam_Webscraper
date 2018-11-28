#include <iostream>
#include <cstdio>

using namespace std;

char words[10001][11];
char list[101][30];
int visit[10001];
int score[10001];
int have[130];

int main()
{
	int tt;
	scanf("%d",&tt);
	for (int tc=1;tc<=tt;tc++)
	{
		int n,m;
		memset(have,0,sizeof(have));
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++)
		{
			scanf("%s",words[i]);
			int llll=strlen(words[i]);
			for (int q=0;q<llll;q++)
				have[words[i][q]]=1;
		}
		printf("Case #%d: ",tc);


		for (int i=0;i<m;i++)
		{
			scanf("%s",list[i]);
			memset(score,0,sizeof(score));
			for (int j=0;j<n;j++)
			{
				memset(visit,0,sizeof(visit));
				int ll=strlen(words[j]);
				for (int k=0;k<n;k++)
					if (strlen(words[k])!=ll) visit[k]=1;
				for (int k=0;k<26;k++)
				{
					if (have[list[i][k]]==0) continue;
					int f=0;
					for (int z=0;z<n;z++)
					{
						if (visit[z]) continue;
						int l=strlen(words[z]);
						for (int y=0;y<l;y++)
							if (words[z][y]==list[i][k]) {f=1;break;}
						if (f) break;
					}
					if (!f) continue;
					else
					{
						int f2=0;
						int l=strlen(words[j]);
						for (int z=0;z<l;z++)
						{
							if (words[j][z]==list[i][k])
							{
								f2=1;
								for (int y=0;y<n;y++)
									if ((!visit[y]) && words[y][z]!=list[i][k]) visit[y]=1;
							}
						}
						for (int z=0;z<l;z++)
							if (words[j][z]!=list[i][k])
								for (int y=0;y<n;y++)
									if ((!visit[y]) && words[y][z]==list[i][k]) visit[y]=1;
						if (!f2) score[j]++;
					}
				}
			}
			int max=-1,ind=0;
			for (int j=0;j<n;j++)
				if (score[j]>max) {max=score[j];ind=j;}
			if (i!=m-1) printf("%s ",words[ind]);
			else printf("%s\n",words[ind]);
		}
	}
	return 0;
}

