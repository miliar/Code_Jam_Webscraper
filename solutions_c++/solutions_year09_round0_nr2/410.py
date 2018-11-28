#include <iostream>
#include <queue>
using namespace std;
typedef struct
{
	int mi,mj;
}Node;
const int MAXN=110;
int Map[MAXN][MAXN];

Node own[MAXN][MAXN];

char key[MAXN][MAXN];
char hash[MAXN][MAXN];



queue<Node> q;
int H,W;

int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};

inline void Bfs(int mi,int mj)
{
	Node st;
	st.mi=mi;
	st.mj=mj;
	while (!q.empty())
	{
		q.pop();
	}

	q.push(st);

	while (!q.empty())
	{
		Node t=q.front();
		q.pop();

		int j;
		int lmin=INT_MAX;

		Node nn;
		int ni,nj;
		for (j=0;j<4;++j)
		{
			nn.mi=t.mi+dx[j];
			nn.mj=t.mj+dy[j];

			if (nn.mi<0||nn.mi>=H||nn.mj<0||nn.mj>=W)
			{
				continue;
			}

			if (Map[nn.mi][nn.mj]<lmin)
			{
				lmin=Map[nn.mi][nn.mj];
				ni=nn.mi;
				nj=nn.mj;
			}
		}

		if (lmin<Map[t.mi][t.mj])
		{
			nn.mi=ni;
			nn.mj=nj;
			q.push(nn);
		}
		else
		{
			own[mi][mj].mi=t.mi;
			own[mi][mj].mj=t.mj;
		}
	}
}

int main()
{
	int T;

	freopen("tes1.txt","r",stdin);
	freopen("res1.txt","w",stdout);

	scanf("%d",&T);

	int b=1;
	while (T--)
	{

		int i,j;

		scanf("%d%d",&H,&W);

		for (i=0;i<H;++i)
		{
			for (j=0;j<W;++j)
			{
				scanf("%d",&Map[i][j]);
			}
		}

		for (i=0;i<H;++i)
		{
			for (j=0;j<W;++j)
			{
				Bfs(i,j);
			}
		}

		memset(hash,0,sizeof(hash));
		char st='a';
		for (i=0;i<H;++i)
		{
			for (j=0;j<W;++j)
			{
				if (hash[own[i][j].mi][own[i][j].mj]==0)
				{
					hash[own[i][j].mi][own[i][j].mj]=st++;
				}

				key[i][j]=hash[own[i][j].mi][own[i][j].mj];
			}
		}

		printf("Case #%d: \n",b++);

		for (i=0;i<H;++i)
		{
			for (j=0;j<W;++j)
			{
				if (j!=0)
				{
					printf(" ");
				}
				printf("%c",key[i][j]);
			}
			puts("");
		}
	}
	return 0;
}