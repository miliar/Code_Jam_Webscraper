#include <cstdio>
#include <vector>

using namespace std;

int N,M;

int board[1024][1024];

char buf[1024];
int dx[] = {-1,0};
int dy[] = {0,-1};

bool canCut(int size, int x, int y)
{
	for (int i=x; i<x+size; i++)
	{
		for (int j=y; j<y+size; j++)
		{
			if (board[i][j] == -1)
				return false;
			for (int k=0; k<2; k++)
			{
				int cx = i+dx[k];
				int cy = j+dy[k];
				if (cx-x < 0 || cy-y < 0)
					continue;
				if (board[i][j] == board[cx][cy])
					return false;
			}
		}
	}
	return true;
}
void DoCut(int size, int x, int y)
{
	for (int i=x; i<x+size; i++)
	{
		for (int j=y; j<y+size; j++)
		{
			board[i][j] = -1;
		}
	}
}

int cut(int size)
{
	int res = 0;
	for (int i=0; i+size<=N; i++)
	{
		for (int j=0; j+size<=M; j++)
		{
			if (canCut(size,i,j))
			{
				DoCut(size,i,j);
				res++;
			}
		}
	}
	return res;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0_out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		scanf("%d%d", &N, &M);
		for (int i=0; i<N; i++)
		{
			scanf("%s", buf);
			for (int j=0; j<M/4; j++)
			{
				int a = buf[j]-'0';
				if (buf[j] >= 'A' && buf[j] <= 'F')
					a = buf[j]-'A'+10;
				board[i][4*j+3] = (a&1)==0;
				board[i][4*j+2] = (a&2)==0;
				board[i][4*j+1] = (a&4)==0;
				board[i][4*j+0] = (a&8)==0;
			}
		}

		//for (int i=0; i<N; i++)
		//{
		//	for (int j=0; j<M; j++)
		//		printf("%d", board[i][j]);
		//	printf("\n");
		//}

		vector<pair<int, int> > res;
		for (int i=min(N,M); i>=1; i--)
		{
			int canCutNumber = cut(i);
			if (canCutNumber > 0)
				res.push_back(make_pair(i,canCutNumber));
		}
		printf("Case #%d: %d\n", t, res.size());
		for (int i=0; i<res.size(); i++)
		{
			printf("%d %d\n", res[i].first, res[i].second);
		}
	}
	return 0;
}