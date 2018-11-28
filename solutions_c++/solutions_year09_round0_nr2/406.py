#include<iostream>
#include<vector>

using namespace std;

#define MAXH 100
#define MAXW 100

typedef pair<int,int> PII;

int M[MAXH][MAXW];
char basin[MAXH][MAXW];
char lastLetter;
int H,W;
int dir[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,tt;
	scanf("%d",&T);
	for(int tt=0;tt<T;tt++)
	{
		lastLetter = 'a'-1;
		scanf("%d%d",&H,&W);
		for(int i=0;i<H;i++)
			for(int j=0;j<W;j++)
				scanf("%d",&M[i][j]);
		memset(basin,0,sizeof(basin));

		for(int i=0;i<H;i++)
			for(int j=0;j<W;j++)
			{
				if (basin[i][j]) continue;
				char letter;
				vector<PII> L;
				PII current(i,j);
				L.push_back(current);
				bool end = false;
				while(!end&&!basin[current.first][current.second])
				{
					bool exist = false;
					PII lowest;
					int min;
					for(int k=0;k<4;k++)
					{
						PII next(current.first+dir[k][0],current.second+dir[k][1]);
						if (next.first<0||next.first>=H||next.second<0||next.second>=W||M[current.first][current.second]<=M[next.first][next.second]) continue;
						if (!exist||M[next.first][next.second]<min) { lowest=next; min=M[next.first][next.second]; }
						exist = true;
					}
					if (!exist) end = true;
					else
					{
						current = lowest;
						L.push_back(current);
					}
				}
				if (!basin[current.first][current.second]) letter = ++lastLetter;
				else letter = basin[current.first][current.second];
				for(int k=0;k<L.size();k++)
					basin[L[k].first][L[k].second] = letter;
			}

		printf("Case #%d:\n",tt+1);
		for(int i=0;i<H;i++)
		{
			printf("%c",basin[i][0]);
			for(int j=1;j<W;j++) printf(" %c",basin[i][j]);
			printf("\n");
		}
	}

	return 0;
}
