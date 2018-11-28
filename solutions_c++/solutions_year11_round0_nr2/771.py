#include <iostream>
#include <vector>
using namespace std;

int main()
{
	freopen("B-large.in","rt",stdin);
	freopen("outLarge.txt","wt",stdout);
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		char nw[27][27];
		memset(nw,0,sizeof(nw));
		char del[27][27];
		memset(del,0,sizeof(del));
		int c,d,n;
		scanf("%d",&c);
		for(int j=1;j<=c;j++)
		{
			char a,b,k;
			scanf("%c",&a);
			scanf("%c%c%c",&a,&b,&k);
			nw[a-'A'][b-'A']=k;
			nw[b-'A'][a-'A']=k;
		}
		scanf("%d",&d);
		for(int j=1;j<=d;j++)
		{
			char a,b;
			scanf("%c",&a);
			scanf("%c%c",&a,&b);
			del[a-'A'][b-'A']=1;
			del[b-'A'][a-'A']=1;
		}
		scanf("%d",&n);
		vector<char> s(n);
		int u=0;
		char f;
		scanf("%c",&f);
		for(int j=1;j<=n;j++)
		{
			char a;
			scanf("%c",&a);
			s[u++]=a;
			if(u>1)
			{
				if(nw[s[u-1]-'A'][s[u-2]-'A'])
				{
					s[u-2]=nw[s[u-1]-'A'][s[u-2]-'A'];
					u--;
					continue;
				}
				for(int k=0;k<u-1;k++)
					if(del[s[k]-'A'][s[u-1]-'A'])
					{
						u=0;
						break;
					}
			}
		}
		printf("Case #%d: [",i);
		for(int j=0;j<u;j++)
		{
			if(j!=0) printf(", ");
			printf("%c",s[j]);
		}
		printf("]\n");
	}
	fclose(stdout);
}