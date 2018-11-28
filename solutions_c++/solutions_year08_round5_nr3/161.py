#include<stdio.h>
#include<vector>
using namespace std;
int match[6402],vis[6402];
vector<int> V[6402];

int r,c;
int cnt;

void INSERT(int x1,int y1,int x2,int y2)
{
//	printf("%d %d %d %d\n",x1,y1,x2,y2);

	V[x1*c+y1].push_back(x2*c+y2);
	V[x2*c+y2].push_back(x1*c+y1);
	cnt++;
}


int BPM(int at)
{
	int sz,i,u;

	vis[at]=1;
	sz=V[at].size();
	for(i=0;i<sz;i++)
	{
		u=V[at][i];

		if(match[u]==-1)
		{
			match[at]=u;
			match[u]=at;
			return 1;
		}
		else if(vis[match[u]]==0 && BPM(match[u]))
		{
			match[at]=u;
			match[u]=at;
			return 1;
		}
	}

	return 0;
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	int T;
	int i,j;
	char word[100][100];
	int tot,ks;
	int z=0;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		scanf("%d%d",&r,&c);
		for(i=0;i<r;i++)
		{
			scanf("%s",word[i]);
		}

		for(i=0;i<r;i++) for(j=0;j<c;j++) V[i*c+j].clear();
z=0;
		for(i=0;i<r;i++) for(j=0;j<c;j++) if(word[i][j]=='x') z++;

		cnt=0;
		for(i=0;i<r;i++)
			for(j=0;j<c;j++)
			{
				if(word[i][j]=='x') continue;

				if(i-1>=0 && j-1>=0 && word[i-1][j-1]!='x')
					INSERT(i-1,j-1,i,j);
				if(i-1>=0 && j+1<c && word[i-1][j+1]!='x')
					INSERT(i-1,j+1,i,j);
				if(j-1>=0 && word[i][j-1]!='x')
					INSERT(i,j-1,i,j);
				if(j+1<c && word[i][j+1]!='x')
					INSERT(i,j+1,i,j);
			}
//			printf("%d\n",cnt);


		cnt=0;
		tot=r*c;
		for(i=0;i<tot;i++) match[i]=-1;

		for(i=0;i<tot;i++)
			if(match[i]==-1)
			{
				for(j=0;j<tot;j++) vis[j]=0;
				if(BPM(i)) cnt++;
			}

//		printf("%d\n",cnt);

		printf("Case #%d: %d\n",ks,r*c-cnt-z);

	}

	return 0;
}